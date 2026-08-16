# 🧬 Composition Invariants

This document mirrors the current **composition-level invariant taxonomy** from the reconciled architecture baseline. It does not define internal cognition, internal Native epistemic-history algorithms, or implementation technology.

## 1. Provenance Conservation

Cross-domain transformation must not erase where material came from or silently make derived material appear independent of its source lineage.

```text
TRANSFORMATION ≠ NEW INDEPENDENT ORIGIN
RESTATEMENT ≠ REPLICATION
```

Attribution and uncertainty that are material to provenance must remain visible rather than being normalized away.

## 2. Authority Non-Escalation

A component gains no new truth, identity, consent, action, or runtime authority merely because it is integrated or technically convenient.

```text
INTEGRATION ≠ AUTHORITY TRANSFER
CAPABILITY ≠ AUTHORIZATION
```

## 3. Loss Explicitness

If a target representation cannot preserve a material semantic distinction, the loss must be visible.

```text
SEMANTIC INCOMPATIBILITY
→ explicit PARTIAL / LOSSY / INCOMPATIBLE
→ never silent approximation
```

Unknown, unsupported, contested, uncertain, or scoped source material must not become stronger merely because the target representation is less expressive.

## 4. Admission Isolation

Transport, compatibility, structural validity, and review receipts must remain distinct from semantic admission.

```text
DELIVERED
≠ STRUCTURALLY_VALID
≠ CONTINUITY_ACCEPTED
≠ TRUE
≠ IDENTITY_ADMITTED
```

Imported human, historical, literary, research, owner, or model material does not become `SELF` or identity content merely by crossing the boundary.

## 5. Branch Non-Collapse

Shared history does not erase later divergence.

```text
SHARED HISTORY ≠ SAME CURRENT IDENTITY
RECORD MERGE ≠ IDENTITY MERGE
```

Forks preserve common provenance while keeping current branch state distinct.

## 6. Revision Accountability

Cross-domain transfer must preserve material revision lineage when that lineage is part of the meaning being transferred.

```text
CURRENT STATEMENT
≠ LICENSE TO ERASE HOW IT CHANGED
```

Restore and migration must not silently erase later history or the fact that a position, relationship, or claim changed.

## 7. Consent Propagation / Freshness

Consent or relational authorization does not remain current automatically merely because an old state, snapshot, fork, backup, or migration package contains it.

```text
HISTORICAL CONSENT
≠ AUTOMATIC CURRENT CONSENT

COPIED CONSENT STATE
≠ CURRENT AUTHORITY
```

When consent or revocation is material to the receiving use, the receiving boundary must preserve enough state to determine whether fresh reconciliation is required.

## 8. Freshness Accountability

A semantic object, receipt, authority assumption, or admission result must not be treated as current after a material change that invalidates its scope or basis.

```text
VALID AT S1
+ MATERIAL CHANGE TO S2
≠ AUTOMATICALLY VALID AT S2
```

Freshness must be accountable rather than inferred from successful retrieval or replay.

This applies especially to:

- stale receipts;
- stale authority assumptions;
- changed source semantics;
- materially changed inputs;
- migration / restore boundaries;
- revised commitments or relationship state.

## 9. Particularity Preservation

Individual experience, aggregate patterns, and general models remain distinct.

```text
INDIVIDUAL TESTIMONY ≠ UNIVERSAL LAW
POPULATION PATTERN ≠ INDIVIDUAL TRUTH
MODEL OF PERSON ≠ PERSON
```

Generalization must preserve scope, provenance, and the distinction between a hypothesis about a person and a fact about that person.

## 10. Non-Circular Generalization

A representation derived from a subject cannot later count as independent support about that same subject merely because it was transformed.

```text
AGGREGATE_DERIVED_FROM_SUBJECT
≠
INDEPENDENT_EVIDENCE_ABOUT_SUBJECT
```

## 11. Receipt Non-Laundering

Receipts prove only the bounded event they are defined to prove. They are not bearer tokens for authority escalation or later replay.

```text
RECEIPT
≠ TRUTH APPROVAL
≠ IDENTITY APPROVAL
≠ ACTION PERMISSION
```

## 12. Composition ≠ Cognition

Mentaury-Kernel defines cross-domain preservation and authority boundaries. It does not own internal thinking, inquiry, identity development, or epistemic-history implementation.

```text
COMPOSITION ≠ COGNITION
```

## Inclusion guard

Before adding another invariant:

```text
Does a concrete cross-domain failure exist?
        │
        ├── NO → do not add a law
        │
        └── YES
             ↓
Is it already covered above?
        │
        ├── YES → do not duplicate
        │
        └── NO
             ↓
Can the smallest rule remain technology-neutral?
        │
        ├── NO → implementation profile / upstream owner
        │
        └── YES → composition candidate
```

`ARCHITECTURAL FIT ≠ ARCHITECTURAL NECESSITY`
