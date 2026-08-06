# ADR-001: Multi-Agent Orchestration with ReAct

## Status

Accepted

## Context

The assistant must answer a variety of sales questions: lead prioritisation, opportunity risk, forecasting, pricing guidance, follow-up recommendations, and similarity search. The Signal described LangChain ReAct agents as the intended pattern. `[FACT]`

## Decision

Use a multi-agent ReAct orchestration pattern with a central orchestrator dispatching to specialist agents (lead, opportunity, pricing, follow-up, RAG). Start the pilot with a single generalist agent to de-risk data quality and latency, then introduce specialist agents. `[OPINION]`

## Consequences

- **Positive**: Specialist agents can optimise prompts/tools per domain; reasoning traces improve explainability. `[OPINION]`
- **Negative**: Higher complexity and failure modes; needs orchestration, retries, and observability. `[OPINION]`
- **Risk**: T-2 in risk register. Mitigation: single-agent MVP first. `[FACT]`

## Alternatives Considered

- Single monolithic prompt — rejected due to poor accuracy across diverse domains. `[OPINION]`
- Hard-coded rule engine — rejected due to lack of natural-language flexibility. `[OPINION]`
