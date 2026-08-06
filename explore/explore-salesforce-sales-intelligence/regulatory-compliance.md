# Regulatory and Compliance Focus: Salesforce Sales Intelligence Assistant

## Header

- **Signal**: `signal/signals/20260804-salesforce-sales-intelligence-assistant.md`
- **Explore Bundle**: `explore/explore-salesforce-sales-intelligence/explore-bundle.md`
- **Status**: Active
- **Last Updated**: 20260805
- **Owner**: `sdeep` (Compliance Lead to be assigned)

## Applicable Standards and Policies

- Salesforce Data Processing Addendum / Acceptable Use Policy (as applicable to connected app). `[ASSUMPTION]`
- Organisation's internal data classification and acceptable use policy. `[ASSUMPTION]`
- Internal pricing, discount, and margin approval policies. `[ASSUMPTION]`
- Accessibility obligations for internal tooling (e.g., WCAG 2.1 AA target if applicable). `[ASSUMPTION]`

## Data Handling Rules

- Customer and prospect data is read from Salesforce; no persistent personal data should be stored beyond what is necessary for query/response state. `[OPINION — rationale: data minimisation]`
- Embeddings for RAG should avoid storing verbatim sensitive conversation content without review. `[OPINION]`
- Audit logs should capture which records were retrieved and used for each AI-generated insight. `[OPINION]`
- Consent and retention rules are inherited from Salesforce and organisational policy. `[ASSUMPTION]`

## Accessibility Requirements

- Conversational UI must be keyboard navigable. `[OPINION]`
- Results and recommendations must be readable by screen readers. `[OPINION]`
- Color must not be the only indicator for risk/priority levels. `[OPINION]`

## Copy and Disclosure Requirements

- Every recommendation must disclose its confidence level and data source. `[OPINION]`
- Pricing or discount guidance must include a policy reminder that it is not a binding approval. `[OPINION]`
- Forecasts must be labelled as projections, not guarantees. `[OPINION]`

## Evidence Requirements

- Audit trail: user query, retrieved records, model version, generated insight, user action. `[OPINION]`
- Policy review: Compliance Lead sign-off on financial guidance before release. `[OPINION]`
- Test evidence: explainability and accuracy benchmarks for AI outputs before production. `[OPINION]`

## Compliance Risk Register

| ID | Risk | Impact | Likelihood | Mitigation |
|----|------|--------|------------|------------|
| CR-1 | AI recommends a discount that violates company policy | High | Medium | Hard guardrails and human-in-the-loop for pricing actions |
| CR-2 | Personal data is retained in vector store without justification | High | Medium | Data minimisation review and retention policy |
| CR-3 | Unexplained forecast causes bad revenue decisions | High | Medium | Confidence scoring and source citations |
| CR-4 | Inaccessible UI excludes sales users | Medium | Low | WCAG 2.1 AA design target |

## Non-Negotiables

- Pricing and discount recommendations are advisory only and require human approval for execution. `[FACT — from Signal scope]`
- AI outputs must cite the Salesforce records used to generate them. `[OPINION]`
- No autonomous write action to Salesforce without explicit user confirmation. `[FACT — from Signal scope]`

## Compliance Acceptance Criteria

- [ ] Pricing guidance is gated by policy and approval workflow.
- [ ] All insights display data source and confidence.
- [ ] Audit logs record query, retrieved records, and user action.
- [ ] Accessibility target is defined and tested before release.

## Enrichment Log

| Date | Session | Changes |
|------|---------|---------|
| 20260805 | Discovery — Part A | Created compliance baseline from Signal; compliance owner to be assigned. |
