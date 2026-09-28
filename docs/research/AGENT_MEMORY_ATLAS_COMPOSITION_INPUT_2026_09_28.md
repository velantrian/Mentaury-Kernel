# Agent Memory Atlas composition input — 2026-09-28

**Status:** `RESEARCH INPUT · NON-CANON · COMPOSITION RELEVANCE ONLY`

Source: https://neoneye.github.io/agent-memory-atlas/

## Scope ownership test

Only cross-domain preservation consequences belong in this repository. Internal memory algorithms, retrieval engines, tombstone schemas and storage choices do not.

## Composition-relevant candidate

A cross-domain correction or rejection can fail if one domain removes or downgrades a value while another derived representation continues to carry the prior meaning as active.

Candidate boundary:

```text
SOURCE CORRECTION
!= AUTOMATIC DERIVED-STATE CORRECTION

REJECTED RECORD
!= GUARANTEE THAT EQUIVALENT VALUE CANNOT RE-ENTER

TRANSPORTED VALUE
!= CURRENTLY ADMISSIBLE VALUE
```

Potential composition requirement to test, not adopt automatically:

> When a downstream domain receives a correction/rejection/supersession signal, the composition path must preserve enough identity, scope and lineage to prevent a semantically equivalent stale value from being silently re-promoted.

## Out of scope here

- retrieval ranking;
- vector/index implementation;
- database tombstone design;
- memory extraction algorithm;
- forced-vs-abstaining retrieval policy inside one owner domain.

Those belong to their owning systems or research labs.

## Promotion boundary

No new invariant is created by this note. Promotion requires a concrete uncovered cross-domain failure plus the existing Scope Ownership / Necessity test.
