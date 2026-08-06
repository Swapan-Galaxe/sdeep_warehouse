# Problem Capture: SDE-0001

## Problem Statement

The Salesforce Sales Intelligence Assistant has no authenticated Salesforce connection. Without a Connected App and OAuth flow, the assistant cannot read Leads, Contacts, Opportunities, or Activities on behalf of a user. This task establishes the trusted identity and permission model that all later features depend on.

- **Current state**: No Salesforce Connected App exists for the assistant; no OAuth integration is configured.
- **Desired state**: A Connected App is configured in a Salesforce sandbox, OAuth scopes are defined, and the assistant can retrieve a valid access token for a test user.
- **Business driver**: Authentication is a hard prerequisite for lead prioritisation, opportunity risk detection, and every other assistant capability. It also enforces the security and permission-filtering requirements from the PRD.

## Stakeholders

- **Sales Rep**: End user whose Salesforce permissions must be respected.
- **Sales Manager / Revenue Leader**: Needs confidence that data access is scoped and auditable.
- **Salesforce Administrator**: Owns Connected App setup, OAuth policies, and token lifecycles.
- **Security/Compliance**: Requires least-privilege access, no credential storage, and audit logging.
- **Developer**: Implements the data access layer that consumes the token.

## Affected Components

- [x] Server
- [ ] Manager
- [ ] App
- [x] Cross-cutting (security, data access, audit)

## Initial Questions

- [ ] Which Salesforce Connected App type is appropriate (web app, mobile, API-only)?
- [ ] Which OAuth scopes are required for Leads, Contacts, Accounts, Opportunities, and Tasks?
- [ ] Which sandbox org should host the Connected App for development/pilot?
- [ ] What token refresh strategy is supported by the chosen OAuth flow?
- [ ] How are Connected App credentials (client ID/secret) stored and rotated?
- [ ] How will permission filtering be tested across roles/territories?
- [ ] Is the data access layer a backend-only process, or does the browser need a Salesforce token?

## Existing Context

- `explore/prds/salesforce-sales-intelligence-prd.md` — PRD R9: permission-filtered access
- `explore/hlds/salesforce-sales-intelligence-hld.md` — Security & Compliance section
- `explore/decisions/salesforce-sales-intelligence-adr-003-salesforce-oauth.md` — ADR-003
- `explore/epics/salesforce-sales-intelligence-epic-01-salesforce-data-access.md`
