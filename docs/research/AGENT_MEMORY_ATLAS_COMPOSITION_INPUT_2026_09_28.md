# Agent Memory Atlas composition input — 2026-09-28

**Status:** `RESEARCH INPUT · NON-CANON · COMPOSITION RELEVANCE ONLY · NO_NEW_INVARIANT · NO_RUNTIME_CHANGE`

Source overview: [Agent Memory Atlas](https://neoneye.github.io/agent-memory-atlas/).

## Scope ownership test

Only cross-domain preservation consequences belong in this repository. Internal memory algorithms, retrieval engines, tombstone schemas, matching/normalization policies and storage choices do not.

This reconciliation builds on prior Atlas-related / pre-existing overlapping coverage in 💠 Crystal (`docs/research/MEMORY_EVAL_ADVERSARIAL_PROFILE_V0.md`, [PR #462](https://github.com/velantrian/velantrim-exocortex-crystal/pull/462)) and 🧬 Native Kernel (`docs/research/MEMORY_EVALUATION_PROTOCOL_V0.md`). This note records only the cross-domain residual after checking existing composition coverage.

## Source-fidelity note

The following claim-level sources were verified at the exact revisions linked below; these are specific donor examples, not a representative benchmark or exhaustive survey.

- **Universal Memory Engine:** the [Atlas analysis](https://neoneye.github.io/agent-memory-atlas/systems/universal-memory-engine/) identifies analyzed source revision [`b17c5486553634b66b3aa70777a007928dab54d7`](https://github.com/12ziyad/universal-memory-engine/commit/b17c5486553634b66b3aa70777a007928dab54d7). At that revision, [`src/pipeline/gates.js`](https://github.com/12ziyad/universal-memory-engine/blob/b17c5486553634b66b3aa70777a007928dab54d7/src/pipeline/gates.js) checks suppressions using `kind:canonicalKey(label)`; [`src/lib/db.js`](https://github.com/12ziyad/universal-memory-engine/blob/b17c5486553634b66b3aa70777a007928dab54d7/src/lib/db.js) defines `canonicalKey` via `normalizeLabel` and persists/lookups suppressions by user, kind, and canonical key; [`migrations/0003_run_32_memory_pages.sql`](https://github.com/12ziyad/universal-memory-engine/blob/b17c5486553634b66b3aa70777a007928dab54d7/migrations/0003_run_32_memory_pages.sql) defines the lookup index. This supports only the source-specific, normalized-label mechanism observed at that commit.
- **Project Golem (contrast, not the same mechanism):** the [Atlas analysis](https://neoneye.github.io/agent-memory-atlas/systems/project-golem/) pins source revision [`210658a11bee669df875cc6edc0511fac239d1ba`](https://github.com/Arvincreator/project-golem/commit/210658a11bee669df875cc6edc0511fac239d1ba), and [`packages/memory/ExperienceMemory.js`](https://github.com/Arvincreator/project-golem/blob/210658a11bee669df875cc6edc0511fac239d1ba/packages/memory/ExperienceMemory.js) records a capped list of rejected proposal types, clears it on success, and renders it as advice. That artifact is not evidence of value-level semantic matching; the Atlas report discusses a separate memory-firewall path.

The Universal Memory Engine suppression key is specifically scoped by `user_id`, `kind`, and `canonical_key` (with project scope applied by the lookup where supplied); it is not a generic `scope + subject + predicate` policy.

```text
DECLARED NORMALIZED VALUE MATCH != ARBITRARY SEMANTIC PARAPHRASE MATCH
```

These source revisions do not establish general semantic-equivalence blocking. Any paraphrase-matching question is an open, owner-local policy / separate test question and is not assumed here. The external donor reports are research evidence only, not validation authority for Mentaury-Kernel.

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

```text
EXTERNAL DONOR != VALIDATION AUTHORITY != CANON != RUNTIME != NEW INVARIANT
```
