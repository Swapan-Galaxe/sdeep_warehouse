# Information Architecture: Salesforce Sales Intelligence Assistant

## Header

- **PRD**: `explore/prds/salesforce-sales-intelligence-prd.md`
- **Status**: Draft
- **Last Updated**: 20260806
- **Owner**: `sdeep`

## Top-Level Structure

```
Salesforce Sales Intelligence Assistant
├── Conversational Query (primary entry point)
│   ├── Natural-language input
│   ├── Suggested prompts
│   └── Follow-up clarifications
├── Insights Feed
│   ├── Prioritised leads
│   ├── At-risk opportunities
│   ├── Weekly focus
│   └── Forecast summary
├── Record Detail View
│   ├── Cited Salesforce records
│   ├── Confidence and reasoning
│   └── Recommended actions
├── Search & RAG
│   ├── Similar opportunities
│   └── Conversation/document snippets
└── Settings & Trust
    ├── Data sources
    ├── Policy reminders
    └── Feedback / corrections
```

## Navigation Principles

- Every screen supports returning to the conversational query within one click. `[OPINION]`
- Insights are grouped by user intent (prioritise, monitor, forecast, search, act). `[OPINION]`
- Record citations are visible and linked to Salesforce detail pages. `[FACT — compliance]`
- No hidden settings; trust controls are reachable from any recommendation. `[OPINION]`

## Enrichment Log

| Date | Session | Changes |
|------|---------|---------|
| 20260806 | Step 4 Part B | Drafted IA for the conversational assistant. |
