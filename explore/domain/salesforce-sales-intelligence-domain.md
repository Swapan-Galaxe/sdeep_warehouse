---
status: Locked
source: explore/explore-salesforce-sales-intelligence/domain-analysis.md
locked_date: 20260806
validated_by: sdeep
---

# Locked Domain Model: Salesforce Sales Intelligence Assistant

This is the locked final domain model for the PRD. No Step 3 refinements were produced; the model is taken directly from the approved domain analysis.

## Core Entities and Relationships

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

## Key Attributes

| Entity | Key Attributes |
|--------|----------------|
| Lead | Status, Source, Score, Owner, Last Activity, Converted |
| Opportunity | Stage, Amount, Close Date, Probability, Owner, Created Date, Last Activity |
| Activity | Type, Date, Duration, Notes, Related To |
| Task | Subject, Due Date, Priority, Status, Assigned To |
| User | Role, Territory, Permissions |

## Lifecycle States

- **Lead**: New → Working → Qualified / Unqualified → Converted
- **Opportunity**: Prospecting → Qualification → Proposal / Negotiation → Closed Won / Closed Lost
- **Task**: Not Started → In Progress → Completed → Overdue

## Domain Rules (Locked)

- A lead score influences prioritisation but does not replace rep judgment. `[OPINION]`
- An opportunity close date in the past with an open stage is a stalled/overdue signal. `[FACT]`
- Probability is tied to stage and should be used cautiously for forecasting. `[ASSUMPTION]`
- Pricing guidance must not override company discount policy. `[FACT]`
- Recommendations must cite the Salesforce records used to generate them. `[OPINION]`

## Enrichment Log

| Date | Session | Changes |
|------|---------|---------|
| 20260806 | Step 4 PRD lock | Locked domain model from Step 2 domain analysis. |
