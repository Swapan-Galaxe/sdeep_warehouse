# Journey Maps: Salesforce Sales Intelligence Assistant

## Header

- **Signal**: `signal/signals/20260804-salesforce-sales-intelligence-assistant.md`
- **Explore Bundle**: `explore/explore-salesforce-sales-intelligence/explore-bundle.md`
- **Personas**: `explore/domain/personas-salesforce-sales-intelligence.md`
- **Status**: Active
- **Last Updated**: 20260806
- **Owner**: `sdeep`

## Journey 1: Sales Rep — Daily Priority Setting

| Stage | Current State | Pain / Opportunity | Emotion | Future State (to be designed in Step 3) |
|-------|---------------|--------------------|---------|------------------------------------------|
| 1. Plan the day | Reps open Salesforce and manually scan lists and dashboards `[ASSUMPTION]` | Time lost; risk of missing priority leads or deals `[FACT — from Signal]` | Frustrated | |
| 2. Ask a question | Reps click through reports or ask peers/managers for advice `[ASSUMPTION]` | Answers are slow or incomplete `[OPINION]` | Impatient | |
| 3. Gather evidence | Reps open multiple records to build context `[ASSUMPTION]` | Cognitive load; data scattered `[FACT — from Signal]` | Overwhelmed | |
| 4. Decide action | Reps decide next step based on memory and intuition `[ASSUMPTION]` | Inconsistent follow-up; missed opportunities `[FACT — from Signal business problems]` | Uncertain | |
| 5. Log activity | Reps update Salesforce manually `[ASSUMPTION]` | Administrative burden; often skipped `[OPINION]` | Bored | |

## Journey 2: Sales Manager — Pipeline Review

| Stage | Current State | Pain / Opportunity | Emotion | Future State (to be designed in Step 3) |
|-------|---------------|--------------------|---------|------------------------------------------|
| 1. Prepare review | Manager pulls reports and manually inspects each rep's pipeline `[ASSUMPTION]` | Time-consuming; surface-level view `[OPINION]` | Stressed | |
| 2. Identify risks | Manager relies on rep self-reporting or stale notes `[ASSUMPTION]` | At-risk deals hidden until too late `[FACT — from Signal business problems]` | Worried | |
| 3. Coach rep | Manager asks probing questions without shared data view `[ASSUMPTION]` | Coaching is generic, not evidence-based `[OPINION]` | Unsupported | |
| 4. Forecast | Manager aggregates stages and gut feel `[ASSUMPTION]` | Forecast confidence is low `[OPINION]` | Anxious | |

## Journey 3: Revenue Leader — Forecast Meeting

| Stage | Current State | Pain / Opportunity | Emotion | Future State (to be designed in Step 3) |
|-------|---------------|--------------------|---------|------------------------------------------|
| 1. Request forecast | Leader receives manually prepared spreadsheet or dashboard `[ASSUMPTION]` | Lacks drill-down or confidence scoring `[OPINION]` | Skeptical | |
| 2. Challenge assumptions | Leader asks for evidence behind key deals `[ASSUMPTION]` | Details are hard to surface quickly `[OPINION]` | Frustrated | |
| 3. Decide allocation | Leader uses intuition due to unclear risk signals `[ASSUMPTION]` | Decisions may be too conservative or too optimistic `[OPINION]` | Uncertain | |

## Evidence Summary

| Claim Type | Count | Notes |
|------------|-------|-------|
| `[FACT]` | 5 | Sourced from Signal business problems and use case |
| `[OPINION]` | 10 | Inferred from Signal; needs validation through observation |
| `[ASSUMPTION]` | 10 | Workflow details assumed; validate with user research |

## Enrichment Log

| Date | Session | Changes |
|------|---------|---------|

## Future-State Target (Step 4)

### Journey 1: Sales Rep — Daily Priority Setting

| Stage | Future State | Emotion |
|-------|--------------|---------|
| 1. Plan the day | Assistant greets rep with prioritised leads and at-risk deals on open | Confident |
| 2. Ask a question | Rep types a natural-language question and receives an answer with citations within seconds | Satisfied |
| 3. Review insight | Rep sees a ranked list with reasoning and source records | Informed |
| 4. Act | Rep accepts, edits, or rejects a recommended action; system logs it as a Salesforce task | Empowered |
| 5. Monitor | Rep returns later to see updated priorities and closed actions | In control |

### Journey 2: Sales Manager — Pipeline Review

| Stage | Future State | Emotion |
|-------|--------------|---------|
| 1. Prepare review | Dashboard shows pipeline health, risk counts, and forecast by team | Prepared |
| 2. Identify risks | At-risk deals are flagged with evidence and owner | Alert but calm |
| 3. Coach rep | Manager and rep view the same insight and decide actions together | Collaborative |
| 4. Forecast | Forecast includes confidence range and a drill-down into the riskiest deals | Confident |

### Journey 3: Revenue Leader — Forecast Meeting

| Stage | Future State | Emotion |
|-------|--------------|---------|
| 1. Request forecast | Leader asks for the quarterly forecast and receives a projection with confidence | Informed |
| 2. Challenge assumptions | Leader can drill into any deal and see the records behind the projection | Confident |
| 3. Decide allocation | Leader uses risk-adjusted insights to allocate resources | Decisive |

## Enrichment Log

| Date | Session | Changes |
|------|---------|---------|
| 20260806 | Discovery — Part B | Created current-state journey maps for Sales Rep, Manager, and Revenue Leader. |
| 20260806 | Step 4 Part B | Added future-state target journeys based on approved PRD. |
