# Implementation Plan: SDE-0001 — Set up Salesforce Connected App and OAuth

## Task Reference

- **Task**: `work/02-planning/SDE-0001-set-up-salesforce-connected-app-and-oauth/task.md`
- **Epic**: `explore/epics/salesforce-sales-intelligence-epic-01-salesforce-data-access.md`
- **Key decisions**: `explore/decisions/salesforce-sales-intelligence-adr-003-salesforce-oauth.md`
- **PRD**: `explore/prds/salesforce-sales-intelligence-prd.md`
- **HLD**: `explore/hlds/salesforce-sales-intelligence-hld.md`

## 1. Problem Statement

The Salesforce Sales Intelligence Assistant has no authenticated Salesforce connection. Without a Connected App and OAuth flow, the assistant cannot read Leads, Contacts, Opportunities, or Activities on behalf of a user. This task establishes the trusted identity and permission model that all later features depend on.

- **Current state**: No Connected App or OAuth integration exists.
- **Desired state**: A Connected App is configured in a Salesforce sandbox, OAuth scopes are defined, and the assistant can retrieve a valid access token for a test user.
- **Business driver**: Authentication is a hard prerequisite for lead prioritisation, opportunity risk detection, and all other assistant capabilities.

## 2. Goals and Constraints

### Measurable Goals

- Connected App exists in a designated Salesforce sandbox and is configured for the assistant.
- OAuth flow returns an access token and a refresh token for a test user.
- Scopes are limited to `api` and `refresh_token` plus any user-info scopes required.
- Token refresh mechanism is documented.
- No credentials are stored in the assistant codebase.
- Permission filtering can be validated with a test user.

### Constraints

- Use standard Salesforce OAuth 2.0 (Web Server or user-agent flow).
- Pilot must be ready within one iteration.
- No production org setup in this task.
- Credentials must use environment variables or a secret manager.

### Non-Goals

- Production Connected App setup.
- Custom consent UI.
- Long-term token persistence.
- Data ingestion or business logic.

## 3. Related Work

### Decisions

- **ADR-003** — Salesforce OAuth for authentication and permission propagation (Accepted).
- **ADR-004** — Policy guardrails for pricing guidance (Accepted).

### Related Tasks

- `SDE-0002` — Build permission-filtered data access layer (depends on this task).
- `SDE-0003` — Implement API gateway and auth middleware (depends on this task).
- `SDE-0005` — Implement agent orchestrator.
- `SDE-0010` — Implement pricing policy guardrails and approval workflow.

### Documentation References

- PRD R9: permission-filtered access, no autonomous writes.
- HLD Security & Compliance: OAuth, permission filtering, no credential storage.
- Risk Register: T-5 permission leakage.

## 4. Technical Approach

### High-Level Strategy

Use the Salesforce **Web Server OAuth 2.0 flow** for a server-side assistant. The backend builds the authorize URL, accepts the callback code, exchanges it for tokens, and runs a smoke SOQL query. Credentials come from environment variables; tokens are not persisted.

### Architecture Decisions

1. **Web Server OAuth flow** — chosen because the backend can keep the client secret confidential and refresh tokens are supported.
2. **Environment-based credentials** — `SALESFORCE_CLIENT_ID`, `SALESFORCE_CLIENT_SECRET`, `SALESFORCE_REDIRECT_URI`, and `SALESFORCE_LOGIN_URL`.
3. **Test user with known profile/territory** — validates permission-filtered access.
4. **Python `simple-salesforce` or direct `requests`** — keeps the OAuth logic visible and under team control.

### Configuration

| Variable | Default | Description |
|----------|---------|-------------|
| `SALESFORCE_LOGIN_URL` | `https://test.salesforce.com` | Authorization and token base URL |
| `SALESFORCE_CLIENT_ID` | required | Connected App consumer key |
| `SALESFORCE_CLIENT_SECRET` | required | Connected App consumer secret |
| `SALESFORCE_REDIRECT_URI` | `http://localhost:8000/auth/callback` | OAuth callback URL |
| `SALESFORCE_SCOPES` | `api refresh_token` | Space-separated scopes |

### Component Changes

- Add `auth_helper.py` module: authorization URL builder, token exchange, refresh token request.
- Add `test_oauth.py` script for end-to-end smoke test.
- Add `.env.example` and update `.gitignore`.
- Configure Connected App in Salesforce sandbox.

## 5. Architectural Context

See `work/09-architecture.md` for the Mermaid component diagram. The flow is:

1. Assistant UI or test script opens the Salesforce authorize URL.
2. Salesforce redirects to the backend callback with an authorization code.
3. Backend exchanges code + client secret for access/refresh tokens.
4. Backend runs a test SOQL query to confirm access and permission filtering.

Integration points:
- `GET /services/oauth2/authorize`
- `POST /services/oauth2/token`
- `GET /services/data/v62.0/query`

## 6. Pipeline Tests

- **Security**: No secrets committed; `.env` in `.gitignore`.
- **Functional**: OAuth flow test, callback URL match, smoke query, permission filtering.
- **Quality**: Lint/type checks; credential-handling review.

## 7. Acceptance Criteria

See `work/10-acceptance-criteria.md`. Key criteria:

- Connected App exists with correct callback URL and scopes.
- Backend exchanges authorization code for tokens.
- Smoke SOQL query returns records.
- Non-admin user only sees permitted records.
- No credentials are hard-coded or committed.

## 8. Risks and Dependencies

### Key Risks

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| Wrong org or callback URL | Medium | High | Verify sandbox and callback before running tests |
| Secret leak | Medium | High | Environment variables + secret scanning |
| Scope mismatch | Medium | High | Confirm `api` and `refresh_token` scopes |
| Sandbox access delay | High | Medium | Add sandbox readiness as prerequisite |

### Dependencies

- **Blocking**: None.
- **Dependent**: SDE-0002, SDE-0003, SDE-0005, SDE-0009.
- **Related**: SDE-0010, SDE-0011.

## 9. Implementation Phases

### Phase 1: Foundation
- Confirm sandbox and create `.env.example`.
- Implement authorization URL builder.
- Implement token exchange and error handling.

### Phase 2: Core Features
- Create Connected App in sandbox with correct scopes and callback.
- Run end-to-end OAuth flow with test user.
- Execute smoke SOQL query.

### Phase 3: Integration & Polish
- Permission-filtered smoke test.
- `.gitignore` and pipeline secret-scanning.
- Documentation for downstream tasks.

## 10. Dev Hints

- Use the Connected App “Manage Profiles” to restrict authorizing users.
- Include `refresh_token` scope explicitly in both Connected App and token request.
- For local testing, obtain the authorization code manually via browser.
- Never commit `.env` files.
