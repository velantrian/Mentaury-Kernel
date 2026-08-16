# 🧬 Composition Invariants

This document collects the current **composition-level** invariants. It does not define internal cognition, internal Native epistemic-history algorithms, or implementation technology.

## 1. Provenance conservation

Cross-domain transformation must not erase where material came from or silently make derived material appear independent of its source lineage.

```text
TRANSFORMATION ≠ NEW INDEPENDENT ORIGIN
RESTATEMENT ≠ REPLICATION
```

## 2. Authority non-escalation

A component gains no new truth, identity, consent, action, or runtime authority merely because it is integrated or technically convenient.

```text
INTEGRATION ≠ AUTHORITY TRANSFER
CAPABILITY ≠ AUTHORIZATION
```

## 3. Loss explicitness

If a target representation cannot preserve a material semantic distinction, the loss must be visible.

```text
SEMANTIC INCOMPATIBILITY
→ explicit PARTIAL / LOSSY / INCOMPATIBLE
→ never silent approximation
```

## 4. Admission isolation

Transport, compatibility, structural validity, and review receipts must remain distinct from semantic admission.

```text
DELIVERED
≠ STRUCTURALLY_VALID
≠ CONTINUITY_ACCEPTED
≠ TRUE
≠ IDENTITY_ADMITTED
```

## 5. Branch non-collapse

Shared history does not erase later divergence.

```text
SHARED HISTORY ≠ SAME CURRENT IDENTITY
RECORD MERGE ≠ IDENTITY MERGE
```

## 6. Revision accountability

Cross-domain transfer must preserve material revision lineage when that lineage is part of the meaning being transferred.

```text
CURRENT STATEMENT
≠ LICENSE TO ERASE HOW IT CHANGED
```

## 7. Attribution preservation

Imported material must not silently become autobiography, `SELF`, or identity content by transport, repetition, prestige, ownership, or presentation style.

```text
IMPORTED HERITAGE ≠ IMPORTED IDENTITY
OWNER STATEMENT ≠ AUTOMATIC IDENTITY FACT
```

## 8. Uncertainty preservation

Unknown, unsupported, contested, uncertain, or scoped representations must not be normalized into stronger epistemic status during composition.

```text
UNCERTAINTY IN SOURCE
→ uncertainty remains visible across boundary
```

## 9. Particularity preservation

Individual experience, aggregate patterns, and general models remain distinct.

```text
INDIVIDUAL TESTIMONY ≠ UNIVERSAL LAW
POPULATION PATTERN ≠ INDIVIDUAL TRUTH
MODEL OF PERSON ≠ PERSON
```

## 10. Non-circular generalization

A representation derived from a subject cannot later count as independent support about that same subject merely because it was transformed.

```text
AGGREGATE_DERIVED_FROM_SUBJECT
≠
INDEPENDENT_EVIDENCE_ABOUT_SUBJECT
```

## 11. Receipt non-laundering

Receipts prove only the bounded event they are defined to prove. They are not bearer tokens for authority escalation or later replay.

```text
RECEIPT
≠ TRUTH APPROVAL
≠ IDENTITY APPROVAL
≠ ACTION PERMISSION
```

## 12. Composition ≠ cognition

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
