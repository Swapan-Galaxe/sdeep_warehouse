# ADR-004: Policy Guardrails for Pricing and Discount Guidance

## Status

Accepted

## Context

Pricing, discount, and margin guidance carries financial and compliance risk if AI outputs are mistaken for approvals. `[FACT]`

## Decision

All pricing and discount guidance is advisory only. The system enforces hard guardrails against recommending actions that violate company policy and requires human approval before any discount is applied. `[FACT]`

## Consequences

- **Positive**: Reduces compliance and revenue risk; aligns with PRD constraints. `[FACT]`
- **Negative**: May slow down discount-heavy workflows; UX must clearly label advisory nature. `[OPINION]`
- **Risk**: CR-1 in risk register. Mitigation: policy rules, human-in-the-loop, audit logs. `[FACT]`

## Alternatives Considered

- AI-generated discount approvals — rejected due to unacceptable compliance risk. `[FACT]`
