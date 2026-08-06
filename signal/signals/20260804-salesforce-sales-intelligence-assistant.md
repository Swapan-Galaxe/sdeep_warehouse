---
date: 20260804
title: "Salesforce AI Sales Intelligence Assistant"
state: Active
source: "sdeep"
type: "Opportunity"
severity: 4
resonance: 4
sponsor: "sdeep"
explore_type: "Diverge-Converge"
---

## The Signal

There is an opportunity to build an AI-powered Salesforce sales intelligence assistant that turns CRM data into prioritized insights, risk alerts, forecasts, and recommended follow-up actions for sales teams. `[ASSUMPTION]`

## Initial Evidence

- The proposed system connects to Salesforce, analyzes leads and opportunities, and supports natural-language questions. `[FACT — source: user-provided use case, 2026-08-04]`
- Target users include sales representatives, sales managers, sales operations teams, and revenue leaders. `[FACT — source: user-provided use case, 2026-08-04]`
- Identified business problems: lead prioritization, at-risk deal detection, pipeline health, follow-up timing, pricing/discount/margin decisions, and similar-opportunity/conversation search. `[FACT — source: user-provided use case, 2026-08-04]`
- Example capabilities include risk detection, lead ranking, weekly focus recommendations, quarterly revenue forecasts, follow-up plan generation, and opportunity similarity search. `[FACT — source: user-provided use case, 2026-08-04]`
- Expected business value: less time searching Salesforce, faster lead response, earlier problem detection, improved follow-up consistency, and better pipeline decisions. `[OPINION — rationale: stated benefits, needs validation]`

## Why This Matters

If validated, an AI sales assistant could reduce time spent retrieving CRM data, improve response speed to leads, surface at-risk deals earlier, and make pipeline decisions more consistent. `[OPINION — rationale: inferred from the business value and problem list described by the user]`

## Actors

| Actor | Role | Impact |
|-------|------|--------|
| sdeep | Sponsor / product owner | Defines direction, priorities, and success criteria |
| Sales representatives | End users | Receive prioritized leads and follow-up recommendations |
| Sales managers | End users | Monitor pipeline health and at-risk deals |
| Sales operations | Enablers / end users | Configure data, processes, and trust metrics |
| Revenue leaders | Decision makers | Use forecasts and risk insights for planning |

## Constraints

- Requires authenticated access to Salesforce and reliable APIs. `[ASSUMPTION]`
- AI-generated insights must be trustworthy and explainable to sales users. `[ASSUMPTION]`
- Must fit into existing sales workflows without adding friction. `[ASSUMPTION]`
- Pricing, forecast, and discount guidance may carry financial and compliance risk. `[ASSUMPTION]`

## Prioritisation

- **Severity**: 4 — The opportunity addresses multiple high-impact sales pain points and could affect pipeline velocity and revenue. `[OPINION — rationale: inferred from breadth of business problems and stated value]`
- **Resonance**: 4 — A clear set of target users (reps, managers, ops, revenue leaders) is identified and likely to benefit. `[OPINION — rationale: inferred from target user breadth and described use cases]`
- **Urgency**: 3 — The idea has momentum (it was raised and described in detail today). `[OPINION — rationale: inferred from user initiative and level of detail]`
- **Position**: `next` — Validate problem/solution fit through Explore before committing to build. `[OPINION — rationale: new product opportunity with broad scope and unvalidated assumptions]`

## Strategic Alignment

- North Star link: improve sales team productivity and revenue predictability. `[ASSUMPTION]`
- Market context: AI sales assistants are an emerging category; integration depth with Salesforce is a likely differentiator. `[ASSUMPTION]`
- Regulatory: no specific external regulatory trigger is known; financial guidance must comply with internal policy. `[ASSUMPTION]`
- Sponsor appetite: `sdeep` is actively sponsoring this and provided a detailed use case. `[FACT — source: user, 2026-08-04]`

## Readiness & Feasibility

- **Technical feasibility**: feasible — Salesforce REST APIs and LangChain ReAct agents are available, but multi-agent orchestration is non-trivial. `[OPINION — rationale: based on described architecture and common tooling]`
- **Data feasibility**: partial — requires clean Salesforce data and embeddings/RAG corpus; data quality is an unknown. `[ASSUMPTION]`
- **Organisational readiness**: partial — adoption depends on sales team trust and workflow fit. `[ASSUMPTION]`
- **Risk of inaction**: delay means continued manual pipeline management and potentially missed revenue opportunities. `[OPINION — rationale: inferred from stated business problems]`

## Explore Type

- **Recommended**: `Diverge-Converge` — the opportunity is broad, targets multiple user groups, and needs both ideation and convergence. `[OPINION — rationale: multiple user types, broad feature surface, and unclear exact solution shape]`

## Completion Criteria Status

- [x] 1. Fundamentals — Complete (no duplicate active Signals found; title, type, source, sponsor set)
- [x] 2. Evidence & Context — Complete (primary source captured; corroborating data deferred to validation)
- [x] 3. Framing & Meaning — Complete (scope, actors, constraints, and outcomes documented)
- [x] 4. Strategic Alignment — Complete (North Star, market, regulatory, and sponsor appetite noted)
- [x] 5. Readiness & Feasibility — Complete (technical/data feasibility, organisational readiness, and risk of inaction assessed)
- [x] 6. Prioritisation — Complete (severity, resonance, urgency, position, and rationale captured)
- [x] 7. Explore Type — Complete (`Diverge-Converge` selected with rationale)

## Signal Summary

| Field | Content |
|-------|---------|
| Problem | Sales teams spend too much time searching Salesforce and lack timely, prioritized insights to act on leads and opportunities. `[OPINION — rationale: synthesis of stated business problems]` |
| Hypothesis | An AI-powered assistant integrated with Salesforce can surface prioritized leads, at-risk deals, forecasts, and follow-up actions, improving productivity and pipeline decisions. `[ASSUMPTION]` |
| Confidence | Medium `[OPINION — rationale: detailed use case but no corroborating data or validation]` |
| Key Evidence | 1. Use case identifies six business problems and target users `[FACT]` 2. Example questions define expected capabilities `[FACT]` 3. Stated business value includes time savings and better decisions `[OPINION]` |
| Critical Assumptions | 1. Salesforce data quality and API access will support reliable AI insights `[ASSUMPTION]` 2. Sales users will trust and act on AI-generated guidance `[ASSUMPTION]` 3. The feature scope can be narrowed to a viable first slice `[ASSUMPTION]` |
| Actors | sdeep (sponsor), sales reps, sales managers, sales ops, revenue leaders |
| Constraints | Salesforce API access, AI trust/explainability, workflow fit, financial guidance risk |
| Importance / Urgency | Severity 4, Resonance 4, Urgency 3, Position: next |
| Explore Type | Diverge-Converge |
| Sponsor | sdeep (appetite: High `[OPINION — rationale: sponsor provided detailed use case and is actively pursuing]`) |

## Routing Decision

- **Decision**: Route to Explore
- **Rationale**: The Signal is well-framed, targets a clear set of users, and represents a broad product opportunity with many unvalidated assumptions. Explore (Diverge-Converge) is the right phase to shape the problem and converge on a viable first slice.
- **Approver**: `sdeep`
- **Date**: 20260804
- **Suggested activities**: Validate problem intensity with target users; define the smallest viable first slice; assess Salesforce data quality and API constraints.
- **Timeline expectation**: To be set during Explore planning.

### Route-Readiness Verification

| Criterion | Status | Notes |
|-----------|--------|-------|
| Signal Fundamentals | Pass | Type, importance, source, and sponsor documented; no duplicates found |
| Evidence and Context | Pass | Primary source captured; all claims tagged; corroborating data deferred to validation |
| Framing and Meaning | Pass | Scope, actors, constraints, and expected outcomes documented |
| Strategic and Market Alignment | Pass | North Star, market, regulatory, and sponsor appetite noted |
| Readiness and Feasibility | Pass | Technical, data, organisational readiness, urgency, and risk of inaction assessed |
| Prioritisation and Positioning | Pass | Severity, resonance, urgency, and position set with rationale |
| Explore Type Recommendation | Pass | `Diverge-Converge` selected with rationale |

**Confidence**: Medium

## Completion Notes

| Date | Session | Changes |
|------|---------|---------|
| 20260804 | Initial capture | Created from user-provided use case; sponsor confirmed as `sdeep`; severity/resonance initial values set; all claims tagged; explore_type deferred to routing step. |
| 20260804 | Signal strengthen | Added strategic alignment, readiness/feasibility, urgency, position, explore type, and Signal Summary; all claims tagged; all completion criteria marked complete. |
| 20260804 | Signal route | Routed to Explore (Diverge-Converge); approver `sdeep`; all route-readiness criteria passed; Signal remains Active. |
