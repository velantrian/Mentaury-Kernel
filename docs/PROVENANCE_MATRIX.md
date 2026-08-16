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

- `Referenced semantic checkpoint`
- `Verified as of`
- `Reconciliation trigger`

## 3. Source verification rule

```text
SOURCE PAGE UPDATE ≠ AUTOMATIC COMPOSITION UPDATE
SOURCE FRESHNESS ≠ SEMANTIC INVALIDATION
REFERENCED SEMANTIC CONTRACT CHANGE = RECONCILIATION TRIGGER
```

A live status change, CI update, implementation milestone, or neighboring documentation edit does not automatically rewrite Mentaury-Kernel semantics. Reconciliation is required when the referenced semantic statement itself is superseded, materially re-scoped, loses support, or changes ownership.

---

## 4. Current inherited semantic pins

### NK-01 · Native claim / representation boundary

**Invariant**  
`Claim / representation ≠ reality / truth`; explicit unknown / uncertainty / unsupported status remains visible; accountable change / revision / retention / loss remains explicit for the declared scope.

**Origin project / composition**  
`Velantrim Native Kernel`

**Source artifact**  
Owning Native Kernel architecture / invariants surface, semantic checkpoint `IAR-1 reconciled problem-level minimum`.

**Source status**  
`STRENGTHENED_FOR_BPV1_SCOPE / STILL_PROVISIONAL`

**Local composition status**  
`INHERITED_PROVISIONAL`

**Scope**  
Only composition-relevant boundaries: non-conflation of representation and truth, explicit uncertainty, and accountable revision / retention / loss. No internal Native implementation form is inherited.

**Rationale**  
Cross-domain transfer must not silently convert Native representations or history into truth, or erase uncertainty and revision lineage.

**Supersedes / Superseded by**  
No local predecessor; not superseded as of `2026-08-15`.

**Referenced semantic checkpoint**  
`IAR-1 reconciled checkpoint · Reconciled minimum · 2026-08-11`

**Verified as of**  
`2026-08-15` — rechecked after later H11 validation hardening; the owning Native architecture explicitly retained the same architecture meaning and scoped/provisional status.

**Reconciliation trigger**  
The referenced minimum is superseded, materially re-scoped, loses support, or Native changes the composition-relevant meaning or ownership of Claim, uncertainty, revision, retention, or loss.

---

### SOUL-01 · Fail-closed self / non-self attribution

**Invariant**  
Imported Creator / historical / current-user / literary / research / model / reviewer material is not automatically `SELF`; absent separately authorized identity / continuation evidence it remains non-self or unknown according to the owning Soul contract.

**Origin project / composition**  
`Mentaury Soul`

**Source artifact**  
Owning Soul research/status surfaces for `NPG-v0.1`.

**Source status**  
`NPG-v0.1 · FROZEN_DOCS · IMPLEMENTED_BOUNDED`; runtime separately unauthorized.

**Local composition status**  
`INHERITED_CANONICAL`

**Scope**  
Imported human, historical, literary, research, model, reviewer, and current-user material at the self/non-self attribution boundary. This pin does not create an Identity Engine, relationship authority, or action/runtime authority.

**Rationale**  
Composition must not launder imported material into Mentaury autobiography or `SELF` merely because it was transported, repeated, summarized, or supplied by an owner.

**Supersedes / Superseded by**  
No local predecessor; not superseded as of `2026-08-15`.

**Referenced semantic checkpoint**  
`NPG-v0.1 Contract Freeze (#86) · Budget Semantics Clarified (#87)`

**Verified as of**  
`2026-08-15` — the current Soul state records bounded implementation while preserving the frozen fail-closed attribution semantics and keeping runtime unauthorized.

**Reconciliation trigger**  
The NPG self/non-self contract is superseded, materially weakened/re-scoped, or the authoritative identity/continuation evidence contract changes what may establish verified self-attribution.

---

### SOUL-02 · PCR provenance / claim separation

**Invariant**  
`SOURCE / PROVENANCE ≠ CLAIM ≠ EVIDENCE STATUS ≠ BELIEF STATUS ≠ TRUTH`

**Origin project / composition**  
`Mentaury Soul`

**Source artifact**  
Owning Soul PCR-v0.1 surfaces.

**Source status**  
`Phase 3 PCR-v0.1 · IMPLEMENTED_BOUNDED · FROZEN_DOCS`

**Local composition status**  
`INHERITED_CANONICAL`

**Scope**  
Composition inheritance of provenance / claim separation only. PCR representation does not itself decide source admission, evidence verdict, belief status, truth, identity, or action authority.

**Rationale**  
Provenance metadata and claim representation must survive transfer without being mistaken for evidence admission, belief commitment, or truth.

**Supersedes / Superseded by**  
No local predecessor; not superseded as of `2026-08-15`.

**Referenced semantic checkpoint**  
`Phase 3 PCR-v0.1 · IMPLEMENTED_BOUNDED · FROZEN_DOCS`

**Verified as of**  
`2026-08-15` — later Soul ATR/HDE work does not supersede this separation; Evidence Gate and source-admission ownership remain distinct.

**Reconciliation trigger**  
PCR provenance/claim separation is superseded, materially weakened/re-scoped, or ownership of evidence status, belief status, truth, or source admission changes in a way material to composition.

---

## 5. Local composition rules

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
