# Technical Approach: SDE-0001

## High-Level Strategy

Use the Salesforce **Web Server OAuth 2.0 flow** for a server-side assistant. The Connected App will be configured in a Salesforce sandbox with a callback URL pointing to the assistant backend. The backend exchanges the authorization code for access and refresh tokens, validates the test user, and confirms that permission-filtered queries can be executed. No tokens are persisted in this task; storage is deferred to SDE-0002.

## Architecture Decisions

### OAuth Flow: Web Server
- **Choice**: Use the Salesforce Web Server flow (authorization code, server-side exchange, refresh token).
- **Rationale**: The assistant has a backend that can keep the client secret confidential. This flow supports refresh tokens and is suitable for long-lived server access on behalf of a user.
- **Alternatives Considered**: User-agent flow (client secret cannot be protected), JWT bearer flow (more complex, not needed for user-delegated access).

### Token Handling
- **Choice**: Access token and refresh token are held in memory for the test; client ID/secret come from environment variables.
- **Rationale**: Minimises secret exposure and avoids committing credentials.
- **Alternatives Considered**: Storing tokens in a database (out of scope for this task).

### Test User
- **Choice**: Create or use a dedicated test Salesforce user with a known profile/territory for validating the OAuth flow.
- **Rationale**: Confirms that access tokens are tied to a real user and that permission filtering can be observed.

### Client Library
- **Choice**: Use `simple-salesforce` with an explicit OAuth login helper, or `requests` directly against `login.salesforce.com`/`test.salesforce.com`.
- **Rationale**: `simple-salesforce` is the de facto Python Salesforce client; direct `requests` keeps the OAuth logic visible and avoid hidden assumptions.
- **Alternatives Considered**: `salesforce-python-toolkit` (less maintained), native REST calls (higher effort).

## Component Changes

### Backend
- [ ] Add environment variables for `SALESFORCE_CLIENT_ID`, `SALESFORCE_CLIENT_SECRET`, `SALESFORCE_REDIRECT_URI`, `SALESFORCE_LOGIN_URL`.
- [ ] Add a test script that builds the authorization URL, simulates or accepts the authorization code, calls the token endpoint, and lists the first few Leads to confirm access.
- [ ] Add a minimal error handler for OAuth errors (`invalid_grant`, `invalid_scope`, `access_denied`).

### Salesforce Sandbox
- [ ] Create Connected App with OAuth enabled, callback URL, and selected scopes.
- [ ] Relax IP restrictions for the sandbox if needed for local development.
- [ ] Record the consumer key and secret in the local secret manager.

## Data Model Changes

None for this task. OAuth credentials are environment configuration; no persistent data model is introduced.

## Integration Points

- **Assistant backend ↔ Salesforce Authorization Server**: `GET /services/oauth2/authorize` and `POST /services/oauth2/token`.
- **Assistant backend ↔ Salesforce REST API**: `GET /services/data/v62.0/query` for a smoke-test SOQL query.
- **Secret manager ↔ Backend**: Environment variables or local `.env` file for local testing (never committed).

## Configuration

| Variable | Default | Description |
|----------|---------|-------------|
| `SALESFORCE_LOGIN_URL` | `https://test.salesforce.com` | Authorization and token endpoint base URL |
| `SALESFORCE_CLIENT_ID` | *(required)* | Connected App consumer key |
| `SALESFORCE_CLIENT_SECRET` | *(required)* | Connected App consumer secret |
| `SALESFORCE_REDIRECT_URI` | `http://localhost:8000/auth/callback` | OAuth callback URL |
| `SALESFORCE_SCOPES` | `api refresh_token` | Space-separated OAuth scopes |

## Dev Hints

- Use the Connected App’s “Manage Profiles” to restrict which users can authorize the app.
- Verify `api` and `refresh_token` scopes are selected; `refresh_token` must be requested explicitly.
- For local testing, obtain the authorization code manually by opening the generated authorize URL in a browser.
- Do not commit `.env` files; add them to `.gitignore`.
