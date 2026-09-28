# Agent Memory Atlas composition input — 2026-09-28

**Status:** `RESEARCH INPUT · NON-CANON · COMPOSITION RELEVANCE ONLY · NO_NEW_INVARIANT · NO_RUNTIME_CHANGE`

Source: https://neoneye.github.io/agent-memory-atlas/

## Scope ownership test

Only cross-domain preservation consequences belong in this repository. Internal memory algorithms, retrieval engines, tombstone schemas, matching/normalization policies and storage choices do not.

This is not the first Agent Memory Atlas intake in the Velantrim ecosystem: prior Atlas-related / pre-existing overlapping coverage exists in 💠 Crystal (`docs/research/MEMORY_EVAL_ADVERSARIAL_PROFILE_V0.md`, [PR #462](https://github.com/velantrian/velantrim-exocortex-crystal/pull/462)) and 🧬 Native Kernel (`docs/research/MEMORY_EVALUATION_PROTOCOL_V0.md`). This note records only the cross-domain residual after checking existing composition coverage.

## Source-fidelity note

Agent Memory Atlas's rejected-value mechanism keys a rejected value under a declared identity/normalization policy (for example scope + subject + predicate + normalized value).

```text
DECLARED NORMALIZED VALUE MATCH != ARBITRARY SEMANTIC PARAPHRASE MATCH
```

The source does not establish general semantic-equivalence blocking. Any paraphrase-matching question is an open, owner-local policy / separate test question and is not assumed here.

## Composition-relevant candidate

A cross-domain correction or rejection can fail if one domain removes or downgrades a value while another derived representation continues to carry the prior meaning as active.

Candidate boundary (descriptive, not a new invariant):

```text
SOURCE CORRECTION
!= AUTOMATIC DERIVED-STATE CORRECTION

REJECTED RECORD
!= GUARANTEE THAT A VALUE MATCHING UNDER THE TARGET DOMAIN'S DECLARED IDENTITY POLICY CANNOT RE-ENTER

TRANSPORTED VALUE
!= CURRENTLY ADMISSIBLE VALUE
```

## Existing composition coverage

The primary check is against current composition invariants and scenarios, not against the spec-reconciliation rule `SOURCE UPDATE ≠ AUTOMATIC COMPOSITION UPDATE` (that rule governs reconciliation of the Mentaury-Kernel spec with its source documents, not runtime data flow).

| Existing coverage | Where | Relevance to this donor candidate |
|---|---|---|
| CI-04 Admission Isolation | [`docs/COMPOSITION_INVARIANTS.md §4`](../COMPOSITION_INVARIANTS.md#4-admission-isolation) | delivery / structural validity / receipts remain distinct from semantic admission — a transported value is not admitted merely by crossing the boundary |
| CI-06 Revision Accountability | [`§6`](../COMPOSITION_INVARIANTS.md#6-revision-accountability) | existing rule: cross-domain transfer and restore/migration keep material revision lineage |
| CI-07 Consent Propagation / Freshness | [`§7`](../COMPOSITION_INVARIANTS.md#7-consent-propagation--freshness) | copied consent/revocation state is not automatically current; existing rule: the receiving boundary keeps enough state to decide whether fresh reconciliation is required (scoped to consent / relational authorization) |
| CI-08 Freshness Accountability | [`§8`](../COMPOSITION_INVARIANTS.md#8-freshness-accountability) | a semantic object, receipt or admission result is not current after a material invalidating change; freshness is not inferred from retrieval or replay |
| CI-09 Particularity Preservation | [`§9`](../COMPOSITION_INVARIANTS.md#9-particularity-preservation) | existing rule: generalization keeps scope and provenance (scope-inflation guard) |
| SC-08 Replay | [`docs/CONFORMANCE_SCENARIOS.md`](../CONFORMANCE_SCENARIOS.md#sc-08--replay) | stale receipt after material change cannot establish current approval |
| SC-14 Stale consent | [`docs/CONFORMANCE_SCENARIOS.md`](../CONFORMANCE_SCENARIOS.md#sc-14--stale-consent) | copied historical consent does not count as current consent |
| SC-16 Scope inflation | [`docs/CONFORMANCE_SCENARIOS.md`](../CONFORMANCE_SCENARIOS.md#sc-16--scope-inflation) | generalization remains scoped, conditional, revisable, provenance-linked |

Naming note: the current repository titles CI-07 "Consent Propagation / Freshness" and CI-09 "Particularity Preservation"; they are cited here under those exact names.

## Coverage check

```text
COVERAGE CHECK: Existing composition invariants already cover the known principle-level risk.
RESULT: NO_NEW_INVARIANT
OPEN RESIDUAL: Only test whether a value matching a prior rejected/corrected value
under a declared owner-local identity rule can cross a domain boundary under a new
record identity in a way not caught by CI-04 / CI-06 / CI-07 / CI-08 / CI-09.
```

**Open research question:** Is there a concrete cross-domain case where the existing admission, freshness, revision, scope and provenance invariants fail to prevent re-entry of a value matching a prior rejected/corrected value under the target domain's declared identity policy?

Equivalence / normalization policy remains owner-local. Mentaury-Kernel does not define a matching rule.

## Out of scope here

- retrieval ranking;
- vector/index implementation;
- database tombstone design;
- memory extraction algorithm;
- value matching / normalization policy inside one owner domain;
- forced-vs-abstaining retrieval policy inside one owner domain (retrieval abstention is routed to Graphiti FM-16 Honest Empty / Crystal retrieval evaluation).

Those belong to their owning systems or research labs.

## Promotion boundary

No new invariant is created by this note. Promotion requires a concrete uncovered cross-domain failure plus the existing Scope Ownership / Necessity test.

```text
CURRENT RESULT: NO_NEW_INVARIANT
NO_RUNTIME_CHANGE
NO_CANON_CHANGE
```
