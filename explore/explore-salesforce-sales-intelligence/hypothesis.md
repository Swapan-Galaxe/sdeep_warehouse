# Hypothesis: Salesforce Sales Intelligence Assistant

## Header

- **Status**: STAKEHOLDER-VALIDATED
- **Signal**: `signal/signals/20260804-salesforce-sales-intelligence-assistant.md`
- **Explore Bundle**: `explore/explore-salesforce-sales-intelligence/explore-bundle.md`
- **Created**: 20260806
- **Owner**: `sdeep`

## Statement

We believe **sales representatives** need a **natural-language, AI-powered assistant connected to Salesforce** that surfaces the highest-priority leads, at-risk deals, and recommended next actions, because **current workflows force reps to manually search and synthesise data across Lead and Opportunity records**. We will know this is true when **pilot users report reduced time-to-answer and act on assistant recommendations without repeatedly reverifying the underlying records**.

## Evidence Base

| Evidence | Source | Type |
|----------|--------|------|
| Signal identifies six business problems: lead prioritisation, at-risk deals, pipeline health, follow-up, pricing, and similar-opportunity search | Signal `[FACT]` | Confirmed |
| Example questions show reps ask for top priority leads, at-risk high-value deals, weekly focus, and follow-up plans | Signal `[FACT]` | Confirmed |
| User confirmed Lead and Opportunity are authoritative objects for this scope | User input, 20260806 `[FACT]` | Confirmed |
| No AI sales tools are currently in use, so greenfield opportunity exists | User input, 20260806 `[FACT]` | Confirmed |
| Persona and journey analysis indicates reps spend significant time scanning dashboards and manually gathering context | Discovery Part B `[OPINION/ASSUMPTION]` | To validate |

## Open Assumptions

| Assumption | Risk if Wrong | Owner |
|------------|---------------|-------|
| Salesforce data quality for Leads and Opportunities is sufficient for reliable AI insights | Recommendations may be wrong or ignored | Lead Engineer |
| Sales reps will trust and act on AI-generated guidance with source citations | Low adoption; wasted investment | Product Manager |
| A first slice can be narrowed to one high-frequency use case (e.g., top-priority leads or at-risk deals) | Scope creep and failed delivery | Product Manager |
| LLM/embedding latency and cost fit conversational UX budget | Degraded UX or unaffordable scaling | Architect |

## Measurable Signals

- **Adoption**: ≥ 60% of pilot reps use the assistant at least 3 times per day within 4 weeks. `[OPINION — target to be calibrated]`
- **Efficiency**: Pilot users report ≥ 30% reduction in time spent searching Salesforce for answers. `[OPINION — target to be calibrated]`
- **Action**: ≥ 50% of assistant recommendations are accepted or edited rather than ignored. `[OPINION — target to be calibrated]`
- **Trust**: ≤ 10% of recommendations are manually double-checked against source records. `[OPINION — target to be calibrated]`

## Stakeholder Validation

| Validator | Date | Outcome | Refinements |
|-----------|------|---------|-------------|
| sdeep | 20260806 | Approved | None |

## Enrichment Log

| Date | Session | Changes |
|------|---------|---------|
| 20260806 | Discovery — Part C | Drafted evidence-based hypothesis from Signal, user input, personas, and journeys. |
| 20260806 | Discovery — Part D | Validated by `sdeep`; status moved from DRAFT to STAKEHOLDER-VALIDATED. |
