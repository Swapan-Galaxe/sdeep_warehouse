# User Flows: Salesforce Sales Intelligence Assistant

## Header

- **PRD**: `explore/prds/salesforce-sales-intelligence-prd.md`
- **Personas**: `explore/domain/personas-salesforce-sales-intelligence.md`
- **Status**: Draft
- **Last Updated**: 20260806
- **Owner**: `sdeep`

## Flow 1: Sales Rep — Get Top Priority Leads

1. Opens assistant dashboard or asks: "What are my top leads this week?" `[FACT — example question]`
2. System authenticates user and fetches user's owned Leads. `[FACT]`
3. Agent scores/ranks leads by score, activity, and conversion signals. `[OPINION]`
4. Results displayed with source citations and confidence. `[FACT]`
5. Rep selects a lead to view recommended next action. `[OPINION]`
6. Rep accepts, edits, or rejects recommendation; action optionally logged as a Task in Salesforce. `[ASSUMPTION]`

## Flow 2: Sales Manager — Review At-Risk Deals

1. Manager asks: "Which of my team's deals are at risk?" `[FACT — example question]`
2. System fetches Opportunities owned by manager's direct reports. `[FACT]`
3. Agent flags stalled/overdue deals and explains rationale. `[OPINION]`
4. Manager reviews list; drills into a deal for detail. `[OPINION]`
5. Manager coaches rep with cited evidence. `[OPINION]`

## Flow 3: Revenue Leader — Forecast Review

1. Leader asks: "What is our forecast for this quarter?" `[FACT — example question]`
2. System aggregates pipeline by stage/probability. `[FACT]`
3. Agent projects revenue with confidence range and highlights high-risk deals. `[OPINION]`
4. Leader challenges assumptions; system shows underlying records. `[OPINION]`

## Enrichment Log

| Date | Session | Changes |
|------|---------|---------|
| 20260806 | Step 4 Part B | Drafted core user flows for Sales Rep, Manager, and Revenue Leader. |
