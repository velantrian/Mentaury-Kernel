# 📌 Current Status — Mentaury-Kernel

**Repository:** `velantrian/Mentaury-Kernel`  
**Bootstrap date:** `2026-08-16`  
**Document envelope:** `DRAFT v0.2.4 · DOCUMENT_RECONCILIATION_ONLY`  
**Semantic architecture baseline:** `v0.2.3`  
**Repository stage:** `SPECIFICATION_BOOTSTRAP_ONLY`  
**External audit checkpoint:** Manus AI read-only audit at PR head `0028ab4e5d115220a61c96353a00b8ed4722f487` → `CHANGES_REQUIRED`; findings `F-01…F-06` remediated on the Draft branch; **re-review pending**.

## ✅ What exists

- technology-neutral composition architecture;
- explicit ownership boundaries between Native Kernel, Mentaury Soul, Port, and Governance;
- normative provenance discipline;
- source semantic pinning and reconciliation triggers;
- authority non-escalation rules;
- semantic-loss taxonomy;
- fork / restore / migration / consent boundaries;
- Particularity ↔ Generalization boundary;
- architecture-level threat model;
- architecture-level conformance scenarios;
- inclusion discipline for future invariants.

## 🚫 What does not exist

```text
runtime implementation          NONE
cognition runtime               NONE
truth authority                 NONE
identity authority              NONE
action authority                NONE
production authority            NONE
wire protocol                   NONE
storage/database decision       NONE
LLM/model dependency            NONE
executable conformance suite    NONE
```

Repository creation does not change any of these values.

## 🧭 Transitional documentation-authority boundary

The originating Notion architecture is currently marked `NOTION-FIRST`, while the permanent Notion↔GitHub semantic authority and conflict-resolution model remains **OPEN** in [Issue #2](https://github.com/velantrian/Mentaury-Kernel/issues/2).

During this bootstrap stage:

```text
REPOSITORY EXISTS
≠ GITHUB AUTOMATICALLY BECOMES SEMANTIC CANON

GITHUB / NOTION DIVERGENCE
→ STOP SILENT PROMOTION
→ RECONCILE EXPLICITLY
→ DO NOT GUESS WHICH CHANGE IS AUTHORITATIVE
```

GitHub is a reviewed specification-bootstrap surface. This temporary rule prevents accidental authority transfer between documentation surfaces; it **does not decide** the permanent authority model tracked in Issue #2.

## 📐 Evaluation class

Current architecture readiness is evaluated only as:

`DOCUMENT_INTERNAL_CONSISTENCY_ONLY`

Therefore:

```text
PASS
≠ executable conformance evidence
≠ implementation evidence
≠ independent review
≠ runtime authorization
≠ production authorization
```

## 🧬 Semantic source reconciliation

The current bootstrap carries forward the bounded semantic pins last reconciled on `2026-08-15`:

1. **Velantrim Native Kernel** — `Claim / representation ≠ reality / truth`; explicit uncertainty and accountable revision / retention / loss remain preserved for the composition-relevant scope.
2. **Mentaury Soul · NPG-v0.1** — imported Creator / historical / current-user / literary / research / model / reviewer material is not automatically `SELF`; fail-closed attribution semantics remain bounded and runtime remains separately unauthorized.
3. **Mentaury Soul · PCR-v0.1** — `SOURCE / PROVENANCE ≠ CLAIM ≠ EVIDENCE STATUS ≠ BELIEF STATUS ≠ TRUTH`; later Soul work does not automatically supersede this boundary.

These are semantic checkpoints, not mirrors of live upstream implementation status.

```text
SOURCE PAGE UPDATE ≠ AUTOMATIC COMPOSITION UPDATE
SOURCE FRESHNESS ≠ SEMANTIC INVALIDATION
REFERENCED SEMANTIC CONTRACT CHANGE = RECONCILIATION TRIGGER
```

## 🔬 Current inclusion rule

Before adding any new invariant, answer:

1. What concrete cross-domain failure does it prevent?
2. Is that failure already covered by an existing invariant?
3. Who owns the internal semantics: Soul, Native, Governance, or composition?
4. Can the necessary rule remain technology-neutral?

If these questions do not establish a distinct composition need, the proposal stays research material and does not become Mentaury-Kernel law.

## 🚪 Separate future gates

The following require separate decisions and must not be inferred from this bootstrap:

- permanent Notion ↔ GitHub semantic authority / conflict-resolution model — [Issue #2](https://github.com/velantrian/Mentaury-Kernel/issues/2);
- repository license — [Issue #2](https://github.com/velantrian/Mentaury-Kernel/issues/2);
- executable conformance format — [Issue #2](https://github.com/velantrian/Mentaury-Kernel/issues/2);
- concrete Port representation / serialization;
- runtime implementation;
- implementation language;
- dependency choices;
- security/deployment profile;
- production authorization.

## 🛡️ Change rule

Any PR that appears to change truth, identity, cognition, action, runtime, production, or documentation authority must be treated as an **architecture-boundary change**, not routine documentation cleanup.

`SPECIFICATION BOOTSTRAP ≠ IMPLEMENTATION AUTHORITY`
