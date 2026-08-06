# Task Sizing: DFT-0002

## Complexity Dimensions

### Technical Scope
- **Target folder**: `working/04-implementing/DFT-0002-build-permission-filtered-data-access-layer/`
- **File count**: ~3 files to create/modify (`salesforce_client.py`, `tests/test_salesforce_client.py`, `auth_helper.py`)
- **Cross-references**: ~4 references to validate (PRD R9, HLD, DFT-0001, ADR-003)
- **Integration points**: 1 external endpoint (Salesforce REST query)

## Effort Estimation

### Multi-Axis Scoring

| Axis | Score (0-3) | Rationale |
|------|------------|-----------|
| Scope / Surface Area | 1 | One client module and its tests; focused API. |
| Coupling / Interfaces | 2 | Consumes `auth_helper` tokens; DFT-0003/0006/0007 will consume this client. |
| Novelty / Uncertainty | 1 | Standard Salesforce REST + `requests`; pattern is well-known. |
| Dependencies | 2 | Requires a valid access token for live permission validation; mocks for unit tests. |
| Testing & Verification | 1 | Mostly unit-testable with mocked `requests`; one live smoke test optional. |
| Risk / Blast Radius | 2 | Permission leakage risk if queries bypass sharing; security-sensitive. |

### Total Complexity Score: 9 / 18

### Size Estimate
- **Shirt Size**: S
- **Time Estimate**: 2–4 days
- **Confidence**: medium

## Dependencies and Risk Factors

- **Blocking**: DFT-0001 must provide a working access token and `instance_url`.
- **Downstream**: DFT-0003, DFT-0006, DFT-0007, DFT-0009 depend on this client.
- **Security**: Token must not be logged or persisted; sharing model must be validated with a restricted test user.
