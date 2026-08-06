# Risk Register: Salesforce Sales Intelligence Assistant

## Header

- **Status**: Active
- **Signal**: `signal/signals/20260804-salesforce-sales-intelligence-assistant.md`
- **PRD**: `explore/prds/salesforce-sales-intelligence-prd.md`
- **Last Updated**: 20260806
- **Owner**: `sdeep`

## Identified Risks

| ID | Risk | Category | Impact | Likelihood | Mitigation | Owner |
|----|------|----------|--------|------------|------------|-------|
| R1 | Salesforce data quality is insufficient for reliable AI insights | Data | High | Medium | Data quality assessment; prototype on clean subset | Lead Engineer |
| R2 | Multi-agent orchestration complexity exceeds team capacity | Technical | High | Medium | Begin with single-agent MVP | Lead Engineer |
| R3 | LLM latency or cost exceeds conversational UX budget | Technical | High | Medium | Benchmark candidates; streaming and caching | Architect |
| R4 | RAG corpus does not exist or is not accessible | Data | Medium | Medium | Validate conversation/document sources early | Lead Engineer |
| R5 | Permission model leaks data across users/teams | Security | High | Low | Enforce Salesforce user-context in all queries | Architect |
| R6 | AI recommends a discount that violates company policy | Compliance | High | Medium | Hard guardrails and human-in-the-loop for pricing | Compliance Lead |
| R7 | Personal data retained in vector store without justification | Compliance | High | Medium | Data minimisation review and retention policy | Architect |
| R8 | Unexplained forecast causes bad revenue decisions | Compliance | High | Medium | Confidence scoring and source citations | Product Manager |
| R9 | Sales users distrust AI recommendations | Adoption | High | Medium | Explainability, citations, pilot trust metrics | Product Manager |
| R10 | Scope grows beyond a deliverable first slice | Delivery | Medium | High | Strict first-slice definition in PRD; feature flags | Product Manager |

## Accepted Risks

| ID | Risk | Rationale | Owner |
|----|------|-----------|-------|
| AR-1 | WCAG 2.1 AA target may need specialist audit | Internal accessibility capacity to be assessed before pilot | Product Manager |
| AR-2 | Exact LLM/embedding provider not selected | To be resolved in Step 5 architecture; no delivery blocker yet | Architect |

## Risk Monitoring

- Review risk register weekly during pilot `[OPINION]`
- Add new risks discovered during Step 5 and implementation `[OPINION]`

## Enrichment Log

| Date | Session | Changes |
|------|---------|---------|
| 20260806 | Step 4 Part C | Consolidated risks from Explore Bundle, technical feasibility, compliance, and PRD. |
