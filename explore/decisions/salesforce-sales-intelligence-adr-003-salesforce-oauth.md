# ADR-003: Salesforce OAuth for Authentication and Permissions

## Status

Accepted

## Context

Salesforce is the system of record for all CRM data. The assistant must not expose records a user is not authorised to see. `[FACT]`

## Decision

Authenticate users through a Salesforce Connected App using OAuth 2.0 and propagate the user's Salesforce permissions and territory context to every data query. `[OPINION]`

## Consequences

- **Positive**: Reuses existing identity and authorisation model; no separate user store. `[OPINION]`
- **Negative**: All backend queries must run under the authenticated user's context, complicating caching and pre-computation. `[OPINION]`
- **Risk**: T-5 in risk register. Mitigation: enforce user context in all queries; audit access. `[FACT]`

## Alternatives Considered

- Service account with broad read access — rejected due to permission-leak risk. `[FACT]`
