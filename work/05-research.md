# Research Findings: SDE-0001

## Search Terms

- OAuth
- Salesforce Connected App
- access token
- permission-filtered
- refresh token

## Decision Inventory

| Decision ID | Status | Key Requirement | Link |
|-------------|--------|-----------------|------|
| ADR-003 | Accepted | Authenticate users through a Salesforce Connected App using OAuth 2.0 and propagate user permissions to every query. | `explore/decisions/salesforce-sales-intelligence-adr-003-salesforce-oauth.md` |
| ADR-004 | Accepted | Pricing/discount guidance is advisory and requires human approval; not directly related to OAuth but reinforces permission model. | `explore/decisions/salesforce-sales-intelligence-adr-004-pricing-guardrails.md` |

## Related Tasks

| Task ID | Status | Relationship | Link |
|---------|--------|--------------|------|
| SDE-0001 | Planning | This task — establishes the authenticated connection. | `work/02-planning/SDE-0001-set-up-salesforce-connected-app-and-oauth/task.md` |
| SDE-0002 | Planning | Depends on SDE-0001 — needs the permission-filtered data access layer. | `work/02-planning/SDE-0002.md` |
| SDE-0003 | Planning | Needs the authenticated API gateway. | `work/02-planning/SDE-0003.md` |
| SDE-0010 | Planning | Uses the same permission/approval model for pricing guardrails. | `work/02-planning/SDE-0010.md` |

## Documentation References

| Document | Relevance | Link |
|----------|-----------|------|
| PRD — Salesforce Sales Intelligence Assistant | PRD R9: permission-filtered access; no autonomous writes; OAuth/Connected App constraints. | `explore/prds/salesforce-sales-intelligence-prd.md` |
| HLD — Salesforce Sales Intelligence Assistant | Security & Compliance section: OAuth, permission filtering, no credential storage. | `explore/hlds/salesforce-sales-intelligence-hld.md` |
| Architecture Context | Existing system landscape and technical constraints. | `explore/explore-salesforce-sales-intelligence/architecture-context.md` |
| Risk Register | Identifies T-5 permission leakage risk and mitigations. | `explore/explore-salesforce-sales-intelligence/risks.md` |

## Conflicts and Gaps

| Conflict/Gap | Description | Resolution |
|--------------|-------------|------------|
| No exact OAuth flow specified | ADR-003 commits to OAuth 2.0 but does not choose user-agent vs. web-server flow. | Choose during planning and document in `plan.md`. |
| Token lifetime / refresh strategy | PRD requires refresh but does not define strategy. | Research Salesforce token lifetime and include refresh handling in implementation plan. |
| Sandbox org details | No specific sandbox URL or admin contact is recorded. | Add an open question to the task file and resolve before implementation. |
