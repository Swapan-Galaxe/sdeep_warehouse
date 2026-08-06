# Epic 06: RAG Similarity Search (Conditional)

## Header

- **PRD**: `explore/prds/salesforce-sales-intelligence-prd.md`
- **HLD**: `explore/hlds/salesforce-sales-intelligence-hld.md`
- **ADR**: `explore/decisions/salesforce-sales-intelligence-adr-002-rag-similarity-search.md`
- **Status**: Draft
- **Priority**: Low

## Description

Add semantic search over an approved corpus of conversations and documents to find similar opportunities and previous interactions. This epic is conditional on validating a usable RAG corpus.

## Acceptance Criteria

- A corpus source is identified and approved for processing. `[FACT — ADR-002]`
- Embeddings and vector store are selected and cost/latency validated. `[ASSUMPTION — HLD]`
- User can query for similar closed/won opportunities and conversation excerpts. `[FACT — PRD R7]`
- Data minimisation and retention policies are enforced. `[FACT — compliance]`

## Linked Tasks

- `working/01-pending-planning/DFT-0013.md` — Validate and ingest RAG corpus (conditional)
