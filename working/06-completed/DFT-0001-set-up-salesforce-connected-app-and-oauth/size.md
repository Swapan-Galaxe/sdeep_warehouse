# Task Sizing: DFT-0001

## Complexity Dimensions

### Technical Complexity
- **Analysis Scope**: 1 target folder (`work/02-planning/DFT-0001-set-up-salesforce-connected-app-and-oauth/`)
- **File Count**: ~4 files to create/modify (`auth_helper.py`, `test_oauth.py`, `.env.example`, existing `task.md` frontmatter)
- **Cross-References**: ~6 references to validate (PRD, HLD, ADR-003, related tasks)
- **Integration Points**: 3 external endpoints (Salesforce authorize, token, REST API)

## Effort Estimation

### Multi-Axis Scoring

| Axis | Score (0-3) | Rationale |
|------|------------|-----------|
| Scope / Surface Area | 1 | A few new files in one auth module; no broad codebase changes. |
| Coupling / Interfaces | 2 | Introduces a new public OAuth helper interface that DFT-0002 and DFT-0003 will consume. |
| Novelty / Uncertainty | 1 | Standard Salesforce OAuth 2.0 flow; well-documented pattern, but sandbox-specific quirks may arise. |
| Dependencies | 2 | Requires a Salesforce sandbox, admin rights to create a Connected App, and a test user. |
| Testing & Verification | 2 | Needs live OAuth token exchange and a real smoke query; cannot be fully automated in CI without sandbox secrets. |
| Risk / Blast Radius | 2 | Security-sensitive (credentials, tokens); foundational for all downstream data access tasks. |

### Total Complexity Score: 10 / 18

### Size Estimate
- **Shirt Size**: M
- **Time Estimate**: 1–2 weeks
- **Confidence**: medium

## Dependencies and Risk Factors

- External: Salesforce sandbox availability and admin access.
- Security: Client secret and access tokens must not be committed or logged.
- Downstream: DFT-0002, DFT-0003, DFT-0005, DFT-0009 depend on this task.
