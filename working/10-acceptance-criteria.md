# Acceptance Criteria: DFT-0001

## Epic Link

Addresses Epic AC: `salesforce-sales-intelligence-epic-01-salesforce-data-access` AC1, AC2, AC3.

## Happy Path Criteria

- [ ] **AC1**: A Connected App named `Salesforce Sales Intelligence Assistant` exists in the designated sandbox and has OAuth enabled.
- [ ] **AC2**: The Connected App has a callback URL matching `SALESFORCE_REDIRECT_URI` and includes the `api` and `refresh_token` scopes.
- [ ] **AC3**: Running the test script generates a valid Salesforce authorization URL for a test user.
- [ ] **AC4**: After the test user authorizes, the backend exchanges the authorization code for an access token and a refresh token.
- [ ] **AC5**: The backend can execute a test SOQL query (e.g. `SELECT Id, Name FROM Lead LIMIT 5`) and receive a successful response.

## Error Handling Criteria

- [ ] **AC6**: When the authorization code is invalid or expired, the backend returns a clear `invalid_grant` error without exposing the client secret.
- [ ] **AC7**: When the requested scope is not permitted, the backend returns an `invalid_scope` error and logs the scope that was rejected.
- [ ] **AC8**: When the user denies authorization, the callback handler returns an `access_denied` error and stops processing.
- [ ] **AC9**: Missing `SALESFORCE_CLIENT_ID` or `SALESFORCE_CLIENT_SECRET` environment variables cause the test script to fail fast with a descriptive message.

## Edge Case Criteria

- [ ] **AC10**: Token exchange works for both sandbox (`test.salesforce.com`) and production (`login.salesforce.com`) login URLs when configured.
- [ ] **AC11**: A non-admin test user can complete the flow and only receives records permitted by their profile/territory in the smoke query.

## Integration Criteria

- [ ] **AC12**: The backend uses environment variables for all Salesforce credentials; no credentials are hard-coded or committed.
- [ ] **AC13**: The OAuth helper is importable by DFT-0002 and DFT-0003 without requiring code changes to the helper.
