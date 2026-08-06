# Goals and Constraints: DFT-0001

## Measurable Goals

- [ ] **Connected App created**: A Connected App exists in a designated Salesforce sandbox and is configured for the assistant. (Verify by logging into the sandbox and viewing the Connected App details.)
- [ ] **OAuth flow working**: The assistant can exchange an authorization code for an access token and a refresh token for a test Salesforce user. (Verify by running an end-to-end OAuth test script.)
- [ ] **Scopes correct**: The Connected App requests only the Salesforce OAuth scopes required for Leads, Contacts, Accounts, Opportunities, Tasks, and user info. (Verify by reviewing the Connected App scope list against PRD R9.)
- [ ] **Token refresh documented**: A token refresh mechanism is documented and tested for the chosen flow. (Verify by documenting the refresh call and expiry handling.)
- [ ] **No credential storage in assistant**: Client ID/secret and tokens are not hard-coded or stored in the assistant codebase. (Verify by code/config review.)
- [ ] **Permission filtering validated**: The access token is tied to the authenticated user and respects profile/territory permissions in a test scenario. (Verify by querying Salesforce as a non-admin user and checking returned records.)

## Constraints

- **Timeline**: Pilot must be ready for user acceptance within one iteration; OAuth setup must not block downstream planning tasks.
- **Resources**: No dedicated Salesforce admin is assumed; setup instructions must be clear enough for a developer to execute.
- **Technical**: Must use standard Salesforce OAuth 2.0 (Web server or user-agent flow); no custom authentication extensions.
- **Compliance**: OAuth credentials must not be committed to the repository; all secrets must use a secret manager or environment variables. Token logs must not include raw access tokens.

## Non-Goals

- [ ] **No production org setup**: The Connected App will be configured in a sandbox; production org setup is out of scope for this task.
- [ ] **No UI for OAuth consent**: A user-facing consent screen is not required; the Connected App uses standard Salesforce consent.
- [ ] **No long-term token storage**: The assistant does not persist user tokens long-term; session handling is deferred to implementation tasks.
- [ ] **No data ingestion or scoring**: This task is limited to authentication and connection setup; lead scoring and insight generation are handled by DFT-0002+.

## Assumptions

| Assumption | Risk | Validation |
|------------|------|------------|
| A Salesforce sandbox is available and accessible to the team. | High | Confirm sandbox URL, admin credentials, and API access before implementation. |
| The assistant will run as a server-side component that can keep a client secret. | Medium | Confirm backend hosting model and secret-management approach. |
| The Web server OAuth flow is compatible with the assistant's UI architecture. | Medium | Review UI framework and callback handling with frontend lead. |
| Salesforce REST/SOQL API permissions can be granted through standard scopes. | Low | Verify scopes with Salesforce Connected App documentation. |
