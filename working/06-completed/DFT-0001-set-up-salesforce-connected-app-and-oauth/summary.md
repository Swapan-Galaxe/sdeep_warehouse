# Implementation Summary: DFT-0001 — Set up Salesforce Connected App and OAuth

## Metadata

**Task ID:** DFT-0001  
**Title:** Set up Salesforce Connected App and OAuth  
**Implemented By:** Human + LLM  
**Date Completed:** 2026-08-06  
**Status:** Completed

## Implementation Approach

Implemented a standalone Python OAuth helper for the Salesforce Web Server flow. The module loads environment-based credentials, builds the Salesforce authorize URL, exchanges an authorization code for tokens, refreshes access tokens, and provides a smoke SOQL query. A manual end-to-end script (`tests/test_oauth.py`) wires these helpers together for live sandbox validation.

### Key Components Implemented

- **`auth_helper.py`**: Core OAuth utilities (`load_config`, `build_authorize_url`, `exchange_code`, `refresh_access_token`, `build_smoke_query`, `SalesforceAuthError`).
- **`tests/test_auth_helper.py`**: Unit tests with mocked `requests.post` responses.
- **`tests/test_oauth.py`**: Manual integration script that walks through authorize, token exchange, refresh, and a smoke SOQL query.
- **`.env.example`**: Template for required environment variables.
- **`.gitignore`**: Excludes `.env`, `__pycache__`, and pytest cache.

### Technologies & Libraries Used

- Python 3.13.14
- `requests` 2.32.5 for HTTP calls
- `pytest` 9.1.1 for unit tests
- `unittest.mock` for isolating HTTP interactions in unit tests

## Divergences from Original Specification

No material divergences. The original plan specified `auth_helper.py`, `.env.example`, `test_oauth.py`, and `.gitignore`; all were created. The integration tests remain manual because a live Salesforce sandbox with admin rights is required.

## Design Decisions

### Decision 1: Use `requests` directly rather than `simple-salesforce`

- **Context:** The plan suggested `simple-salesforce` or direct `requests`.
- **Decision:** Use direct `requests` calls for the OAuth endpoints.
- **Rationale:** Keeps the OAuth flow visible, small, and under team control. No additional third-party dependency beyond `requests`.
- **Implications:** Downstream data access tasks can choose to wrap `requests` or adopt `simple-salesforce` once the token is available.

### Decision 2: Environment-based configuration with `.env.example`

- **Context:** Credentials must not be committed.
- **Decision:** `load_config` reads `SALESFORCE_CLIENT_ID`, `SALESFORCE_CLIENT_SECRET`, `SALESFORCE_LOGIN_URL`, `SALESFORCE_REDIRECT_URI`, and `SALESFORCE_SCOPES` from environment variables.
- **Rationale:** Avoids hard-coded secrets and supports secret managers or `.env` files.
- **Implications:** Consumers of `auth_helper` must set environment variables before calling functions.

## Integration Points

### Dependencies Consumed

- **Salesforce OAuth endpoints**: `GET /services/oauth2/authorize`, `POST /services/oauth2/token`
- **Salesforce REST API**: `GET /services/data/v62.0/query` (used in `tests/test_oauth.py`)

### Interfaces Provided

- `build_authorize_url(config: dict) -> str`: Returns the Salesforce authorization URL.
- `exchange_code(config: dict, code: str) -> dict`: Exchanges an authorization code for tokens.
- `refresh_access_token(config: dict, refresh_token: str) -> dict`: Refreshes an access token.
- `load_config(env: Mapping | None) -> dict`: Validates and returns OAuth configuration.

## Testing Approach

### Test Coverage

- **Unit Tests:** 6 passing tests covering URL construction, token exchange, token refresh, config validation, and smoke query generation.
- **Integration Tests:** Manual end-to-end script (`tests/test_oauth.py`) for live sandbox validation.

### Test Scenarios Covered

- Authorize URL contains required OAuth parameters.
- Valid authorization code returns access and refresh tokens.
- Invalid/exchange error response raises `SalesforceAuthError`.
- Refresh token returns a new access token.
- Missing required environment variables raises `SalesforceAuthError`.
- Smoke SOQL query is syntactically valid.

### Known Test Gaps

- Live Salesforce OAuth flow and SOQL smoke query require sandbox credentials; not run in CI.
- Permission-filtered access is validated manually against a configured test user.

## Known Limitations

### Current Limitations

1. **No persistent token storage**: Tokens are returned to the caller; persistence is out of scope.
2. **No automatic retry or token caching**: Each call is stateless.
3. **Manual end-to-end testing**: Live integration requires a real Salesforce Connected App and test user.

## Future Work

### Immediate Follow-ups

- Configure a Connected App in the Salesforce sandbox with the callback URL and scopes from `.env.example`.
- Run `tests/test_oauth.py` with real credentials to validate the full flow.

### Recommendations for Dependent Tasks

- **DFT-0002** (permission-filtered data access): Consume `load_config` and use the returned access token to call Salesforce REST API endpoints.
- **DFT-0003** (API gateway and auth middleware): Use `build_authorize_url` to initiate login and `exchange_code`/`refresh_access_token` to manage session tokens.

## Configuration & Deployment Notes

### Environment Variables

- `SALESFORCE_LOGIN_URL`: Authorization base URL (default `https://test.salesforce.com`).
- `SALESFORCE_CLIENT_ID`: Connected App consumer key (required).
- `SALESFORCE_CLIENT_SECRET`: Connected App consumer secret (required).
- `SALESFORCE_REDIRECT_URI`: OAuth callback URL (default `http://localhost:8000/auth/callback`).
- `SALESFORCE_SCOPES`: Space-separated scopes (default `api refresh_token`).

### Deployment Considerations

- Never commit `.env` or tokens.
- Run `py -m pytest` before committing.

## References

- **Task:** `work/04-implementing/DFT-0001-set-up-salesforce-connected-app-and-oauth/task.md`
- **Plan:** `work/04-implementing/DFT-0001-set-up-salesforce-connected-app-and-oauth/plan.md`
- **Epic:** `explore/epics/salesforce-sales-intelligence-epic-01-salesforce-data-access.md`
- **Decision:** `explore/decisions/salesforce-sales-intelligence-adr-003-salesforce-oauth.md`
