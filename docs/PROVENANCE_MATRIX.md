# 📜 Normative Provenance Matrix

Mentaury-Kernel must not present a locally useful idea as Canon of another project. Every normative rule therefore records origin, source status, local status, scope, rationale, and supersession state.

## 1. Closed status vocabulary

```text
INHERITED_CANONICAL
INHERITED_PROVISIONAL
COMPOSITION_PROPOSED
DERIVED
OPEN
REJECTED
SUPERSEDED
```

The status vocabulary is closed for the current semantic baseline. Scope qualifiers belong in a separate `Scope` field; they must not be encoded by inventing ad-hoc status tokens.

## 2. Required fields

Every normative record must identify:

- `Invariant`
- `Origin project / composition`
- `Source artifact`
- `Source status`
- `Local composition status`
- `Scope`
- `Rationale`
- `Supersedes / Superseded by`

Inherited rules additionally identify:

- `Exact source locator / checkpoint`
- `Verified as of`
- `Reconciliation trigger`

`Local composition status` is the only local status field. Scope qualifiers are not encoded into the status token. Local composition rules do not need to imitate inherited-source pin metadata.

## 3. Source verification rule

```text
SOURCE PAGE UPDATE ≠ AUTOMATIC COMPOSITION UPDATE
SOURCE FRESHNESS ≠ SEMANTIC INVALIDATION
REFERENCED SEMANTIC CONTRACT CHANGE = RECONCILIATION TRIGGER
```

A live registry/root page may be used as a navigation or evidence surface, but an inherited pin must name the exact semantic checkpoint that was actually checked and provide a resolvable source locator where one exists.

A live status change, CI update, implementation milestone, or neighboring documentation edit does not automatically rewrite Mentaury-Kernel semantics. Reconciliation is required when the referenced semantic statement itself is superseded, materially re-scoped, loses support, or changes ownership.

---

## 4. Current inherited semantic pins

### NK-01 · Native claim / representation boundary

**Invariant**  
`Claim / representation ≠ reality / truth`; explicit unknown / uncertainty / unsupported status remains visible; accountable change / revision / retention / loss remains explicit for the declared scope.

**Origin project / composition**  
`Velantrim Native Kernel`

**Source artifact**  
[Native Kernel · Core Architecture & Invariants](https://app.notion.com/p/3a5ac84d0547815ba58bd2ed52771601)

**Source status**  
`IAR-1 RECONCILED PROBLEM-LEVEL MINIMUM · ARCHITECTURE STRENGTHENED_FOR_BPV1_SCOPE / STILL_PROVISIONAL`

**Local composition status**  
`INHERITED_PROVISIONAL`

**Scope**  
Only composition-relevant boundaries: non-conflation of representation and truth, explicit uncertainty, and accountable revision / retention / loss. No internal Native implementation form is inherited.

**Rationale**  
Cross-domain transfer must not silently convert Native representations or history into truth, or erase uncertainty and revision lineage.

**Supersedes / Superseded by**  
No local predecessor; not superseded as of `2026-08-16`.

**Exact source locator / checkpoint**  
[Native Kernel · Core Architecture & Invariants](https://app.notion.com/p/3a5ac84d0547815ba58bd2ed52771601) → `IAR-1 reconciled checkpoint · Reconciled minimum · 2026-08-11`.

**Verified as of**  
`2026-08-16` — rechecked against the current Native architecture authority-routing surface after later H11/authority-routing hygiene. The current authority chain still resolves through IAR-1/IAR-1-R1, preserves the same problem-level minimum, keeps the architecture scoped/provisional, and does not promote implementation/profile structures into universal Canon.

**Reconciliation trigger**  
The referenced minimum is superseded, materially re-scoped, loses support, or Native changes the composition-relevant meaning or ownership of Claim, uncertainty, revision, retention, or loss.

---

### SOUL-01 · Fail-closed self / non-self attribution

**Invariant**  
Imported Creator / historical / current-user / literary / research / model / reviewer material is not automatically `SELF`; absent separately authorized identity / continuation evidence it remains non-self or unknown according to the owning Soul contract.

**Origin project / composition**  
`Mentaury Soul`

**Source artifact**  
[Mentaury · Research Registry](https://app.notion.com/p/3b5ac84d05478106b93dff3dcefc6396) — owning NPG-v0.1 research/status surface.

**Source status**  
`NPG-v0.1 · FROZEN_DOCS · IMPLEMENTED_BOUNDED`; runtime separately unauthorized.

**Local composition status**  
`INHERITED_CANONICAL`

**Scope**  
Imported human, historical, literary, research, model, reviewer, and current-user material at the self/non-self attribution boundary. This pin does not create an Identity Engine, relationship authority, or action/runtime authority.

**Rationale**  
Composition must not launder imported material into Mentaury autobiography or `SELF` merely because it was transported, repeated, summarized, or supplied by an owner.

**Supersedes / Superseded by**  
No local predecessor; not superseded as of `2026-08-16`.

**Exact source locator / checkpoint**  
[Mentaury · Research Registry](https://app.notion.com/p/3b5ac84d05478106b93dff3dcefc6396) → `NPG-v0.1 Contract Freeze (#86)` + `Budget Semantics Clarified (#87)`. The named frozen checkpoint, not the current top of the registry, is the semantic pin.

**Verified as of**  
`2026-08-16` — the current Soul research registry still records `NPG-v0.1 · UNCHANGED`, `IMPLEMENTED_BOUNDED`, and runtime `NOT_AUTHORIZED`; later Soul milestones do not supersede the pinned fail-closed attribution semantics.

**Reconciliation trigger**  
The NPG self/non-self contract is superseded, materially weakened/re-scoped, or the authoritative identity/continuation evidence contract changes what may establish verified self-attribution.

---

### SOUL-02 · PCR provenance / claim separation

**Invariant**  
`SOURCE / PROVENANCE ≠ CLAIM ≠ EVIDENCE STATUS ≠ BELIEF STATUS ≠ TRUTH`

**Origin project / composition**  
`Mentaury Soul`

**Source artifact**  
[Mentaury Soul](https://app.notion.com/p/3b2ac84d054781cf841ed08ca339f211) — owning PCR-v0.1 surface.

**Source status**  
`Phase 3 PCR-v0.1 · IMPLEMENTED_BOUNDED · FROZEN_DOCS`

**Local composition status**  
`INHERITED_CANONICAL`

**Scope**  
Composition inheritance of provenance / claim separation only. PCR representation does not itself decide source admission, evidence verdict, belief status, truth, identity, or action authority.

**Rationale**  
Provenance metadata and claim representation must survive transfer without being mistaken for evidence admission, belief commitment, or truth.

**Supersedes / Superseded by**  
No local predecessor; not superseded as of `2026-08-16`.

**Exact source locator / checkpoint**  
[Mentaury Soul](https://app.notion.com/p/3b2ac84d054781cf841ed08ca339f211) → `Phase 3 PCR-v0.1 · IMPLEMENTED_BOUNDED · FROZEN_DOCS` and its explicit provenance/claim/evidence/belief/truth separation.

**Verified as of**  
`2026-08-16` — the current Soul surface continues to state `SOURCE / PROVENANCE ≠ CLAIM ≠ EVIDENCE STATUS ≠ BELIEF STATUS ≠ TRUTH`; later ATR/HDE work remains separately bounded and does not supersede Evidence Gate or source-admission ownership.

**Reconciliation trigger**  
PCR provenance/claim separation is superseded, materially weakened/re-scoped, or ownership of evidence status, belief status, truth, or source admission changes in a way material to composition.

---

## 5. Local composition rules

### 5.1 Coverage registry for the 12-item composition taxonomy

The twelve current composition invariants are local Mentaury-Kernel rules defined in `docs/COMPOSITION_INVARIANTS.md`. This registry supplies the provenance fields required by §2 without changing their wording, order, or semantic status.

| ID | Invariant | Source artifact | Source status | Local composition status | Scope | Rationale | Supersedes / Superseded by |
|---|---|---|---|---|---|---|---|
| CI-01 | Provenance Conservation | `docs/COMPOSITION_INVARIANTS.md §1` | `COMPOSITION_LOCAL · DRAFT semantic baseline v0.2.3` | `COMPOSITION_PROPOSED` | provenance across cross-domain transformation | prevent transformed material from appearing independently sourced | none |
| CI-02 | Authority Non-Escalation | `docs/COMPOSITION_INVARIANTS.md §2` | `COMPOSITION_LOCAL · DRAFT semantic baseline v0.2.3` | `COMPOSITION_PROPOSED` | authority across integrated domains | prevent technical integration from creating truth, identity, consent, action, or runtime authority | none |
| CI-03 | Loss Explicitness | `docs/COMPOSITION_INVARIANTS.md §3` | `COMPOSITION_LOCAL · DRAFT semantic baseline v0.2.3` | `COMPOSITION_PROPOSED` | semantic degradation during transfer | prevent weaker representations from silently strengthening or normalizing source meaning | none |
| CI-04 | Admission Isolation | `docs/COMPOSITION_INVARIANTS.md §4` | `COMPOSITION_LOCAL · DRAFT semantic baseline v0.2.3` | `COMPOSITION_PROPOSED` | delivery / validation versus target-domain admission | prevent transport or structural validity from becoming semantic admission | none |
| CI-05 | Branch Non-Collapse | `docs/COMPOSITION_INVARIANTS.md §5` | `COMPOSITION_LOCAL · DRAFT semantic baseline v0.2.3` | `COMPOSITION_PROPOSED` | forked histories and current branch state | preserve shared provenance without collapsing later divergence | none |
| CI-06 | Revision Accountability | `docs/COMPOSITION_INVARIANTS.md §6` | `COMPOSITION_LOCAL · DRAFT semantic baseline v0.2.3` | `COMPOSITION_PROPOSED` | material revision lineage | prevent current state from erasing meaning carried by how it changed | none |
| CI-07 | Consent Propagation / Freshness | `docs/COMPOSITION_INVARIANTS.md §7` | `COMPOSITION_LOCAL · DRAFT semantic baseline v0.2.3` | `COMPOSITION_PROPOSED` | copied / restored / migrated consent state | prevent historical consent from becoming automatic current authority | none |
| CI-08 | Freshness Accountability | `docs/COMPOSITION_INVARIANTS.md §8` | `COMPOSITION_LOCAL · DRAFT semantic baseline v0.2.3` | `COMPOSITION_PROPOSED` | stale receipts, assumptions, semantics, and inputs | require reconciliation after material invalidating change | none |
| CI-09 | Particularity Preservation | `docs/COMPOSITION_INVARIANTS.md §9` | `COMPOSITION_LOCAL · DRAFT semantic baseline v0.2.3` | `COMPOSITION_PROPOSED` | individual, aggregate, and general-model levels | prevent scope inflation and person-model/person conflation | none |
| CI-10 | Non-Circular Generalization | `docs/COMPOSITION_INVARIANTS.md §10` | `COMPOSITION_LOCAL · DRAFT semantic baseline v0.2.3` | `COMPOSITION_PROPOSED` | subject-derived aggregates returned to the same subject | prevent transformed dependent material from masquerading as independent support | none |
| CI-11 | Receipt Non-Laundering | `docs/COMPOSITION_INVARIANTS.md §11` | `COMPOSITION_LOCAL · DRAFT semantic baseline v0.2.3` | `COMPOSITION_PROPOSED` | bounded receipts and later replay | prevent receipts from becoming bearer tokens for broader authority | none |
| CI-12 | Composition ≠ Cognition | `docs/COMPOSITION_INVARIANTS.md §12` | `COMPOSITION_LOCAL · DRAFT semantic baseline v0.2.3` | `COMPOSITION_PROPOSED` | ownership boundary of Mentaury-Kernel | prevent composition rules from absorbing internal cognition or epistemic-history implementation | none |

**Origin project / composition for CI-01…CI-12:** `Mentaury-Kernel · local composition`.

The detailed local rules below are retained as focused cross-cutting records; they do not replace the twelve-item coverage registry.

### 5.2 Focused local records

### MK-01 · Port validation ≠ semantic approval

**Invariant**  
`Port validation ≠ semantic approval`

**Origin project / composition**  
`Mentaury-Kernel · local composition`

**Source artifact**  
`docs/ARCHITECTURE.md` · Semantic Continuity Port + Receipt Taxonomy

**Source status**  
`COMPOSITION_LOCAL · DRAFT semantic baseline v0.2.3`

**Local composition status**  
`COMPOSITION_PROPOSED`

**Scope**  
Transport/version compatibility, structural validation, declared loss, and bounded receipts at the Native↔Soul composition boundary.

**Rationale**  
Successful delivery or structural compatibility cannot become bearer authority for truth, identity admission, consent, or downstream action.

**Supersedes / Superseded by**  
No local predecessor.

---

### MK-02 · Subject-derived aggregate ≠ independent evidence about subject

**Invariant**  
`AGGREGATE_DERIVED_FROM_SUBJECT ≠ INDEPENDENT_EVIDENCE_ABOUT_SUBJECT`

**Origin project / composition**  
`Mentaury-Kernel · local composition`

**Source artifact**  
`docs/ARCHITECTURE.md` · Particularity ↔ Generalization boundary

**Source status**  
`COMPOSITION_LOCAL · DRAFT semantic baseline v0.2.3`

**Local composition status**  
`COMPOSITION_PROPOSED`

**Scope**  
Human testimony, person models, aggregates, and derived summaries used across domains.

**Rationale**  
Information causally derived from subject A cannot return to A as independent corroboration merely because it has been transformed, aggregated, summarized, or repeated.

**Supersedes / Superseded by**  
No local predecessor.
