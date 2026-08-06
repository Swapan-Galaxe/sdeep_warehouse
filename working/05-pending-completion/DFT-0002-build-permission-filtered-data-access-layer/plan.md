# Implementation Plan: DFT-0002 — Build permission-filtered data access layer

## Task Reference

- **Task**: `working/04-implementing/DFT-0002-build-permission-filtered-data-access-layer/task.md`
- **Epic**: `explore/epics/salesforce-sales-intelligence-epic-01-salesforce-data-access.md`
- **PRD**: `explore/prds/salesforce-sales-intelligence-prd.md`
- **HLD**: `explore/hlds/salesforce-sales-intelligence-hld.md`
- **Dependency**: `working/06-completed/DFT-0001-set-up-salesforce-connected-app-and-oauth/task.md`

## 1. Problem Statement

DFT-0001 provides a valid OAuth access token for a Salesforce user. DFT-0002 must turn that token into a safe, reusable data-access layer that runs SOQL/REST queries under the authenticated user's context so that Salesforce's native sharing, profile, and territory permissions automatically restrict the returned records.

- **Current state**: Token is available but no query layer exists.
- **Desired state**: A `salesforce_client` module that can execute SOQL and REST calls using the user's token, with automatic rate-limit backoff, and return only records the user is authorised to see.
- **Business driver**: All downstream insights (lead scoring, opportunity risk, forecasting) depend on trustworthy, permission-filtered data.

## 2. Goals and Constraints

### Measurable Goals

- Provide `execute_soql` that runs a SOQL query with the user's access token.
- Provide `query_user_records` that scopes common objects to the calling user via `OwnerId`/`CreatedById`/`LastModifiedById` or `USING SCOPE Mine`.
- Handle 429 / `REQUEST_LIMIT_EXCEEDED` with exponential backoff and max retries.
- Raise a clear `SalesforceAuthError` / `SalesforceAPIError` on failures.
- Unit tests cover success, permission errors, and rate-limit retries without a live org.

### Constraints

- Use only the access token and `instance_url` returned by `auth_helper`.
- No credential storage in the code.
- No writes to Salesforce.
- Target Salesforce REST API v62.0.

### Non-Goals

- Full SOQL parser or dynamic object builder.
- Complex multi-object joins beyond what `execute_soql` accepts as raw SOQL.
- Caching or persistent token storage.

## 3. Related Work

- **DFT-0001** — OAuth token retrieval and refresh.
- **DFT-0003** — API gateway and auth middleware will consume this client.
- **DFT-0006/0007** — Lead scoring and opportunity risk need permission-filtered queries.
- **ADR-003** — Salesforce OAuth for permission propagation.
- **PRD R9** — permission-filtered access, no autonomous writes.

## 4. Technical Approach

### High-Level Strategy

Create a thin Python module `salesforce_client.py` that wraps `requests` calls to `/services/data/v62.0/query` and `/services/data/v62.0/sobjects/{sobject}/...`. The caller supplies the access token and `instance_url`; the client sets `Authorization: Bearer <token>` and lets Salesforce enforce CRUD/FLS/sharing. Rate limiting is handled by a small retry helper.

### Architecture Decisions

1. **Pass token in, no state** — keeps the client easy to test and avoids token lifecycle concerns.
2. **Exponential backoff on 429** — simple loop with `time.sleep`; no extra dependencies.
3. **Raw SOQL strings** — downstream agents can compose queries; the client only executes and validates responses.
4. **Raise domain exceptions** — `SalesforceAPIError` for non-auth failures, `SalesforceAuthError` for `INVALID_SESSION_ID`.

### Configuration

| Variable | Default | Description |
|----------|---------|-------------|
| `SALESFORCE_API_VERSION` | `v62.0` | REST API version segment |
| `SALESFORCE_QUERY_PAGE_SIZE` | `2000` | Not used in MVP; SOQL `LIMIT` is caller's responsibility |

### Component Changes

- `salesforce_client.py` — query execution, error handling, backoff.
- `tests/test_salesforce_client.py` — mocked unit tests.
- `auth_helper.py` — add `instance_url` extraction helper if missing.
- `requirements.txt` — add `requests` and `pytest` if not already present.

## 5. Architectural Context

```
auth_helper (OAuth)
       │
       ▼
 access_token + instance_url
       │
       ▼
salesforce_client.execute_soql(query, token, instance_url)
       │
       ▼
Salesforce REST API /services/data/v62.0/query
       │
       ▼
permission-filtered result JSON
```

Integration points:
- `GET /services/data/v62.0/query?q=<SOQL>`
- `GET /services/data/v62.0/sobjects/{SObject}/describe` (optional, for field discovery)

## 6. Pipeline Tests

- **Unit**: `execute_soql` success, error codes, 429 retry, invalid session.
- **Security**: No token logged; no credentials in code.
- **Quality**: pytest passes; `flake8` clean if configured.

## 7. Acceptance Criteria

See task `task.md`. In brief:

- Queries return only records visible to the authenticated user.
- User territory and profile permissions are respected.
- API rate limits are handled with backoff.

## 8. Risks and Dependencies

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Sharing not automatic via REST API | Low | High | Validate with a restricted test user |
| 429 rate limits in tests | Low | Medium | Mock retry path; live tests rate-limit aware |
| Token expiry during query | Low | High | Surface `INVALID_SESSION_ID` clearly; caller refreshes via `auth_helper` |

### Dependencies

- **Blocking**: DFT-0001 (auth token).
- **Dependent**: DFT-0003, DFT-0006, DFT-0007, DFT-0009.

## 9. Implementation Phases

### Phase 1: Foundation
- Define `SalesforceAPIError`.
- Implement `execute_soql` with `requests` and response validation.

### Phase 2: Core Features
- Implement `query_user_records` helper for common objects.
- Add exponential backoff for 429 errors.

### Phase 3: Integration & Polish
- Unit tests with mocks.
- Run `pytest`; document usage for downstream tasks.

## 10. Dev Hints

- Always use `instance_url` from the token response, not `login_url`.
- For permission testing, create a Salesforce user with restricted record visibility.
- Keep the client stateless; callers manage token refresh.
