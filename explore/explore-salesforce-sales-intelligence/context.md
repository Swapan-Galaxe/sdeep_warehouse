# Context: Salesforce Sales Intelligence Assistant

## Header

- **Signal**: `signal/signals/20260804-salesforce-sales-intelligence-assistant.md`
- **Explore Bundle**: `explore/explore-salesforce-sales-intelligence/explore-bundle.md`
- **Status**: Active
- **Last Updated**: 20260805
- **Owner**: `sdeep`

## Problem Statement

Sales teams lose productive selling time navigating Salesforce and synthesising scattered lead, opportunity, and activity data into actionable priorities. The problem is not a lack of data, but a lack of timely, contextual, and trustworthy interpretation that tells each seller what to do next.

## Scope

### In Scope

- Natural-language query interface for sales questions
- Lead prioritisation and ranking
- Opportunity risk, health, and stall detection
- Pipeline forecasting and revenue projections
- Pricing, discount, and margin guidance (policy-controlled)
- Follow-up action recommendations
- Similar opportunity and conversation search (RAG)
- Multi-agent orchestration behind a single interaction surface
- Salesforce integration as the primary data source

### Out of Scope (for this Explore)

- Replacing Salesforce as the system of record
- Autonomous actions that modify Salesforce data without human approval
- Real-time CRM sync performance guarantees (to be validated in Step 5)
- Compliance-specific legal sign-off (to be escalated to Compliance Lead)

## Domain Model

| Entity | Description | Key Attributes | Relationships |
|--------|-------------|----------------|---------------|
| Lead | Unqualified sales prospect | Source, score, status, owner, last activity | Owned by Sales Rep; may convert to Contact/Opportunity |
| Contact | Person associated with an account | Role, engagement history, email | Belongs to Account; linked to Opportunities |
| Account | Customer or prospect organisation | Industry, tier, region, annual revenue | Has Contacts and Opportunities |
| Opportunity | Potential revenue deal | Stage, amount, close date, probability, owner | Owned by Sales Rep; linked to Account, Contacts, Activities |
| Activity | Sales touchpoint (call, email, meeting) | Type, date, outcome, notes | Linked to Lead, Contact, or Opportunity |
| Task | Planned follow-up action | Due date, priority, status, assigned to | Linked to Opportunity or Contact |
| Forecast | Projected revenue for a period | Period, category, amount, confidence | Aggregated from Opportunities |
| Insight | AI-generated prioritisation or risk output | Type, confidence, evidence, recommendation | Generated from Opportunity/Lead/Account data |
| Recommendation | Suggested next action | Action, rationale, priority, owner | Proposed for a user and an opportunity |
| User | Sales team member | Role, permissions, territory | Asks questions; receives Insights and Recommendations |

## System Map

| Component | Role | Integrates With |
|-----------|------|-----------------|
| Salesforce REST API | System of record for CRM data | Lead, Contact, Account, Opportunity, Activity, Task objects |
| Data Ingestion Service | Extracts and normalises Salesforce data | Salesforce REST API, data lake/vector store |
| Vector Store | Stores embeddings for semantic search and RAG | Ingestion service, RAG retriever |
| Agent Orchestrator | Routes user questions to specialist agents | ReAct agents, RAG retriever, Salesforce API |
| ReAct Agents | Specialist reasoning agents for leads, opportunities, risks, pricing, follow-up | Orchestrator, Salesforce data, LLM |
| LLM Provider | Generates natural-language responses and reasoning traces | ReAct agents, guardrails |
| Guardrails & Policy Layer | Enforces explainability and compliance controls | Pricing/recommendation outputs |
| Web/Messaging UI | Natural-language query and results interface | Agent orchestrator |

## Technical Constraints

| Constraint | Source | Status |
|------------|--------|--------|
| Salesforce API rate limits and object permissions | Signal + `[ASSUMPTION]` | Assumed |
| Data quality of existing Salesforce records is unknown | Signal | Open question |
| LLM hallucination risk on financial/pricing guidance | Signal | Assumed |
| Need for human oversight before any write action | Scope decision | Confirmed |
| Latency targets for conversational queries not yet defined | Gap | Open question |

## Stakeholder Map & RACI

| Stakeholder | Role | R | A | C | I |
|-------------|------|---|---|---|---|
| sdeep | Product Manager / Sponsor | C | A | R | I |
| Sales Representatives | Primary end users | R | C | C | I |
| Sales Managers | Managers / end users | C | C | R | I |
| Sales Operations | Data / process enablers | R | C | C | I |
| Revenue Leaders | Decision makers / approvers | I | A | C | C |
| Architect | Technical strategy | R | A | C | C |
| Lead Engineer | Implementation feasibility | R | C | A | C |

## Governance Framework

- **Product decisions**: `sdeep` owns scope and priority; Revenue Leaders approve changes to forecast/pricing guidance policy.
- **Technical decisions**: Architect owns architecture and non-functional constraints; Lead Engineer owns feasibility and build constraints.
- **Data decisions**: Sales Operations owns Salesforce data quality and field definitions.
- **Compliance decisions**: To be assigned to a Compliance Lead once identified.

## Assumptions Catalogue

| Assumption | Source | Open Question | Risk if Wrong | Owner |
|------------|--------|---------------|---------------|-------|
| Salesforce data is accessible and sufficiently clean for AI analysis | Signal `[ASSUMPTION]` | What is the current data quality and field coverage? | Insights may be unreliable | Lead Engineer |
| Sales users will trust AI-generated guidance with explainability | Signal `[ASSUMPTION]` | What level of explanation and human oversight is required? | Low adoption | Product Manager |
| The feature scope can be narrowed to a viable first slice | Signal `[ASSUMPTION]` | What is the smallest valuable first slice? | Scope creep / missed timeline | Product Manager |
| Multi-agent orchestration with LangChain ReAct is technically feasible | Signal `[ASSUMPTION]` | Which LLM and agent patterns fit the latency/quality needs? | Integration failure or poor UX | Architect |
| Pricing/discount guidance can be governed through policy | Signal `[ASSUMPTION]` | What are the exact policy and approval boundaries? | Compliance or revenue risk | Compliance Lead |

## Gaps for Part B

| Gap | Why It Matters | Closes In |
|-----|---------------|-----------|
| Actual user workflows and pain points | Personas and journeys must be grounded in real behaviour | Personas, Journey Mapping |
| Stated vs observed priority of use cases | Need to validate which questions are asked most often | Market Research, Personas |
| Trust and explainability expectations | Determines guardrail and UI design | Personas, Journey Mapping |
| Salesforce org-specific data model | User confirmed Lead and Opportunity are authoritative objects; custom fields and data quality still to validate | Domain Analysis, Technical Feasibility |

## Enrichment Log

| Date | Session | Changes |
|------|---------|---------|
| 20260805 | Discovery — Part A | Created context baseline from Signal and Explore Bundle. |
| 20260806 | User input — Part A gaps | Confirmed Lead and Opportunity as authoritative objects; no AI tools currently in use. |
