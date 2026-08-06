# Wireframes: Salesforce Sales Intelligence Assistant

## Header

- **PRD**: `explore/prds/salesforce-sales-intelligence-prd.md`
- **Status**: Draft
- **Last Updated**: 20260806
- **Owner**: `sdeep`
- **Note**: Low-fidelity text wireframes only. Visual design system not in scope without Figma design pipeline.

## Screen 1: Conversational Home

```
+--------------------------------------------------+
|  Salesforce AI Sales Intelligence Assistant      |
+--------------------------------------------------+
|  Hi Jordan. What would you like to know?         |
|  [What are my top leads today?    ] [Ask]        |
+--------------------------------------------------+
|  Suggested:                                      |
|  • Top leads this week                           |
|  • Deals at risk                                 |
|  • Forecast for this quarter                     |
+--------------------------------------------------+
```

## Screen 2: Prioritised Lead List

```
+--------------------------------------------------+
|  Your top 5 leads this week                      |
+--------------------------------------------------+
|  1. Acme Corp — score 92 [High]                  |
|     Source: Webinar, last activity: 1 hour ago   |
|     [View recommended next action]               |
|  2. Beta Inc — score 85 [Medium]                 |
|     ...                                          |
+--------------------------------------------------+
```

## Screen 3: Insight Detail

```
+--------------------------------------------------+
|  Insight: Acme Corp is a high-priority lead      |
+--------------------------------------------------+
|  Confidence: 88%                                 |
|  Based on: Lead score, last activity recency     |
|  Source records: [Lead: Acme Corp] [Activity]    |
+--------------------------------------------------+
|  Recommended next action:                        |
|  Schedule a discovery call by Friday.            |
|  [Accept] [Edit] [Reject]                        |
+--------------------------------------------------+
```

## Design Notes

- Conversational interface is the primary interaction model. `[FACT — Signal]`
- Every recommendation shows confidence, source records, and a policy reminder where relevant. `[FACT — compliance]`
- No autonomous action buttons; all write actions require explicit confirmation. `[FACT — scope]`

## Enrichment Log

| Date | Session | Changes |
|------|---------|---------|
| 20260806 | Step 4 Part B | Created low-fidelity text wireframes for core screens. |
