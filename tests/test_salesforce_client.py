"""Unit tests for salesforce_client.py."""

from unittest.mock import MagicMock, patch

import pytest

from auth_helper import SalesforceAuthError
from salesforce_client import SalesforceAPIError, execute_soql, query_user_records


def test_execute_soql_returns_records():
    """Given valid token, execute_soql returns Salesforce query result."""
    mock_resp = MagicMock()
    mock_resp.ok = True
    mock_resp.text = '{"totalSize": 1, "records": [{"Id": "001"}]}'
    mock_resp.json.return_value = {"totalSize": 1, "records": [{"Id": "001"}]}

    with patch("salesforce_client.requests.get", return_value=mock_resp) as mock_get:
        result = execute_soql("SELECT Id FROM User LIMIT 1", "token", "https://example.my.salesforce.com")

    assert result["totalSize"] == 1
    assert result["records"][0]["Id"] == "001"
    mock_get.assert_called_once()
    args, kwargs = mock_get.call_args
    assert args[0] == "https://example.my.salesforce.com/services/data/v62.0/query"
    assert kwargs["headers"]["Authorization"] == "Bearer token"
    assert kwargs["params"]["q"] == "SELECT Id FROM User LIMIT 1"


def test_execute_soql_raises_api_error():
    """Given non-OK response, execute_soql raises SalesforceAPIError."""
    mock_resp = MagicMock()
    mock_resp.ok = False
    mock_resp.status_code = 400
    mock_resp.text = '{"message": "malformed query"}'
    mock_resp.json.return_value = {"message": "malformed query"}

    with patch("salesforce_client.requests.get", return_value=mock_resp):
        with pytest.raises(SalesforceAPIError) as exc:
            execute_soql("bad", "token", "https://example.my.salesforce.com")

    assert "malformed query" in str(exc.value)


def test_execute_soql_invalid_session_raises_auth_error():
    """Given 401, execute_soql raises SalesforceAuthError."""
    mock_resp = MagicMock()
    mock_resp.ok = False
    mock_resp.status_code = 401
    mock_resp.text = '{"message": "Session expired or invalid"}'
    mock_resp.json.return_value = {"message": "Session expired or invalid"}

    with patch("salesforce_client.requests.get", return_value=mock_resp):
        with pytest.raises(SalesforceAuthError):
            execute_soql("SELECT Id FROM User LIMIT 1", "token", "https://example.my.salesforce.com")


def test_execute_soql_retries_on_429_and_succeeds():
    """Given 429 then 200, execute_soql retries and returns result."""
    ok_resp = MagicMock()
    ok_resp.ok = True
    ok_resp.text = '{"totalSize": 0, "records": []}'
    ok_resp.json.return_value = {"totalSize": 0, "records": []}

    rate_limit_resp = MagicMock()
    rate_limit_resp.ok = False
    rate_limit_resp.status_code = 429
    rate_limit_resp.text = ""

    with patch("salesforce_client.requests.get", side_effect=[rate_limit_resp, ok_resp]) as mock_get:
        with patch("salesforce_client.time.sleep"):
            result = execute_soql("SELECT Id FROM User LIMIT 1", "token", "https://example.my.salesforce.com")

    assert result["totalSize"] == 0
    assert mock_get.call_count == 2


def test_query_user_records_builds_query():
    """query_user_records returns records and builds valid SOQL."""
    mock_resp = MagicMock()
    mock_resp.ok = True
    mock_resp.text = '{"totalSize": 2, "records": [{"Id": "001"}, {"Id": "002"]}'
    mock_resp.json.return_value = {"totalSize": 2, "records": [{"Id": "001"}, {"Id": "002"}]}

    with patch("salesforce_client.requests.get", return_value=mock_resp) as mock_get:
        result = query_user_records("Lead", "token", "https://example.my.salesforce.com", limit=5)

    assert result["totalSize"] == 2
    args, kwargs = mock_get.call_args
    assert kwargs["params"]["q"] == "SELECT Id FROM Lead LIMIT 5"


def test_query_user_records_with_owner_id():
    """query_user_records scopes query to OwnerId when provided."""
    mock_resp = MagicMock()
    mock_resp.ok = True
    mock_resp.text = '{"totalSize": 1, "records": [{"Id": "001"]}'
    mock_resp.json.return_value = {"totalSize": 1, "records": [{"Id": "001"}]}

    with patch("salesforce_client.requests.get", return_value=mock_resp) as mock_get:
        query_user_records(
            "Lead",
            "token",
            "https://example.my.salesforce.com",
            limit=10,
            owner_id="005xx000001X8YZAA0",
        )

    args, kwargs = mock_get.call_args
    assert "OwnerId = '005xx000001X8YZAA0'" in kwargs["params"]["q"]
    assert "LIMIT 10" in kwargs["params"]["q"]


def test_query_user_records_rejects_invalid_sobject():
    """query_user_records raises ValueError for invalid object name."""
    with pytest.raises(ValueError):
        query_user_records("Lead; DROP TABLE", "token", "https://example.my.salesforce.com")


def test_query_user_records_rejects_invalid_owner_id():
    """query_user_records raises ValueError for malformed owner id."""
    with pytest.raises(ValueError):
        query_user_records("Lead", "token", "https://example.my.salesforce.com", owner_id="bad id")
