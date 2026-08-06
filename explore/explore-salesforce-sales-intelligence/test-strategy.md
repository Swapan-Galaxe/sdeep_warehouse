# Test Strategy: Salesforce Sales Intelligence Assistant

## Header

- **PRD**: `explore/prds/salesforce-sales-intelligence-prd.md`
- **HLD**: `explore/hlds/salesforce-sales-intelligence-hld.md`
- **Status**: Draft
- **Last Updated**: 20260806
- **Owner**: `sdeep`

## Testing Pyramid

| Layer | Focus | Tools / Approach | Coverage Target |
|-------|-------|------------------|-----------------|
| Unit | Scoring, ranking, policy rules, data transformations | Python `pytest` `[ASSUMPTION]` | ≥ 80% `[OPINION — to be calibrated]` |
| Integration | Salesforce data access, permission filtering, agent tool calls | Sandbox Salesforce + mock LLM `[ASSUMPTION]` | All happy paths and major error paths `[OPINION]` |
| Contract | Inter-service/API boundaries | Pact or hand-written contract tests `[ASSUMPTION]` | API surface `[OPINION]` |
| E2E | Core user flows: ask question, view prioritised leads, accept recommendation | Playwright/Cypress `[ASSUMPTION]` | 3 critical flows `[OPINION]` |
| AI Quality | Hallucination, citation accuracy, policy compliance | Golden-question set, human evaluation `[OPINION]` | Before production release `[FACT]` |
| Performance | p95 query latency under representative load | Load tests in staging `[OPINION]` | Target from PRD Group 3 `[FACT]` |
| Accessibility | WCAG 2.1 AA conformance | axe-core, manual screen-reader checks `[ASSUMPTION]` | Critical user paths `[OPINION]` |
| Security | OAuth flow, permission leaks, PII handling | Security review + automated SAST `[ASSUMPTION]` | Before pilot `[OPINION]` |

## Test Data Strategy

- **Primary**: Salesforce sandbox with sanitised, representative data. `[ASSUMPTION]`
- **Synthetic**: Generate leads/opportunities/activities for edge cases (stale dates, missing fields). `[OPINION]`
- **Golden questions**: Curated set of expected questions with acceptable answers for AI regression. `[OPINION]`
- **PII handling**: No production customer data in test environments. `[FACT — compliance]`

## CI/CD Quality Gates

1. Unit + integration tests pass. `[OPINION]`
2. Lint and type checks pass. `[OPINION]`
3. AI quality benchmark passes (pre-release). `[OPINION]`
4. Security scan has no high/critical findings. `[OPINION]`
5. Accessibility audit passes for changed UI. `[OPINION]`

## Enrichment Log

| Date | Session | Changes |
|------|---------|---------|
| 20260806 | Step 5 Part 2 | Drafted test strategy from PRD Group 3 and HLD. |
