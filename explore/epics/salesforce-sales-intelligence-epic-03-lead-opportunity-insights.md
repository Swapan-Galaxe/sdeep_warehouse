# Epic 03: Lead & Opportunity Insights

## Header

- **PRD**: `explore/prds/salesforce-sales-intelligence-prd.md`
- **HLD**: `explore/hlds/salesforce-sales-intelligence-hld.md`
- **Status**: Draft
- **Priority**: High

## Description

Deliver prioritised lead ranking, opportunity risk/health detection, and pipeline forecasting using Salesforce data.

## Acceptance Criteria

- System ranks user's open Leads by score, activity, and conversion signals. `[FACT — PRD R2]`
- System flags opportunities with stale close dates, low activity, or stage-probability mismatches. `[FACT — PRD R3]`
- System projects revenue by period with a confidence range labelled as a projection. `[FACT — PRD R4]`
- All insights cite source records and confidence. `[FACT — PRD R8]`

## Linked Tasks

- `working/01-pending-planning/DFT-0006.md` — Implement lead scoring and prioritisation
- `working/01-pending-planning/DFT-0007.md` — Implement opportunity risk/health detection
- `working/01-pending-planning/DFT-0008.md` — Implement pipeline forecasting
