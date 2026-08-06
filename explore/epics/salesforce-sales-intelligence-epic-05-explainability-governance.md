# Epic 05: Explainability, Audit & Governance

## Header

- **PRD**: `explore/prds/salesforce-sales-intelligence-prd.md`
- **HLD**: `explore/hlds/salesforce-sales-intelligence-hld.md`
- **Status**: Draft
- **Priority**: High

## Description

Ensure every insight is explainable, cite source records, log all queries and actions, and meet accessibility targets.

## Acceptance Criteria

- Every insight displays the Salesforce records used and a confidence level. `[FACT — PRD R8]`
- Audit log captures user query, retrieved records, model version, generated insight, and user action. `[FACT — PRD R10]`
- UI is keyboard navigable and screen-reader friendly, targeting WCAG 2.1 AA. `[ASSUMPTION — accessibility spec]`
- Error states are explained in plain language with suggested next actions. `[OPINION — accessibility spec]`

## Linked Tasks

- `working/01-pending-planning/DFT-0011.md` — Implement citations, confidence, and audit logging
- `working/01-pending-planning/DFT-0012.md` — Accessibility and error-recovery implementation
