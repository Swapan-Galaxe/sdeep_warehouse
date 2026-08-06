---
domain: Salesforce Sales Intelligence Assistant
source: explore/explore-salesforce-sales-intelligence/architecture-context.md
glossary_version: 20260806
validated_by: sdeep
explore_type: Diverge/Converge
evidence_label: OBS
---

# HLD · Salesforce Sales Intelligence Assistant

## 1. Title & Classification

| Field | Value |
|-------|-------|
| **Domain** | Salesforce Sales Intelligence Assistant |
| **Explore Type** | Diverge/Converge |
| **Status** | Approved |
| **Approved** | 20260806 |
| **Version** | 1.0 |
| **Owner** | `sdeep` |
| **Approver** | `sdeep` |
| **Source** | `explore/explore-salesforce-sales-intelligence/architecture-context.md` |

## 2. Abstract

A greenfield AI assistant layer that reads from Salesforce to surface prioritised leads, at-risk opportunities, forecasts, follow-up actions, and similarity search for sales teams. The system uses natural-language queries, multi-agent ReAct-style reasoning, and an optional RAG corpus, all behind a Salesforce OAuth permission model. `[FACT — PRD + architecture-context]`

## 3. Context & Scope

- **In scope**: natural-language query, lead/opportunity prioritisation, risk/health detection, forecasting, advisory pricing guidance, follow-up recommendations, RAG similarity search, explainability, audit. `[FACT — PRD]`
- **Out of scope**: replacing Salesforce, autonomous writes, real-time sync guarantees, final LLM/vector store selection. `[FACT — PRD]`
- **Primary actors**: Sales Rep, Sales Manager, Sales Operations, Revenue Leader. `[FACT — personas]`

## 4. Architecture Approach

- **Pattern**: Modular assistant with bounded contexts, multi-agent orchestration, RAG augmentation. `[OPINION]`
- **Initial implementation**: Single-agent MVP to de-risk data quality and latency; evolve to multi-agent after validation. `[OPINION — risk mitigation]`
- **Reasoning**: ReAct agents allow traceable reasoning and source citations, addressing trust and explainability requirements. `[OPINION]`

## 5. Component Breakdown

| Component | Responsibility | Technology / Pattern | Notes |
|-----------|----------------|----------------------|-------|
| Web/Messaging UI | Natural-language input and result display | Web app or Salesforce Lightning component `[ASSUMPTION]` | Must be keyboard and screen-reader accessible `[FACT — accessibility spec]` |
| API Gateway | Route queries, enforce auth, rate limiting | REST/gRPC `[ASSUMPTION]` | Salesforce OAuth token validation `[ASSUMPTION]` |
| Agent Orchestrator | Dispatch queries to specialist agents | LangChain / ReAct orchestration `[FACT — Signal]` | Start with single-agent for pilot `[OPINION]` |
| Lead Agent | Score and rank leads | ReAct with Salesforce query tools `[OPINION]` | Cites source records `[FACT]` |
| Opportunity Agent | Risk/health detection, forecast, follow-up | ReAct with Salesforce query tools `[OPINION]` | Uses stage, close date, activity `[FACT]` |
| Pricing Agent | Advisory pricing/discount guidance | ReAct + policy rules `[OPINION]` | Hard guardrails; no auto-execution `[FACT]` |
| RAG Retriever | Similar opportunity / conversation search | Vector store + embeddings `[ASSUMPTION]` | Corpus to be validated `[FACT]` |
| Sales Data Access Layer | Read, cache, and permission-filter Salesforce records | Salesforce REST/SOQL API `[ASSUMPTION]` | Enforces user context per query `[FACT]` |
| Vector Store | Embeddings and chunks for RAG | Not selected; options to be validated `[ASSUMPTION]` | Data minimisation review required `[OPINION]` |
| LLM Provider | Reasoning and natural-language generation | Not selected; options to be validated `[ASSUMPTION]` | Latency/cost budget to be defined `[ASSUMPTION]` |
| Audit & Governance | Log queries, records, model version, user actions | Append-only audit store `[OPINION]` | Required for explainability and compliance `[FACT]` |

## 6. Technology Stack

| Layer | Candidate / Decision | Status |
|-------|----------------------|--------|
| Language | Python (agent backend), TypeScript (UI) `[ASSUMPTION]` | Proposed |
| Agent Framework | LangChain ReAct `[FACT]` | Confirmed in Signal |
| LLM | To be selected `[ASSUMPTION]` | Defer to spike |
| Embeddings | To be selected `[ASSUMPTION]` | Defer to spike |
| Vector Store | To be selected `[ASSUMPTION]` | Defer to spike |
| CRM Integration | Salesforce REST / SOQL API `[ASSUMPTION]` | Confirmed assumption |
| Auth | Salesforce OAuth 2.0 Connected App `[ASSUMPTION]` | Proposed |
| Hosting | Containerised services `[ASSUMPTION]` | To be detailed in DevOps strategy |
| CI/CD | Existing pipeline `[ASSUMPTION]` | To be detailed in DevOps strategy |

## 7. Data Architecture

- **System of record**: Salesforce (Leads, Contacts, Accounts, Opportunities, Activities, Tasks). `[FACT]`
- **Derived data**: Insights, recommendations, scores, forecasts — computed at query time or pre-computed for high-frequency views. `[OPINION]`
- **Vector data**: Optional chunks from conversations/documents for RAG; subject to data minimisation and retention policy. `[ASSUMPTION]`
- **Audit data**: Immutable logs of query, retrieved records, model version, generated output, and user action. `[OPINION]`

## 8. Security & Compliance

- Salesforce OAuth token propagated to all data retrieval; no credential storage in assistant. `[ASSUMPTION]`
- Permission filtering by user role, territory, and profile. `[FACT — PRD]`
- No autonomous writes; all actions require explicit user confirmation. `[FACT — PRD]`
- Pricing guidance gated by policy and approval workflow. `[FACT — PRD]`
- Audit logs retained per organisational policy. `[ASSUMPTION]`
- WCAG 2.1 AA target for UI. `[ASSUMPTION]`

## 9. Quality Attributes

| Attribute | Target | How Addressed |
|-----------|--------|---------------|
| Explainability | High | Source citations and confidence scores on every output `[FACT]` |
| Accuracy | High | Clean subset pilot; human-in-the-loop for pricing `[FACT]` |
| Latency | Medium | Streaming responses; pre-computation of common views `[OPINION]` |
| Security | High | OAuth, permission filtering, audit `[FACT]` |
| Scalability | Medium | Single org initially; component boundaries support future multi-tenant `[OPINION]` |
| Maintainability | Medium | Modular agents; single-agent MVP de-risks `[OPINION]` |
| Cost | Medium | Caching and provider selection spike `[OPINION]` |

## 10. Deployment Architecture

- **Pilot**: Containerised services in a sandbox environment with a Salesforce sandbox org. `[OPINION]`
- **Environments**: development, staging, pilot, production. `[OPINION]`
- **Deployment**: CI/CD pipeline with feature flags for experimental features. `[OPINION]`
- **Roll-out**: gated by pilot metrics and compliance sign-off. `[OPINION]`
- Full deployment model to be detailed in `devops-strategy.md`. `[FACT — Step 5 Part 2]`

## 11. Monitoring & Observability

- Query latency, error rate, and token usage per model. `[OPINION]`
- User adoption, query volume, recommendation acceptance. `[OPINION]`
- Audit log completeness and anomaly detection. `[OPINION]`
- Model/output quality metrics (hallucination, citation accuracy). `[OPINION]`
- Full observability model to be detailed in `devops-strategy.md`. `[FACT — Step 5 Part 2]`

## 12. Risks & Assumptions

| ID | Risk / Assumption | Mitigation |
|----|-------------------|------------|
| A1 | Salesforce data quality unknown | Data audit; start with clean subset `[FACT]` |
| A2 | LLM latency/cost unknown | Provider spike; streaming + caching `[OPINION]` |
| A3 | Multi-agent complexity | Start single-agent; add agents after validation `[OPINION]` |
| A4 | RAG corpus availability | Validate sources before building `[FACT]` |
| A5 | User trust | Explainability, citations, pilot usability `[FACT]` |

## 13. Roadmap

| Phase | Focus | Key Deliverables |
|-------|-------|------------------|
| 0 | Spike | LLM/embedding/provider selection; data quality audit `[OPINION]` |
| 1 | MVP | Single-agent natural-language query for top leads and at-risk deals `[OPINION]` |
| 2 | Expand | Forecasting, follow-up recommendations, pricing guardrails `[OPINION]` |
| 3 | Scale | RAG similarity search, multi-agent orchestration, multi-tenant readiness `[OPINION]` |

## 14. Appendices

- **ADRs**: `explore/decisions/salesforce-sales-intelligence-adr-*.md`
- **Domain Model**: `explore/domain/salesforce-sales-intelligence-domain.md`
- **PRD**: `explore/prds/salesforce-sales-intelligence-prd.md`
- **Risk Register**: `explore/explore-salesforce-sales-intelligence/risks.md`
- **Architecture Context**: `explore/explore-salesforce-sales-intelligence/architecture-context.md`

## Enrichment Log

| Date | Session | Changes |
|------|---------|---------|
| 20260806 | Step 5 Part 1 | Drafted HLD from architecture context and PRD. |
