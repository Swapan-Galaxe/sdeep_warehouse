"""Salesforce OAuth helper stubs for SDE-0001."""


def build_authorize_url(config):
    """Build Salesforce OAuth authorize URL."""
    raise NotImplementedError


def exchange_code(config, code):
    """Exchange authorization code for access and refresh tokens."""
    raise NotImplementedError


def refresh_access_token(config, refresh_token):
    """Use a refresh token to obtain a new access token."""
    raise NotImplementedError


def load_config(env=None):
    """Load OAuth configuration from environment variables."""
    raise NotImplementedError


def build_smoke_query():
    """Return a safe SOQL query for validating token access."""
    raise NotImplementedError
