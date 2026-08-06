"""Failing test skeletons for auth_helper.py (SDE-0001)."""

import pytest

from auth_helper import (
    SalesforceAuthError,
    build_authorize_url,
    build_smoke_query,
    exchange_code,
    load_config,
    refresh_access_token,
)


def test_build_authorize_url_includes_all_parameters():
    """Given config, build_authorize_url returns a URL with all required parameters."""
    pytest.fail("Test skeleton - not implemented")


def test_exchange_code_returns_tokens_on_success():
    """Given valid code, exchange_code posts to token endpoint and returns tokens."""
    pytest.fail("Test skeleton - not implemented")


def test_exchange_code_raises_on_error():
    """Given invalid code, exchange_code raises SalesforceAuthError."""
    pytest.fail("Test skeleton - not implemented")


def test_refresh_token_returns_new_access_token():
    """Given refresh token, refresh_access_token returns a new access token."""
    pytest.fail("Test skeleton - not implemented")


def test_load_config_missing_variable_raises():
    """Given missing env var, load_config raises an error."""
    with pytest.raises(SalesforceAuthError):
        load_config({})


def test_build_soql_smoke_query():
    """build_smoke_query returns a valid SOQL string."""
    pytest.fail("Test skeleton - not implemented")
