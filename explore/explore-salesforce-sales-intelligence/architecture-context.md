# Architecture Context: Salesforce Sales Intelligence Assistant

## Header

- **Signal**: `signal/signals/20260804-salesforce-sales-intelligence-assistant.md`
- **Explore Bundle**: `explore/explore-salesforce-sales-intelligence/explore-bundle.md`
- **Status**: Active
- **Last Updated**: 20260805
- **Owner**: `sdeep` (Architect)

## Existing System Landscape

- **Salesforce CRM**: System of record for sales data; source of Leads, Contacts, Accounts, Opportunities, Activities, Tasks. `[FACT — from Signal]`
- **Salesforce REST / SOQL API**: Assumed primary integration path. `[ASSUMPTION]`
- **Conversational / RAG data sources**: Not identified in the Signal; to be discovered. `[ASSUMPTION]`
- **No existing AI assistant**: The system described in the Signal is the proposed solution, not a current system. `[FACT — from Signal]`

## Architecture Drivers

| Driver | Priority | Rationale |
|--------|----------|-----------|
| Explainability | High | Sales users must trust AI guidance `[ASSUMPTION]` |
| Accuracy | High | Bad insights damage trust and pipeline decisions `[OPINION]` |
| Latency | Medium | Conversational UX requires responsive answers `[ASSUMPTION]` |
| Security | High | CRM data access must respect permissions `[ASSUMPTION]` |
| Scalability | Medium | Initial single org; future growth possible `[ASSUMPTION]` |
| Maintainability | Medium | Multi-agent architecture must be debuggable `[OPINION]` |
| Cost | Medium | LLM usage can be expensive at scale `[OPINION]` |

## Constraints and Assumptions

- Authentication through Salesforce OAuth / Connected App. `[ASSUMPTION]`
- No direct database writes to Salesforce unless user explicitly approves. `[FACT — from Signal scope]`
- Vector store and LLM provider to be selected during solution design. `[ASSUMPTION]`
- Existing infrastructure (hosting, CI/CD) not described; to be defined. `[ASSUMPTION]`

## Bounded Contexts (Light Domain Model)

| Bounded Context | Responsibility | Key Entities |
|-----------------|----------------|--------------|
| Sales Data Access | Read, cache, and permission-filter Salesforce records | Lead, Contact, Account, Opportunity, Activity, Task |
| Insight Generation | Score, rank, and reason over sales data | Insight, Score, Risk, Forecast |
| Recommendation | Propose next actions with rationale | Recommendation, Action |
| Conversation | Natural-language query handling and response | Query, Response, Trace |
| RAG Search | Semantic search over documents and previous conversations | Document, Embedding, Chunk |
| Governance | Policy enforcement, audit, and explainability | Policy, Audit Log, Approval |

## Context Map

```
+-------------------+     reads      +-------------------+
|  Sales Data Access |<------------->|  Salesforce CRM   |
+-------------------+                +-------------------+
         |                                  |
         | provides data                    |
         v                                  v
+-------------------+     +-------------------+     +-------------------+
| Insight Generation|<--->| Conversation    |<--->| Recommendation    |
+-------------------+     +-------------------+     +-------------------+
         ^                                  |
         |                                  |
         | retrieves                        |
         v                                  v
+-------------------+                +-------------------+
| RAG Search        |                | Governance        |
+-------------------+                +-------------------+
```

## Existing-State HLD (High-Level)

No existing system is being replaced. The proposed assistant will be a new layer above Salesforce. A future HLD will describe the new system in `explore/hlds/salesforce-sales-intelligence-hld.md`.

## Architecture Context Summary

The proposed system is a greenfield AI assistant that reads from Salesforce and optionally from a RAG corpus. The architecture must be secure, explainable, and cost-aware. No legacy architecture needs to be baselined beyond Salesforce itself.

## Enrichment Log

| Date | Session | Changes |
|------|---------|---------|
| 20260805 | Discovery — Part A | Created architecture context from Signal and technical feasibility. |
