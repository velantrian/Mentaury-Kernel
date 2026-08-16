# 🧭 Mentaury-Kernel Architecture

## 1. Mission

Mentaury-Kernel is a **revisable, technology-neutral composition specification** for interactions between independently governed semantic domains.

Its job is not to compute cognition. Its job is to define what must remain explicit when meaning crosses system boundaries.

It answers questions such as:

- what provenance must survive transfer;
- which authority belongs to which domain;
- what semantic loss occurred;
- what a receipt proves and does not prove;
- how fork / restore / migration affect continuity claims;
- how individual experience may be abstracted without becoming universal truth;
- how composition boundaries are challenged through adversarial scenarios.

## 2. Core invariant

```text
COMPOSITION ≠ COGNITION
```

Mentaury-Kernel is not:

- a third brain;
- a superior arbiter over Native Kernel or Mentaury Soul;
- a Truth Gate;
- an Identity Engine;
- a scheduler;
- an autonomous loop;
- a runtime coordinator.

## 3. Scope Ownership Test

Every proposed rule must pass this routing test before inclusion.

```text
Does the rule describe HOW cognition, inquiry,
attention, deliberation, or result formation works?
→ YES: 🌀 MENTAURY SOUL INTERNAL

Does it describe internal self/non-self,
identity admission/evolution, relationships,
or other identity-domain processes?
→ YES: 🌀 MENTAURY SOUL INTERNAL

Does it describe WHAT must survive about provenance,
authority, loss, scope, or admission when meaning
crosses domains?
→ YES: 🪁 COMPOSITION

Does it describe internal epistemic-history semantics,
revision, retention, replay, or loss?
→ YES: 🧬 NATIVE KERNEL INTERNAL

Does it depend on a specific LLM, database, graph,
vector store, programming language, device, or framework?
→ YES: 🚫 IMPLEMENTATION-SPECIFIC
```

## 4. Ownership matrix

| Domain | Owns | Does not own |
|---|---|---|
| 🧬 Native Kernel | epistemic-history semantics, provenance, uncertainty, accountable revision / retention / loss | cognition, identity admission, consent, relationship truth |
| 🌀 Mentaury Soul | cognition-domain and identity-domain semantics | rewriting upstream provenance; automatic claim→truth promotion |
| 🌉 Continuity Port | transport, compatibility checks, structural validation, declared loss, bounded receipts | truth, identity, consent, action decisions |
| 🪁 Mentaury-Kernel | composition invariants, authority boundaries, cross-domain threat model, conformance specification | runtime coordination, internal algorithms, superior authority |
| 🏛️ Governance | bounded authorization and admission procedures in the owning project | automatic truth or identity-content authority |

```text
INTEGRATION ≠ AUTHORITY TRANSFER
```

## 5. Semantic Continuity Port

The Port is a bounded composition boundary, not a decision engine.

### Data plane

```text
🧬 Native Kernel
      ↓
versioned semantic / continuity envelope
      ↓
🌉 Port
      ↓
🌀 Mentaury Soul
```

### Bounded disposition plane

A receiving domain may return bounded processing dispositions such as:

```text
ACCEPTED_FOR_REVIEW
DEFERRED
REJECTED
INCOMPATIBLE
```

These are **Port dispositions**, not semantic-loss values. In particular, `INCOMPATIBLE` indicates a bounded disposition at the Port boundary and must not replace `INDETERMINATE` in the loss taxonomy.

Such a response may be recorded or reconciled upstream, but it does not grant permission to rewrite source history or promote semantic authority.

### Port laws

```text
Port validation ≠ semantic approval
Compatibility ≠ semantic equivalence
Transport success ≠ identity continuity
Receipt ≠ truth
Receipt ≠ identity admission
Receipt ≠ action authority
```

## 6. Receipt taxonomy

At minimum, a future implementation profile must distinguish the existing receipt classes:

```text
DELIVERY_RECEIPT
STRUCTURAL_VALIDATION_RECEIPT
CONTINUITY_RECEIPT
```

`IDENTITY_ADMISSION_DECISION` is a **separate governed decision**, not a receipt and not a Port transport outcome.

Core law:

```text
DELIVERED
≠ STRUCTURALLY_VALID
≠ CONTINUITY_ACCEPTED
≠ TRUE
≠ IDENTITY_ADMITTED
```

Receipts are not bearer tokens for later truth, identity, consent, action, or replay authority.

## 7. Heritage boundary

Imported human, historical, literary, research, or model-derived material may cross domains only with attribution and provenance preserved.

```text
IMPORTED WISDOM ≠ IMPORTED IDENTITY
IMPORTED METHOD ≠ IDENTITY BY ORIGIN
HERITAGE TRANSPORT ≠ IDENTITY ADMISSION
OWNER STATEMENT ≠ AUTOMATIC FACT ABOUT MENTAURY
```

When a reasoning trajectory matters, reducing it to a slogan may itself be semantic loss.

## 8. Particularity ↔ Generalization boundary

Three useful levels must remain distinguishable:

```text
L1 PARTICULAR
specific person / event / testimony

        ↓ explicit scoped abstraction

L2 AGGREGATE / PATTERN
population or multi-case synthesis

        ↓ explicit scoped generalization

L3 GENERAL MODEL
broad revisable hypothesis
```

Transitions are never automatic.

```text
INDIVIDUAL TESTIMONY ≠ UNIVERSAL LAW
POPULATION PATTERN ≠ INDIVIDUAL TRUTH
MODEL OF PERSON ≠ PERSON
PERSON NARRATIVE ≠ VERIFIED INTERNAL STATE
```

Central anti-circularity law:

```text
AGGREGATE_DERIVED_FROM_SUBJECT
≠
INDEPENDENT_EVIDENCE_ABOUT_SUBJECT
```

## 9. Loss semantics

A cross-domain transfer must not silently normalize away distinctions.

Current architecture-level loss vocabulary:

```text
PRESERVED
PARTIAL
UNSUPPORTED
INDETERMINATE
LOSSY
```

`DEFERRED` and `INCOMPATIBLE` remain Port dispositions from §5; they are not additional loss values.

A declaration of loss only makes loss visible. It does not prove the loss is acceptable.

## 10. Fork / restore / migration / consent

Composition must preserve these distinctions:

```text
SHARED HISTORY ≠ SAME CURRENT IDENTITY
RECORD MERGE ≠ IDENTITY MERGE
RESTORE ≠ ERASURE OF POST-SNAPSHOT HISTORY
MIGRATION SUCCESS ≠ PROOF OF IDENTITY CONTINUITY
```

Material state that may require reconciliation includes:

- current consent / revocation status;
- commitments and relationship state;
- identity claims;
- branch provenance;
- stale receipts;
- stale authority assumptions.

## 11. Inclusion discipline

```text
ARCHITECTURAL FIT ≠ ARCHITECTURAL NECESSITY
IMPORTANT IDEA ≠ MENTAURY-KERNEL RESPONSIBILITY
```

A proposed invariant may enter only when:

1. it covers cross-domain composition;
2. a concrete semantic / authority / loss failure exists without it;
3. existing invariants do not already cover that failure;
4. the smallest necessary rule is technology-neutral;
5. it does not duplicate internal Soul or Native semantics.

## 12. Technology neutrality

The architecture intentionally avoids making any of the following canonical:

- LLMs;
- prompts;
- context windows;
- embeddings;
- vector databases;
- graph databases;
- RAG;
- specific programming languages;
- specific operating systems or devices;
- specific serialization or transport protocols.

Implementation choices may be introduced later only as explicitly scoped profiles.

## 13. Architecture gate

Current evaluation class:

`DOCUMENT_INTERNAL_CONSISTENCY_ONLY`

Current architecture may be described as ready for its bounded specification scope with declared open questions, but that is not implementation or runtime readiness.

```text
ARCHITECTURE_GATE_READY
≠ CREATE_RUNTIME_AUTHORITY
≠ PRODUCTION_AUTHORITY
```
