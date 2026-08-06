# DevOps Strategy: Salesforce Sales Intelligence Assistant

## Header

- **PRD**: `explore/prds/salesforce-sales-intelligence-prd.md`
- **HLD**: `explore/hlds/salesforce-sales-intelligence-hld.md`
- **Status**: Draft
- **Last Updated**: 20260806
- **Owner**: `sdeep`

## Environments

| Environment | Purpose | Salesforce Org | Notes |
|-------------|---------|----------------|-------|
| Local | Developer iteration | Developer sandbox `[ASSUMPTION]` | Mock LLM/vector store `[OPINION]` |
| CI | Automated tests / builds | N/A | Isolated, ephemeral `[OPINION]` |
| Staging | Integration and UAT | Staging sandbox `[ASSUMPTION]` | Representative data subset `[OPINION]` |
| Pilot | Limited user group | Pilot sandbox `[ASSUMPTION]` | Real users, measured adoption `[OPINION]` |
| Production | Live users | Production `[ASSUMPTION]` | Gated by pilot metrics `[OPINION]` |

## CI/CD Pipeline

1. **Build** — container image build, dependency vulnerability scan. `[OPINION]`
2. **Test** — unit, integration, contract, lint. `[OPINION]`
3. **AI Quality Gate** — golden-question evaluation on staging. `[OPINION]`
4. **Security Gate** — SAST, secrets scan, dependency audit. `[OPINION]`
5. **Deploy to Staging** — automated. `[OPINION]`
6. **Deploy to Pilot** — manual approval, feature flags. `[OPINION]`
7. **Deploy to Production** — manual approval, pilot metrics met. `[OPINION]`

## Observability

- **Metrics**: query latency, error rate, token usage, adoption, recommendation acceptance. `[OPINION]`
- **Logs**: structured logs with correlation ID; audit log for every query/insight. `[FACT — PRD]`
- **SLOs**: p95 query latency < 3s; availability 99.5% business hours pilot. `[OPINION]`
- **Alerting**: on-call for high error rate or latency degradation. `[OPINION]`

## DevSecOps

- Secrets stored in secret manager; never committed. `[OPINION]`
- SAST/DAST in CI; dependency scanning. `[OPINION]`
- Least-privilege service accounts. `[OPINION]`
- Model/version pinning and rollback capability. `[OPINION]`

## DORA Targets (Pilot)

| Metric | Target | Notes |
|--------|--------|-------|
| Lead time for changes | < 1 week for small changes | `[OPINION — to be calibrated]` |
| Deployment frequency | On demand for staging; weekly for pilot | `[OPINION — to be calibrated]` |
| Change failure rate | < 15% | `[OPINION — to be calibrated]` |
| Mean time to recovery | < 1 hour for critical issues | `[OPINION — to be calibrated]` |

## Enrichment Log

| Date | Session | Changes |
|------|---------|---------|
| 20260806 | Step 5 Part 2 | Drafted DevOps strategy from HLD deployment and monitoring sections. |
