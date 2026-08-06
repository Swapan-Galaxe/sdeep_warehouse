"""Salesforce OAuth helper stubs for SDE-0001."""

import base64
import hashlib
import os
import secrets
import urllib.parse as _urlparse

import requests


class SalesforceAuthError(Exception):
    """Raised when Salesforce OAuth configuration or token exchange fails."""


def generate_pkce():
    """Generate a PKCE verifier/challenge pair for Salesforce OAuth."""
    verifier = secrets.token_urlsafe(96)
    digest = hashlib.sha256(verifier.encode("utf-8")).digest()
    challenge = base64.urlsafe_b64encode(digest).rstrip(b"=")
    return {
        "code_verifier": verifier,
        "code_challenge": challenge.decode("utf-8"),
        "code_challenge_method": "S256",
    }


def build_authorize_url(config, pkce=None):
    """Build Salesforce OAuth authorize URL."""
    base = config["login_url"].rstrip("/")
    params = {
        "response_type": "code",
        "client_id": config["client_id"],
        "redirect_uri": config["redirect_uri"],
        "scope": config["scopes"],
        "state": secrets.token_urlsafe(16),
    }
    if pkce:
        params["code_challenge"] = pkce["code_challenge"]
        params["code_challenge_method"] = pkce["code_challenge_method"]
    return f"{base}/services/oauth2/authorize?{_urlparse.urlencode(params)}"


def exchange_code(config, code, code_verifier=None):
    """Exchange authorization code for access and refresh tokens."""
    base = config["login_url"].rstrip("/")
    url = f"{base}/services/oauth2/token"
    payload = {
        "grant_type": "authorization_code",
        "code": code,
        "client_id": config["client_id"],
        "client_secret": config["client_secret"],
        "redirect_uri": config["redirect_uri"],
    }
    if code_verifier:
        payload["code_verifier"] = code_verifier
    response = requests.post(url, data=payload)
    body = response.json()
    if not response.ok:
        raise SalesforceAuthError(body.get("error_description", body.get("error", "Token exchange failed")))
    return body


def refresh_access_token(config, refresh_token):
    """Use a refresh token to obtain a new access token."""
    base = config["login_url"].rstrip("/")
    url = f"{base}/services/oauth2/token"
    payload = {
        "grant_type": "refresh_token",
        "refresh_token": refresh_token,
        "client_id": config["client_id"],
        "client_secret": config["client_secret"],
    }
    response = requests.post(url, data=payload)
    body = response.json()
    if not response.ok:
        raise SalesforceAuthError(body.get("error_description", body.get("error", "Token refresh failed")))
    return body


def load_config(env=None):
    """Load OAuth configuration from environment variables."""
    env = os.environ if env is None else env

    required = ["SALESFORCE_CLIENT_ID", "SALESFORCE_CLIENT_SECRET"]
    for key in required:
        if key not in env or not env[key]:
            raise SalesforceAuthError(f"Missing required environment variable: {key}")

    return {
        "client_id": env["SALESFORCE_CLIENT_ID"],
        "client_secret": env["SALESFORCE_CLIENT_SECRET"],
        "redirect_uri": env.get(
            "SALESFORCE_REDIRECT_URI", "http://localhost:8000/auth/callback"
        ),
        "login_url": env.get("SALESFORCE_LOGIN_URL", "https://test.salesforce.com"),
        "scopes": env.get("SALESFORCE_SCOPES", "api refresh_token"),
    }


def build_smoke_query():
    """Return a safe SOQL query for validating token access."""
    return "SELECT Id FROM User LIMIT 1"
