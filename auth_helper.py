"""Salesforce OAuth helper stubs for SDE-0001."""

import os
import secrets
import urllib.parse as _urlparse


class SalesforceAuthError(Exception):
    """Raised when Salesforce OAuth configuration or token exchange fails."""


def build_authorize_url(config):
    """Build Salesforce OAuth authorize URL."""
    base = config["login_url"].rstrip("/")
    params = {
        "response_type": "code",
        "client_id": config["client_id"],
        "redirect_uri": config["redirect_uri"],
        "scope": config["scopes"],
        "state": secrets.token_urlsafe(16),
    }
    return f"{base}/services/oauth2/authorize?{_urlparse.urlencode(params)}"


def exchange_code(config, code):
    """Exchange authorization code for access and refresh tokens."""
    raise NotImplementedError


def refresh_access_token(config, refresh_token):
    """Use a refresh token to obtain a new access token."""
    raise NotImplementedError


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
    raise NotImplementedError
