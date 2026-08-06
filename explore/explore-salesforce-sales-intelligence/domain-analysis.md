# Domain Analysis: Salesforce Sales Intelligence Assistant

## Header

- **Signal**: `signal/signals/20260804-salesforce-sales-intelligence-assistant.md`
- **Explore Bundle**: `explore/explore-salesforce-sales-intelligence/explore-bundle.md`
- **Status**: Active
- **Last Updated**: 20260805
- **Owner**: `sdeep`

## Domain Glossary

| Term | Definition | Usage |
|------|------------|-------|
| Lead | Unqualified prospect with potential interest | Scored and routed to sales reps |
| Opportunity | Potential revenue deal tracked through stages | Forecasted, risk-assessed, recommended for next actions |
| Pipeline | Aggregate view of opportunities by stage and time | Health and forecast source |
| Stage | Opportunity lifecycle phase | Drives probability and risk heuristics |
| Probability | Likelihood of opportunity closing | Forecast and risk input |
| Close Date | Expected opportunity close date | Used for overdue and forecast calculations |
| Amount | Expected revenue for an opportunity | Forecast and prioritisation input |
| Contact Role | Contact's relationship to an opportunity | Influence and follow-up targeting |
| Activity | Historical touchpoint (call, email, meeting, task) | Recency and engagement evidence |
| Task | Planned follow-up | Recommended by the assistant or owned by rep |
| Forecast | Revenue projection for a period | Aggregated from opportunities |
| RAG | Retrieval-Augmented Generation | Semantic search over documents/conversations |
| Agent | Specialist reasoning module | Handles one domain: lead, opportunity, risk, pricing, follow-up |
| Insight | Prioritised output with evidence | Presented to the user |
| Recommendation | Suggested action | User decides whether to act |

## Domain Model

### Core Entities and Relationships

```
Account 1--* Contact
Account 1--* Opportunity
Opportunity 1--* Contact (via Contact Role)
Opportunity 1--* Activity
Opportunity 1--* Task
Lead 0..1 -> Opportunity (conversion)
User (Rep/Manager) *--* Lead (owner)
User (Rep/Manager) *--* Opportunity (owner)
Insight *--1 Opportunity | Lead | Account
Recommendation *--1 User
Recommendation *--1 Opportunity | Lead
```

### Key Attributes

| Entity | Key Attributes |
|--------|----------------|
| Lead | Status, Source, Score, Owner, Last Activity, Converted |
| Opportunity | Stage, Amount, Close Date, Probability, Owner, Created Date, Last Activity |
| Activity | Type, Date, Duration, Notes, Related To |
| Task | Subject, Due Date, Priority, Status, Assigned To |
| User | Role, Territory, Permissions |

### Lifecycle States

- **Lead**: New → Working → Qualified / Unqualified → Converted
- **Opportunity**: Prospecting → Qualification → Proposal / Negotiation → Closed Won / Closed Lost
- **Task**: Not Started → In Progress → Completed → Overdue (if past due)

## Domain Rules and Constraints

- A lead score should influence prioritisation but does not replace rep judgment. `[OPINION]`
- An opportunity's close date in the past with an open stage is a stalled/overdue signal. `[FACT — from Signal business problems]`
- Probability is tied to stage and should be used cautiously for forecasting. `[ASSUMPTION]`
- Pricing guidance must not override company discount policy. `[FACT — from Signal constraints]`
- Recommendations should cite the Salesforce records used to generate them. `[OPINION — rationale: explainability]`

## User Roles and Responsibilities

| Domain Role | Responsibilities |
|-------------|------------------|
| Sales Representative | Owns leads/opportunities; executes follow-up; accepts or rejects recommendations |
| Sales Manager | Monitors pipeline health; reviews risk and forecast insights |
| Sales Operations | Defines data hygiene, fields, and workflow rules; validates metrics |
| Revenue Leader | Uses aggregate forecasts and risk summaries for planning |
| System | Ingests data, scores/ranks, generates insights, records explanations |

## Current State

- Salesforce is the system of record for leads, opportunities, contacts, accounts, activities, and tasks. `[FACT — from Signal]`
- Data is often scattered across objects and may be incomplete or stale. `[ASSUMPTION]`
- Reps currently search and synthesise data manually. `[FACT — from Signal]`
- No AI assistant is currently described as operational. `[FACT — from Signal]`

## Domain Risks and Unknowns

| Risk / Unknown | Impact | Resolution |
|----------------|--------|------------|
| Data quality of historical activities | Insights may be wrong | Data audit in Technical Feasibility |
| Stage/probability mapping not standardised | Forecasts unreliable | Confirm with Sales Operations |
| Multiple currencies / territories | Complexity for scoring and forecasting | Domain rule validation |
| Activity-recording habits vary by rep | Engagement signals inconsistent | User research in Part B |

## Domain Model Summary

The assistant operates on top of standard Salesforce CRM entities, with additional derived entities for `Insight` and `Recommendation`. It does not introduce new CRM records unless explicitly approved. The primary value is transforming existing data into prioritised, explainable guidance.

## Enrichment Log

| Date | Session | Changes |
|------|---------|---------|
| 20260805 | Discovery — Part A | Created domain glossary, model, and rules from Signal. |
