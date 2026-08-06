# Epic 04: Recommendations & Follow-Up Actions

## Header

- **PRD**: `explore/prds/salesforce-sales-intelligence-prd.md`
- **HLD**: `explore/hlds/salesforce-sales-intelligence-hld.md`
- **ADR**: `explore/decisions/salesforce-sales-intelligence-adr-004-pricing-guardrails.md`
- **Status**: Draft
- **Priority**: Medium

## Description

Generate and present follow-up action recommendations and advisory pricing guidance with proper guardrails and human approval.

## Acceptance Criteria

- System suggests next action, owner, and due date for opportunities and leads. `[FACT — PRD R6]`
- User can accept, edit, or reject a recommendation. `[OPINION — wireframes]`
- Pricing/discount/margin guidance is advisory and references policy. `[FACT — PRD R5]`
- No pricing action is executed without human approval. `[FACT — PRD R12]`

## Linked Tasks

- `working/01-pending-planning/DFT-0009.md` — Build recommendation engine with citations
- `working/01-pending-planning/DFT-0010.md` — Implement pricing policy guardrails and approval workflow
