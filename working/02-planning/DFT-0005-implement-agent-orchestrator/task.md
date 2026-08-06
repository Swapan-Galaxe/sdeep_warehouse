+++
[sources]
epic = "explore/epics/salesforce-sales-intelligence-epic-02-conversational-query-orchestrator.md"
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
# DFT-0005: Implement agent orchestrator

## Description

Build the orchestrator that receives a parsed query and dispatches it to the appropriate reasoning path, starting with a single generalist agent.

## Acceptance Criteria

- Orchestrator routes common sales questions to a reasoning agent. `[FACT — PRD R1]`
- Reasoning traces are captured for explainability. `[OPINION — HLD]`
- Design supports future specialist agents without rework. `[OPINION — HLD]`

## Epic

- `explore/epics/salesforce-sales-intelligence-epic-02-conversational-query-orchestrator.md`

## Priority

High
