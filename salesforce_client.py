"""Permission-filtered Salesforce data access client."""

import re
import time

import requests

from auth_helper import SalesforceAuthError


class SalesforceAPIError(Exception):
    """Raised when a Salesforce REST API call fails for non-auth reasons."""


def _api_url(instance_url, version, path):
    return f"{instance_url.rstrip('/')}/services/data/{version}/{path.lstrip('/')}"


def _validate_sobject(sobject):
    if not re.fullmatch(r"[A-Za-z][A-Za-z0-9_]*", sobject):
        raise ValueError(f"Invalid Salesforce object name: {sobject}")
    return sobject


def _validate_id(sf_id):
    if not re.fullmatch(r"[A-Za-z0-9]{15,18}", sf_id):
        raise ValueError(f"Invalid Salesforce ID: {sf_id}")
    return sf_id


def execute_soql(
    query,
    access_token,
    instance_url,
    version="v62.0",
    max_retries=3,
    base_delay=1.0,
):
    """Run a SOQL query using the authenticated user's access token.

    Salesforce sharing, profile, and territory permissions are enforced
    automatically because the request is made with the user's token.
    """
    url = _api_url(instance_url, version, "query")
    headers = {"Authorization": f"Bearer {access_token}"}
    params = {"q": query}

    for attempt in range(max_retries + 1):
        response = requests.get(url, headers=headers, params=params)

        if response.status_code == 429:
            if attempt < max_retries:
                time.sleep(base_delay * (2 ** attempt))
                continue
            raise SalesforceAPIError("Rate limit exceeded after retries")

        if response.status_code == 401:
            body = response.json() if response.text else {}
            raise SalesforceAuthError(body.get("message", "Session expired or invalid"))

        if not response.ok:
            body = response.json() if response.text else {}
            raise SalesforceAPIError(
                f"{response.status_code}: {body.get('message', response.text)}"
            )

        return response.json()

    raise SalesforceAPIError("Rate limit exceeded after retries")


def query_user_records(
    sobject,
    access_token,
    instance_url,
    limit=100,
    version="v62.0",
    owner_id=None,
    max_retries=3,
    base_delay=1.0,
):
    """Query records for a given Salesforce object under the user's context.

    If `owner_id` is supplied the query is scoped to records owned by that
    user; otherwise the user's own sharing visibility is relied on.
    """
    sobject = _validate_sobject(sobject)
    soql = f"SELECT Id FROM {sobject}"
    if owner_id is not None:
        owner_id = _validate_id(owner_id)
        soql = f"{soql} WHERE OwnerId = '{owner_id}'"
    soql = f"{soql} LIMIT {int(limit)}"
    return execute_soql(
        soql,
        access_token,
        instance_url,
        version=version,
        max_retries=max_retries,
        base_delay=base_delay,
    )
