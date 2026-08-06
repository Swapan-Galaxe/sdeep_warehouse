# Pipeline Test Requirements: DFT-0001

## Security & Compliance Gates

- [ ] **No secrets committed**: CI scan must not find `SALESFORCE_CLIENT_SECRET`, `SALESFORCE_CLIENT_ID`, or access tokens in the codebase.
- [ ] **Environment variables documented**: Required environment variables are listed in a `.env.example` or deployment manifest.
- [ ] `.env` files are in `.gitignore`.

## Functional Gates

- [ ] **OAuth flow test**: A script can build a Salesforce authorization URL and request a token with `api` and `refresh_token` scopes. (This may be a semi-automated test requiring a sandbox user; for CI it can be skipped with a clear `SKIP` flag.)
- [ ] **Callback URL configured**: The configured `SALESFORCE_REDIRECT_URI` matches the Connected App callback URL.
- [ ] **Smoke query test**: After token exchange, a test SOQL query to `User` or `Lead` returns records for the authenticated test user.
- [ ] **Permission filtering test**: A non-admin test user sees only records they are authorised to see.

## Quality Gates

- [ ] All new files pass lint/type checks.
- [ ] OAuth client code is reviewed for credential handling.
- [ ] Error handling covers `invalid_grant`, `invalid_scope`, and `access_denied`.
