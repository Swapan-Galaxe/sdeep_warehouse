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
    from urllib.parse import parse_qs, urlparse

    config = {
        "login_url": "https://test.salesforce.com",
        "client_id": "abc",
        "redirect_uri": "http://localhost:8000/auth/callback",
        "scopes": "api refresh_token",
    }
    url = build_authorize_url(config)
    parsed = urlparse(url)
    query = parse_qs(parsed.query)

    assert parsed.scheme == "https"
    assert parsed.netloc == "test.salesforce.com"
    assert parsed.path == "/services/oauth2/authorize"
    assert query["response_type"] == ["code"]
    assert query["client_id"] == ["abc"]
    assert query["redirect_uri"] == ["http://localhost:8000/auth/callback"]
    assert query["scope"] == ["api refresh_token"]
    assert "state" in query and query["state"][0]


def test_exchange_code_returns_tokens_on_success():
    """Given valid code, exchange_code posts to token endpoint and returns tokens."""
    from unittest.mock import MagicMock, patch

    config = {
        "login_url": "https://test.salesforce.com",
        "client_id": "abc",
        "client_secret": "secret",
        "redirect_uri": "http://localhost:8000/auth/callback",
    }
    mock_resp = MagicMock()
    mock_resp.ok = True
    mock_resp.json.return_value = {
        "access_token": "atoken",
        "refresh_token": "rtoken",
    }

    with patch("auth_helper.requests.post", return_value=mock_resp) as mock_post:
        result = exchange_code(config, "authcode")

    assert result["access_token"] == "atoken"
    assert result["refresh_token"] == "rtoken"
    mock_post.assert_called_once()
    args, kwargs = mock_post.call_args
    assert args[0] == "https://test.salesforce.com/services/oauth2/token"
    assert kwargs["data"]["grant_type"] == "authorization_code"
    assert kwargs["data"]["code"] == "authcode"


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
    query = build_smoke_query()
    assert "SELECT" in query
    assert "FROM" in query
    assert "LIMIT 1" in query
