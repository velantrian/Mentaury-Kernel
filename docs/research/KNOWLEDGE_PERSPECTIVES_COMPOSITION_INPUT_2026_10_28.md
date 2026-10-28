# Knowledge Perspectives — cross-domain composition research input (2026-10-28)

**Status:** `RESEARCH INPUT · NON-CANON · DOCS-ONLY · NO NEW INVARIANT · NO NEW PORT · NO RUNTIME / AUTHORITY CHANGE`
**Source class:** cross-project use-case reconciliation, not a normative change.
**Source baseline:** `main@485ac073c7ad1ba018d071716b84e2646404ff10` as observed on 2026-10-28.
**Ownership:** Knowledge Semantics owns its descriptive vocabulary; Crystal and the other domains retain their source-specific evidence, epistemic, identity and action boundaries. This repository owns composition constraints only.

## 1. Why this note exists

Velantrim knowledge collection proposes four collection directions (foundational/stable, contextual/variant, practical/procedural, living perspectives) with purpose and reasoning as cross-cutting concerns. This is **not** a request for a five-database architecture. The canonical cross-project vocabulary already names **five orthogonal descriptive dimensions**:

- [VELANTRIM_KNOWLEDGE_SEMANTICS.md](https://github.com/velantrian/velantrim/blob/main/docs/knowledge/VELANTRIM_KNOWLEDGE_SEMANTICS.md) — `Stability / Variance / Practical / Perspective / Purpose`, descriptive; no authority transfer.
- [Knowledge Collection × Mentaury Research Crosswalk](https://app.notion.com/p/407ac84d054781f8bb7df570b24e204b) — scoped research synthesis only.
- [Mentaury-Life v0.3](https://docs.google.com/document/d/1DoPzWOkMsE0qXzqEqGDpCn0GeJw4KNK7t8IaQaQJmJk/edit) — fixed research baseline, **not** an owner for Kernel invariants.
- [Digital Brain reconciliation](https://docs.google.com/document/d/1-_SWbyv9lbScpHf39bcPS7gOu_fMri4_mNRlMCO9PBQ/edit) — historical implementation profile distinguished from neutral meaning.

The question here is limited to **what distinctions a transfer must preserve** when independently governed systems use these knowledge perspectives.

## 2. Concrete boundary example: one tree, multiple interpretations

Source S: a study reports observations that a certain bird species perches on some branches of a tree under specified season and habitat conditions.

Producer P: a collection agent extracts: `bird/tree/perching` with `source`, `species`, `observed_conditions`, `observation_vs_interpretation`, `uncertainty`, and a versioned `perspective-model` classification.

Consumer C: an independent domain summarizes: "for the bird, this tree offers a vantage point" and retrieves human/practical uses (shade, fruit, timber) and a conservation purpose.

Plausible cross-boundary failures:

| Failure | Why it matters | Existing coverage |
| --- | --- | --- |
| Source lineage lost in a summary; repeating C is treated as independent evidence | Artificially inflates support | SC-02 Evidence Laundering; SC-12 Cross-Boundary Epistemic Echo |
| "Bird can perch" becomes "all birds perceive this tree as safe" | Scope/species/conditions and observation-vs-inference lost | SC-13 Semantic Downgrade; SC-16 Particular→General Scope Inflation; SC-04 Silent Loss |
| Represented affordance becomes the animal's lived subjective experience | Interpretation promoted to identity/experience fact without evidence | SC-01 Projection Laundering; SC-10 Source-Authority Spoofing; SC-16 Scope Inflation |
| Practical procedure is transferred as permission to run a tool or modify environment | Cross-domain authority creep | SC-03 Authority Creep; SC-09 Receipt Laundering |
| User's restoration goal is treated as proof that a biological claim is true | Confuses objective with evidentiary basis | SC-03 Authority Creep; SC-10 Source-Authority Spoofing |
| Archived or context-specific relationship is reused after a material change | Stale semantics presented as current | SC-08 Replay Divergence; SC-14 Stale Consent / Authority; source update reconciliation |

**Disposition:** The present use-case maps to *existing* scenarios. No concrete uncovered cross-domain failure requiring a new CI/SC or Port field has been established.

## 3. Transfer/conformance research questions (not new required fields)

1. Can a producer and consumer retain and inspect source identity, derivation lineage, observer/species, temporal/local scope and relevant exclusions?
2. When a summary drops a distinction, is loss honestly declared with the existing architecture vocabulary `PRESERVED / PARTIAL / UNSUPPORTED / INDETERMINATE / LOSSY` (Port disposition remains separate)?
3. Can a recipient detect `CONTRADICTS_CANDIDATE` without treating a relation/score as adjudicated truth?
4. Can a consumer distinguish descriptive perspective claims from normative goals and from granted action capabilities?
5. Are transported classifications themselves treated as source-attributed, revisable claims rather than privileged meta-truth?
6. Does a target perform its own admission when receiving a delivered artifact, independently of transport validation?

These are **test case ideas**, not results and not changes to SC-01…SC-16. Any executable test/profile expansion requires explicit separate owner authorization.

## 4. Neutrality and stop rule

`COMPOSITION != COGNITION`.
`CLASSIFICATION != TRUTH`.
`PERSPECTIVE MODEL != LIVED EXPERIENCE`.
`PROCEDURE != PERMISSION`.
`PURPOSE != EVIDENCE`.
`RETRIEVAL != USE`.
`DELIVERED != TRUE != ADMITTED`.

No BM25, vector index, graph DB, prompt format, LLM, multi-tier store or "Living Perspectives Engine" is required by this composition note.

**STOP:** Unless a reproducible, materially new cross-boundary failure evades existing CI/SC coverage, close this input as research-only and avoid new invariants, ports, runtime wiring, claim promotions, model choices, merge authorization, or production claims. The repo's independent governance/review requirements still apply.

## 5. Status and sources

This note documents a new example over existing rules; it has no new semantic Canon and no tested implementation. The PR carrying this note is a proposed documentation change only. GitHub/Notion authority reconciliation and license decisions remain open in [Issue #2](https://github.com/velantrian/Mentaury-Kernel/issues/2).
