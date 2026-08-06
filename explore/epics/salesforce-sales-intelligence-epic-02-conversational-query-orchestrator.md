# Epic 02: Conversational Query & Orchestrator

## Header

- **PRD**: `explore/prds/salesforce-sales-intelligence-prd.md`
- **HLD**: `explore/hlds/salesforce-sales-intelligence-hld.md`
- **ADR**: `explore/decisions/salesforce-sales-intelligence-adr-001-multi-agent-orchestration.md`
- **Status**: Draft
- **Priority**: High

## Description

Implement the natural-language query interface, API gateway, and agent orchestrator that receives user questions and dispatches them to the appropriate reasoning path.

## Acceptance Criteria

- User can type a sales question and receive a natural-language answer. `[FACT — PRD R1]`
- API gateway validates OAuth tokens and routes requests. `[FACT — PRD]`
- Orchestrator starts with a single agent MVP and supports future specialist agents. `[OPINION — HLD]`
- Responses include source citations and confidence. `[FACT — PRD R8]`

## Linked Tasks

- `work/01-pending-planning/SDE-0003.md` — Implement API gateway and auth middleware
- `work/01-pending-planning/SDE-0004.md` — Build conversational UI
- `work/01-pending-planning/SDE-0005.md` — Implement agent orchestrator
