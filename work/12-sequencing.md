# Sequencing and Scope: SDE-0001

## Implementation Phases

### Phase 1: Foundation
- [ ] Confirm Salesforce sandbox and obtain Connected App creation rights.
- [ ] Set up local environment variables and `.env.example` (no secrets).
- [ ] Implement the OAuth authorization URL builder.
- [ ] Implement the token-exchange helper and error handler.

### Phase 2: Core Features
- [ ] Create the Connected App in the sandbox and configure callback URL/scopes.
- [ ] Run end-to-end OAuth flow with a test user and obtain access token.
- [ ] Execute a smoke SOQL query against the Salesforce REST API.

### Phase 3: Integration & Polish
- [ ] Add permission-filtered smoke test with a non-admin user.
- [ ] Add `.gitignore` and pipeline secret-scanning rule.
- [ ] Document the setup steps for SDE-0002 and SDE-0003 consumers.

## Parallel Work Opportunities

- The API gateway OAuth callback endpoint (`SDE-0003`) can be designed in parallel, using the helper interface defined in this task.
- The agent orchestrator (`SDE-0005`) and lead/opportunity insights (`SDE-0006/0007`) can continue design work while this task is being implemented, because the data access contract is known.

## Scope Validation

### Original Requirements
- Create and configure a Connected App: Addressed in Phase 2.
- Define OAuth scopes: Addressed in Phase 1/2.
- Validate authentication flow: Addressed in Phase 2/3.
- Document token refresh: Addressed in Phase 1 (technical approach) and Phase 3 (docs).

### Scope Creep Detected

- None. No production org setup, consent UI, or persistent token storage is included.

### Non-Goals Confirmed Excluded

- Production org setup.
- Custom consent UI.
- Long-term token persistence.
- Data ingestion or business logic (lead scoring, etc.).

## Task Tags

- **Complexity**: moderate
- **Component**: server
- **Type**: feature
- **Priority**: high
- **Risk**: medium
