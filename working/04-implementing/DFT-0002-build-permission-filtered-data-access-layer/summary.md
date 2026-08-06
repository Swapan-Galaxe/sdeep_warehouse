# Implementation Summary: DFT-0002 — Build permission-filtered data access layer

## Metadata

**Task ID:** DFT-0002  
**Title:** Build permission-filtered data access layer  
**Implemented By:** Human + LLM  
**Date Completed:** 2026-08-07  
**Status:** Completed

## Implementation Approach

Implemented a thin, stateless Salesforce REST client that executes SOQL queries under an authenticated user's token. Because the request is made with the user's own access token, Salesforce sharing, profile, and territory permissions are enforced automatically. The client also handles HTTP 429 rate-limit responses with exponential backoff and raises clear domain exceptions for auth and API failures.

### Key Components Implemented

- **`salesforce_client.py`**:
  - `SalesforceAPIError` for non-auth API failures.
  - `execute_soql(query, access_token, instance_url, ...)` — executes a raw SOQL query.
  - `query_user_records(sobject, access_token, instance_url, ...)` — convenience helper with optional `OwnerId` scoping and input validation.
- **`tests/test_salesforce_client.py`** — 8 unit tests covering success, API errors, invalid session, 429 retries, query building, and injection guards.

### Technologies & Libraries Used

- Python 3.13.14
- `requests` 2.32.5 for HTTP calls
- `pytest` 9.1.1 for unit tests
- `unittest.mock` for isolating HTTP interactions
- `auth_helper.SalesforceAuthError` reused for session failures

## Divergences from Original Specification

No material divergences. The task asked for a permission-filtered query layer with rate-limit backoff; all implemented.

## Design Decisions

### Decision 1: Stateless client that receives token and `instance_url`

- **Context:** DFT-0001 already retrieves and refreshes tokens. The data access layer should not duplicate that lifecycle.
- **Decision:** `execute_soql` and `query_user_records` take `access_token` and `instance_url` as arguments.
- **Rationale:** Keeps the client testable, avoids storing sensitive tokens, and lets callers refresh tokens as needed.
- **Implications:** Downstream tasks pass the token from `auth_helper` into `salesforce_client` for each query.

### Decision 2: Exponential backoff on HTTP 429

- **Context:** Salesforce REST API has per-org rate limits.
- **Decision:** Retry up to `max_retries` times with `base_delay * 2 ** attempt` seconds between attempts.
- **Rationale:** No extra dependency; simple and predictable.
- **Implications:** Very heavy query bursts may still exceed the retry budget; callers should monitor `REQUEST_LIMIT_EXCEEDED`.

### Decision 3: Reuse `SalesforceAuthError` for invalid sessions

- **Context:** An expired or revoked access token returns a 401 / `INVALID_SESSION_ID`.
- **Decision:** Map 401 responses to `SalesforceAuthError` from `auth_helper`.
- **Rationale:** Callers can catch a single `SalesforceAuthError` for any auth problem and trigger a token refresh.
- **Implications:** `salesforce_client.py` imports `SalesforceAuthError` from `auth_helper`.

## Integration Points

### Dependencies Consumed

- `auth_helper.SalesforceAuthError`
- Salesforce REST API `GET /services/data/v62.0/query`

### Interfaces Provided

- `execute_soql(query, access_token, instance_url, version="v62.0", max_retries=3, base_delay=1.0)` → `dict`
- `query_user_records(sobject, access_token, instance_url, limit=100, version="v62.0", owner_id=None, ...)` → `dict`

## Testing Approach

### Test Coverage

- **Unit Tests:** 8 passing tests in `tests/test_salesforce_client.py`.
- **Full Suite:** 16 tests pass across `tests/test_auth_helper.py` and `tests/test_salesforce_client.py`.

### Test Scenarios Covered

- Successful SOQL query returns expected JSON.
- Non-OK response raises `SalesforceAPIError`.
- 401 response raises `SalesforceAuthError`.
- 429 response triggers retry then success.
- `query_user_records` builds correct SOQL with and without `OwnerId`.
- Invalid `sobject` and `owner_id` inputs raise `ValueError`.

### Known Test Gaps

- Live permission-filtered validation with a restricted Salesforce test user is not automated; it requires a sandbox and real credentials.

## Known Limitations and Future Work

- No caching of query results; every call is a live Salesforce REST request.
- No `describe` or schema discovery in the MVP; callers must supply valid SOQL.
- `query_user_records` does not validate that the user can actually access the SObject; it relies on the REST API to return an auth error.

## References

- Task: `working/04-implementing/DFT-0002-build-permission-filtered-data-access-layer/task.md`
- Plan: `working/04-implementing/DFT-0002-build-permission-filtered-data-access-layer/plan.md`
- Epic: `explore/epics/salesforce-sales-intelligence-epic-01-salesforce-data-access.md`
- PRD: `explore/prds/salesforce-sales-intelligence-prd.md`
