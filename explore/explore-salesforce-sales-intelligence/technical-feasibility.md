# Technical Feasibility: Salesforce Sales Intelligence Assistant

## Header

- **Signal**: `signal/signals/20260804-salesforce-sales-intelligence-assistant.md`
- **Explore Bundle**: `explore/explore-salesforce-sales-intelligence/explore-bundle.md`
- **Status**: Active
- **Last Updated**: 20260805
- **Owner**: `sdeep` (Architect / Lead Engineer)

## System Context

| Platform / Layer | Current Role | Notes |
|------------------|--------------|-------|
| Salesforce CRM | System of record for leads, opportunities, contacts, accounts, activities, tasks | REST/SOQL API assumed available `[ASSUMPTION]` |
| LangChain | Agent orchestration and ReAct agent framework | Described in Signal `[FACT]` |
| LLM Provider | Natural language reasoning and response generation | Not selected; options and constraints to be validated `[ASSUMPTION]` |
| Vector Store | Embeddings storage for RAG / similarity search | Not selected; to be validated `[ASSUMPTION]` |
| Web UI / Messaging | User interaction surface | To be designed in Step 4 |

## Data Realities

| Data Source | Availability | Quality | Latency | Ownership | Gaps |
|-------------|--------------|---------|---------|-----------|------|
| Leads | Salesforce | Unknown | API/query dependent | Sales Operations | Authoritative object confirmed by user; field coverage and completeness unknown |
| Opportunities | Salesforce | Unknown | API/query dependent | Sales Operations | Authoritative object confirmed by user; stage/probability standardisation unknown |
| Activities | Salesforce | Unknown | API/query dependent | Sales Reps (input) | Recording habits inconsistent `[ASSUMPTION]` |
| Tasks | Salesforce | Unknown | API/query dependent | Sales Reps | Due-date and priority discipline unknown |
| Conversations / Documents | External source (TBD) | Unknown | TBD | TBD | Source not identified in Signal |

## Technical Constraints

| Constraint | Source | Implication |
|------------|--------|-------------|
| Salesforce API rate limits | `[ASSUMPTION]` | Caching or batching may be required for large orgs |
| Salesforce object/field permissions | `[ASSUMPTION]` | Ingestion must respect user and profile permissions |
| LLM output latency for conversational UX | `[ASSUMPTION]` | Streaming responses or async pre-computation may be needed |
| Hallucination and explainability | Signal `[ASSUMPTION]` | Outputs must cite records; guardrails needed for pricing |
| Multi-tenancy / data isolation | `[ASSUMPTION]` | Single org for now; design should not preclude expansion |
| No autonomous write actions | Scope decision | Recommendations are read-only until user approves |

## Technical Opportunities

- Use existing Salesforce data without building a new CRM. `[FACT — from Signal]`
- Multi-agent orchestration can split reasoning by domain (leads, opportunities, pricing, follow-up). `[OPINION — rationale: from Signal architecture]`
- RAG can surface similar opportunities and previous conversations. `[FACT — from Signal]`
- Agent reasoning traces can provide explainability. `[OPINION]`
- Caching and pre-computation can improve perceived latency for common queries. `[OPINION]`

## Technical Risks and Unknowns

| ID | Risk | Impact | Likelihood | Mitigation |
|----|------|--------|------------|------------|
| T-1 | Salesforce data is too dirty for reliable AI insights | High | Medium | Data quality assessment; start with a clean subset |
| T-2 | Multi-agent orchestration adds complexity and failure modes | High | Medium | Begin with a single-agent MVP |
| T-3 | LLM latency or cost exceeds conversational UX budget | High | Medium | Benchmark candidates; consider streaming and caching |
| T-4 | RAG corpus does not exist or is not accessible | Medium | Medium | Validate conversation/document sources early |
| T-5 | Permission model leaks data across users/teams | High | Low | Enforce Salesforce user-context in all queries |

## Design Constraints and Guardrails

- All AI outputs must cite source Salesforce records. `[OPINION]`
- User context (role, territory, permissions) must filter all data retrieval. `[OPINION]`
- Pricing/discount guidance is advisory; no auto-write. `[FACT — from Signal constraints]`
- Conversational interface should expose confidence and allow follow-up questions. `[OPINION]`

## Questions for Engineering

1. Which fields within Lead and Opportunity are authoritative for scoring, risk, and forecast calculations?
2. What is the existing API and authentication setup (connected app, OAuth scopes)?
3. What LLM and embedding models are approved, and what are the latency/cost limits?
4. Is there an existing conversation/document corpus for RAG?
5. What caching or pre-computation infrastructure is available?
6. What is the target query response time for a conversational interaction?

## Enrichment Log

| Date | Session | Changes |
|------|---------|---------|
| 20260805 | Discovery — Part A | Created technical feasibility baseline from Signal. |
| 20260806 | User input | Confirmed Lead and Opportunity as authoritative Salesforce objects. |
