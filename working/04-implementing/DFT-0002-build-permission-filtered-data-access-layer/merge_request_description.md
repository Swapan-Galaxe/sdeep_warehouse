# DFT-0002 - Build permission-filtered data access layer

## Purpose

Implement the layer that executes Salesforce SOQL/REST queries under the authenticated user's context, respecting Salesforce sharing, profile, and territory permissions, with automatic rate-limit backoff.

## Implementation

- Added `salesforce_client.py` with `execute_soql`, `query_user_records`, `SalesforceAPIError`, and 429 retry logic.
- Reused `SalesforceAuthError` from `auth_helper.py` for 401 / `INVALID_SESSION_ID` responses.
- Added `tests/test_salesforce_client.py` with 8 unit tests using mocked `requests` responses.
- Added `plan.md`, `size.md`, `summary.md`, and `assignments.toml` under the DFT-0002 task folder.

## Verification

```powershell
py -m pytest -v
# Expected: 16 passed
```

## Notes

- Live permission-filtered validation still requires a sandbox user with restricted visibility.
- No additional runtime dependencies beyond `requests` and `pytest`.
