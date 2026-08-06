# Risks and Dependencies: DFT-0001

## Risk Assessment

| Risk | Category | Likelihood | Impact | Mitigation |
|------|----------|------------|--------|------------|
| Connected App created in wrong org or with wrong callback URL | Operations | Medium | High | Document exact sandbox URL and callback in task; verify before running test script. |
| Client secret leaked in logs or committed to repository | Security | Medium | High | Use environment variables only; add secret-scanning to pipeline; never log tokens. |
| OAuth scope mismatch prevents lead/opportunity queries | Dependencies | Medium | High | Select `api` scope and confirm object-level permissions in the test user profile. |
| Sandbox unavailable or admin access delayed | Dependencies | High | Medium | Add sandbox readiness as a prerequisite; have a fallback test account. |
| Refresh token not issued due to missing `refresh_token` scope | Technical | Medium | High | Include `refresh_token` explicitly in Connected App and token request. |
| Token endpoint returns `invalid_grant` during local testing | UX | Medium | Low | Provide clear error messages and instructions for re-authorization. |
| IP restrictions block local callback | Security | Low | Medium | Whitelist local callback or use a tunnel for development; document in setup guide. |

## Dependencies

### Blocking (must complete first)

- None. This is the first task in the data access epic.

### Dependent (depends on this task)

- `DFT-0002` — Build permission-filtered data access layer (needs valid access token).
- `DFT-0003` — Implement API gateway and auth middleware (needs OAuth helper and callback logic).
- `DFT-0005` — Implement agent orchestrator (needs data access layer).
- `DFT-0009` — Build recommendation engine with citations (needs Salesforce query capability).

### Related (shared context)

- `DFT-0010` — Implement pricing policy guardrails and approval workflow (shares security and permission model).
- `DFT-0011` — Implement citations, confidence, and audit logging (needs query auditability).

## Validation Against Research

- [x] No conflicts with existing decisions — ADR-003 (OAuth) and ADR-004 (pricing guardrails) are aligned.
- [x] Dependencies align with related tasks — DFT-0002/0003/0005/0009/0010/0011 all require authenticated access.
- [x] No gaps or stale references — research from `work/05-research.md` confirms the Salesforce OAuth approach.

### Conflicts/Gaps Found

| Issue | Description | Resolution |
|-------|-------------|------------|
| Sandbox org not yet specified | No concrete sandbox URL or admin contact in existing artifacts. | Add an open task to confirm sandbox before implementation starts. |
