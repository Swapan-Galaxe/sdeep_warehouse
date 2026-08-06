# Epic 01: Salesforce Data Access

## Header

- **PRD**: `explore/prds/salesforce-sales-intelligence-prd.md`
- **HLD**: `explore/hlds/salesforce-sales-intelligence-hld.md`
- **ADR**: `explore/decisions/salesforce-sales-intelligence-adr-003-salesforce-oauth.md`
- **Status**: Draft
- **Priority**: High

## Description

Build the authenticated, permission-filtered Salesforce data access layer so the assistant can read Leads, Contacts, Accounts, Opportunities, Activities, and Tasks without exposing unauthorised data.

## Acceptance Criteria

- OAuth Connected App is configured and can authenticate a Salesforce user. `[FACT — PRD]`
- All data queries filter by the authenticated user's Salesforce permissions and territory. `[FACT — PRD]`
- No writes to Salesforce are performed by the assistant. `[FACT — PRD]`
- Rate limits and API errors are handled gracefully. `[FACT — technical-feasibility]`

## Linked Tasks

- `working/01-pending-planning/DFT-0001.md` — Set up Salesforce Connected App and OAuth
- `working/01-pending-planning/DFT-0002.md` — Build permission-filtered data access layer
