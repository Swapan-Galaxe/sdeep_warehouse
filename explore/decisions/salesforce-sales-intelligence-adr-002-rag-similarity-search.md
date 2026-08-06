# ADR-002: RAG for Similar Opportunity and Conversation Search

## Status

Accepted (conditional on corpus validation)

## Context

The Signal includes "similar opportunity and conversation search" as a capability, which requires semantic search over unstructured text. `[FACT]`

## Decision

Use Retrieval-Augmented Generation (RAG) over an embeddings-backed vector store to support similarity search, if and only if a usable corpus of conversations or documents is identified and approved for processing. `[OPINION]`

## Consequences

- **Positive**: Reps can discover similar closed/won deals and relevant conversation snippets. `[OPINION]`
- **Negative**: Adds vector store, embedding pipeline, and data-retention governance. `[FACT]`
- **Risk**: T-4 in risk register. Mitigation: validate corpus before building. `[FACT]`

## Alternatives Considered

- Keyword-only search — rejected as insufficient for semantic similarity. `[OPINION]`
- No similarity search — deferred to later phase to reduce first-slice scope. `[OPINION]`
