+++
[sources]
epic = "explore/epics/salesforce-sales-intelligence-epic-03-lead-opportunity-insights.md"
documents = []

[links]
blocks = []
related = []
parent = []
child = []

[workflow]
planned = ""
spec_complete = ""
implemented = ""
impl_complete = ""
completed = ""

[assignments]
planning = ""
implementation = ""
completed = ""
+++
# DFT-0008: Implement pipeline forecasting

## Description

Aggregate opportunities by period and probability to produce a revenue projection with a confidence range.

## Acceptance Criteria

- Forecast displays projected revenue and confidence range. `[FACT — PRD R4]`
- Forecast is labelled as a projection, not a guarantee. `[FACT — compliance]`
- Drill-down into highest-risk deals is supported. `[OPINION — wireframes]`

## Epic

- `explore/epics/salesforce-sales-intelligence-epic-03-lead-opportunity-insights.md`

## Priority

Medium
