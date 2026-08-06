---
domain: Salesforce Sales Intelligence Assistant
source: explore/explore-salesforce-sales-intelligence/domain-analysis.md
glossary_version: 20260805
validated_by: sdeep
explore_type: Diverge/Converge
evidence_label: OBS
---

# PRD · Salesforce Sales Intelligence Assistant

## Header

- **Status**: Approved
- **Signal**: `signal/signals/20260804-salesforce-sales-intelligence-assistant.md`
- **Explore Bundle**: `explore/explore-salesforce-sales-intelligence/explore-bundle.md`
- **Last Updated**: 20260806
- **Owner**: `sdeep`
- **Approved**: 20260806

## Group 1: Product Definition

### Links

- Signal · Hypothesis · Personas · Journey Map · Context · Risk Register

### Priority & Stakeholder Appetite

- **Priority**: High (Signal severity 4)
- **Stakeholder appetite**: High (Signal resonance 4)

### Problem Statement

Sales teams lose productive selling time navigating Salesforce and synthesising scattered lead, opportunity, and activity data into actionable priorities. The problem is not a lack of data, but a lack of timely, contextual, and trustworthy interpretation that tells each seller what to do next. `[FACT — context.md]`

### Goals

1. Reduce time sales reps spend searching Salesforce for answers. `[OPINION — inferred from Signal]`
2. Surface at-risk deals earlier than current manual review. `[OPINION — inferred from Signal]`
3. Provide consistent, policy-controlled guidance for pricing, discount, and margin. `[FACT — regulatory-compliance.md]`
4. Improve pipeline decision quality and forecast confidence. `[OPINION — inferred from Signal]`

### Success Metrics

| Metric | Target | Measurement Method |
|--------|--------|--------------------|
| Adoption | ≥ 60% of pilot reps use the assistant ≥ 3 times/day within 4 weeks | Analytics on daily active users and query counts `[OPINION — target to calibrate]` |
| Efficiency | ≥ 30% reduction in time spent searching Salesforce for answers | User-reported time diary or in-app feedback survey `[OPINION — target to calibrate]` |
| Action | ≥ 50% of assistant recommendations accepted or edited | Track recommendation interactions and outcomes `[OPINION — target to calibrate]` |
| Trust | ≤ 10% of recommendations manually double-checked against source records | Observation or self-report during pilot `[OPINION — target to calibrate]` |

### Target Users

| Persona | Role | Primary Need |
|---------|------|--------------|
| Jordan | Sales Representative | Prioritised leads and recommended next actions `[FACT]` |
| Priya | Sales Manager | Pipeline health and at-risk deals `[FACT]` |
| Alex | Sales Operations | Data quality transparency and trust metrics `[FACT]` |
| Samir | Revenue Leader | Forecast confidence and risk drivers `[FACT]` |

## Group 2: Technical Specification

### Requirements

| # | Requirement | Acceptance Criteria | Priority |
|---|-------------|---------------------|----------|
| R1 | Natural-language query interface | User can type a sales question; system returns a natural-language answer with cited records | Must |
| R2 | Lead prioritisation | System ranks user's open Leads by score, activity recency, and conversion signals | Must |
| R3 | Opportunity risk / health detection | System flags opportunities with stale close dates, low activity, or stage-probability mismatches | Must |
| R4 | Pipeline forecasting | System projects revenue by period with confidence range, labelled as a projection | Should |
| R5 | Pricing / discount / margin guidance | System provides advisory guidance that references policy and requires human approval for execution | Should |
| R6 | Follow-up action recommendations | System suggests next action, owner, and due date for each opportunity/lead | Should |
| R7 | Similar opportunity / conversation search (RAG) | User can query for similar closed/won opportunities and conversation excerpts, if corpus exists | Could |
| R8 | Explainability and source citations | Every insight displays the Salesforce records used and a confidence level | Must |
| R9 | Permission-filtered data access | All queries filter by the authenticated user's Salesforce permissions and territory | Must |
| R10 | Audit logging | Each query records user, retrieved records, model version, generated insight, and user action | Should |
| R11 | No autonomous writes | The system never modifies Salesforce data without explicit user confirmation | Must |
| R12 | Human-in-the-loop for pricing actions | Pricing/discount recommendations cannot be executed directly; approval workflow required | Must |

### Constraints

| Constraint | Source |
|------------|--------|
| Salesforce API rate limits and object/field permissions | Technical Feasibility `[ASSUMPTION]` |
| Lead and Opportunity are authoritative objects; field coverage/quality unknown | User input + Technical Feasibility `[FACT]` |
| LLM output latency and cost must fit conversational UX budget | Technical Feasibility `[ASSUMPTION]` |
| Hallucination risk on pricing/forecast guidance; requires guardrails | Signal + Compliance `[ASSUMPTION]` |
| Pricing guidance is advisory only and policy-controlled | Signal scope `[FACT]` |
| Accessibility target: WCAG 2.1 AA | Compliance `[ASSUMPTION]` |
| RAG corpus availability and content permissions not validated | Technical Feasibility `[ASSUMPTION]` |

### Out of Scope

- Replacing Salesforce as the system of record `[FACT — context.md]`
- Autonomous actions that modify Salesforce data without human approval `[FACT — context.md]`
- Real-time CRM sync performance guarantees (to be validated in Step 5) `[FACT — context.md]`
- Final LLM, embedding model, and vector store selection (to be decided in Step 5) `[ASSUMPTION]`
- Compliance-specific legal sign-off (to be escalated to Compliance Lead) `[FACT — context.md]`

### Technical Notes

- **Architecture**: greenfield assistant layer above Salesforce; bounded contexts include Sales Data Access, Insight Generation, Recommendation, Conversation, RAG Search, and Governance `[FACT — architecture-context.md]`.
- **Integration**: Salesforce REST/SOQL API via OAuth Connected App; user context and permissions must propagate to all queries `[ASSUMPTION]`.
- **Data realities**: Lead, Opportunity, Activity, Task data quality is unknown; start with a clean subset for pilot `[FACT — technical-feasibility.md]`.
- **AI approach**: multi-agent orchestration (lead, opportunity, risk, pricing, follow-up) with ReAct-style reasoning; begin with a single-agent MVP to de-risk `[OPINION — technical-feasibility.md]`.
- **Explainability**: reasoning traces and record citations required for trust; confidence scores displayed with every recommendation `[OPINION — technical-feasibility.md]`.
- **Security**: no persistent personal data beyond query/response state; RAG content must be reviewed for sensitive data retention `[OPINION — regulatory-compliance.md]`.

## Group 3: Quality Definition

### Non-Functional Requirements

| Area | Requirement | Target |
|------|-------------|--------|
| Performance | Conversational query response time | p95 < 3 seconds for simple queries; streaming responses allowed for complex reasoning `[OPINION — target to validate]` |
| Security | Salesforce OAuth 2.0 with user-scoped permissions; no credential storage in the assistant `[ASSUMPTION]` |
| Availability | Pilot availability target | 99.5% during business hours `[OPINION — to be validated]` |
| Scalability | Single Salesforce org pilot; architecture must not preclude multi-tenant expansion `[ASSUMPTION]` |
| Accessibility | WCAG 2.1 AA conformance for web UI; keyboard-navigable, screen-reader friendly `[ASSUMPTION]` |
| Observability | Audit logs and model/retrieval traces captured per query `[OPINION — required for explainability]` |

### Quality Gates

**Definition of Ready (DoR)**
- Requirement maps to a validated Signal or discovery artifact `[FACT]`
- Acceptance criteria are measurable and testable `[OPINION]`
- No unresolved external dependency blocks implementation `[OPINION]`
- Data source and Salesforce object/field assumptions are documented `[FACT]`

**Definition of Done (DoD)**
- Feature implemented behind a feature flag if experimental `[OPINION]`
- Unit and integration tests pass; AI outputs pass accuracy/explainability benchmarks `[OPINION]`
- Source citations and confidence scores visible for all insights `[FACT — from compliance]`
- Security and accessibility review completed for user-facing changes `[ASSUMPTION]`
- PRD acceptance criteria verified in a pilot environment `[OPINION]`

### Testing Strategy

- **Unit tests** for scoring, ranking, and policy-check logic `[OPINION]`
- **Integration tests** for Salesforce data access, permission filtering, and agent orchestration `[FACT]`
- **E2E tests** for core user flows: ask question, view prioritised leads, accept recommendation `[OPINION]`
- **AI quality benchmarks** for hallucination, citation accuracy, and policy compliance before production `[OPINION]`
- Full test strategy produced in Step 5 `[FACT — Step 4 spec]`

### DevOps & Deployment Strategy

- **Environments**: pilot/staging connected to a sandbox Salesforce org; production roll-out gated by pilot metrics `[OPINION]`
- **Deployment**: containerised services behind existing CI/CD; model/provider versions pinned and auditable `[OPINION]`
- **Monitoring**: query latency, error rate, user adoption, recommendation acceptance, and audit log completeness `[OPINION]`
- Full DevOps strategy produced in Step 5 `[FACT — Step 4 spec]`

## Group 4: Specification Completion

### Open Questions

| # | Question | Owner | Priority | Target Resolution |
|---|----------|-------|----------|-------------------|
| Q1 | Which Lead and Opportunity fields are authoritative for scoring, risk, and forecast? | Lead Engineer / Sales Operations | High | Before first data ingest `[FACT — explore bundle]` |
| Q2 | What is the smallest viable first slice that still delivers measurable value to one user group? | Product Manager | High | Before PRD approval `[FACT — explore bundle]` |
| Q3 | How must pricing, discount, and margin guidance be governed to avoid compliance risk? | Compliance Lead | High | Before release `[FACT — explore bundle]` |
| Q4 | What is the current quality and accessibility of Salesforce data for AI consumption? | Lead Engineer | High | Before pilot `[FACT — explore bundle]` |
| Q5 | Which LLM and embedding models are approved, and what is the budget for inference? | Architect / Finance | High | Before Step 5 architecture `[FACT — explore bundle]` |
| Q6 | Will sales users trust AI-generated recommendations without human review? | Product Manager | Medium | Pilot usability validation `[FACT — explore bundle]` |

### Dependencies

| Dependency | Type | Risk if Unavailable |
|------------|------|---------------------|
| Salesforce Connected App and OAuth scopes | External | No data access; project blocked `[ASSUMPTION]` |
| Clean subset of Lead/Opportunity data | Internal | Pilot insights unreliable `[ASSUMPTION]` |
| Approved LLM and embedding provider | External | No reasoning/search capability `[ASSUMPTION]` |
| Compliance Lead assignment and pricing policy | Internal | Financial guidance cannot be released `[FACT — regulatory-compliance.md]` |
| Pilot user cohort (sales reps) | Internal | No adoption validation `[ASSUMPTION]` |

### Assumptions

| # | Assumption | Risk if Wrong | Validation Plan |
|---|------------|---------------|-----------------|
| A1 | Salesforce data is accessible and sufficiently clean for reliable AI insights | Recommendations inaccurate or misleading; low adoption | Data quality audit on Leads and Opportunities before pilot `[FACT]` |
| A2 | Sales users will trust AI-generated guidance if source records and confidence are shown | Low adoption; wasted investment | Pilot usability testing with 3–5 reps; measure trust signals `[OPINION]` |
| A3 | A first slice can be narrowed to one high-frequency use case | Scope creep or failed delivery | Converge on top-priority leads or at-risk deals in PRD/Step 5 `[OPINION]` |
| A4 | Multi-agent orchestration with ReAct is technically feasible | Integration or performance blockers | Build single-agent MVP; benchmark latency/cost `[OPINION]` |
| A5 | Pricing/discount guidance can be governed through policy and human oversight | Compliance or revenue risk | Lock policy rules before launch; require approval for execution `[FACT]` |

## Enrichment Log

| Date | Session | Changes |
|------|---------|---------|
| 20260806 | PRD Group 1 | Approved product definition. |
| 20260806 | PRD Group 2 | Approved technical specification. |
| 20260806 | PRD Group 3 | Approved quality definition. |
| 20260806 | PRD Group 4 | Approved open questions, dependencies, and assumptions. |
| 20260806 | PRD-4 approval | Wrote approved PRD to disk. |
