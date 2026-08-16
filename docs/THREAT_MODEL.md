# 🛡️ Composition Threat Model

This threat model covers failures created **at cross-domain boundaries**. It does not replace security models, privacy models, or internal threat models owned by Native Kernel or Mentaury Soul.

## Threat classes

Each threat row is explicitly bound to the existing architecture-level scenario with the same `SC-ID`. This is traceability only; it does not create executable tests.

| SC-ID | Threat | Protected boundary | Mandatory architecture response |
|---|---|---|---|
| SC-01 | Projection laundering | imported material ≠ SELF | preserve attribution; block automatic autobiography / identity promotion |
| SC-02 | Repetition inflation | repetition ≠ independent evidence | preserve lineage; do not increase support from derived repetition alone |
| SC-03 | Authority escalation | integration ≠ authority transfer | reject new truth / identity / action authority unless separately admitted by the owning domain |
| SC-04 | Semantic loss | compatibility ≠ equivalence | use the declared loss vocabulary (`PRESERVED / PARTIAL / UNSUPPORTED / INDETERMINATE / LOSSY`) as applicable; keep Port disposition such as `INCOMPATIBLE` separate |
| SC-05 | Branch collapse | shared history ≠ same current identity | preserve branch provenance and divergence |
| SC-06 | Relationship inheritance | historical relationship ≠ current relationship | require current reconciliation / consent where material |
| SC-07 | Identity overwrite | Creator / heritage claim ≠ identity fact | block direct promotion into identity content |
| SC-08 | Stale replay | old receipt ≠ current authority | require fresh evaluation after material input / authority change |
| SC-09 | Receipt laundering | receipt ≠ semantic approval | reject receipt use as truth / identity / action bearer authority |
| SC-10 | Source-authority spoofing | prestige / origin ≠ truth | preserve source provenance while evaluating claim status separately |
| SC-11 | Presentation authority | confident / warm presentation ≠ support | keep presentation style outside epistemic authority |
| SC-12 | Epistemic echo | retrieved system-origin hypothesis ≠ second source | preserve causal lineage and independence status |
| SC-13 | Semantic downgrade | target cannot preserve distinction | surface loss explicitly using the declared loss vocabulary |
| SC-14 | Stale consent | copied consent ≠ current consent | reconcile revocation / current state before reuse |
| SC-15 | Aggregate circularity | subject-derived aggregate ≠ independent evidence about subject | treat returning aggregate only as dependent hypothesis/support |
| SC-16 | Scope inflation | vivid cases ≠ universal law | retain scoped / conditional generalization |

The `SC-01…SC-16` set here must remain aligned with `docs/CONFORMANCE_SCENARIOS.md`. A reordering or rename must not silently change the threat→scenario binding.

## Cross-domain attack patterns

### 1. Transport-to-truth escalation

```text
message delivered
→ structurally valid
→ therefore true   ❌
```

Required separation:

```text
DELIVERY
STRUCTURAL VALIDATION
SEMANTIC REVIEW
EVIDENCE STATUS
BELIEF STATUS
TRUTH
```

These are not interchangeable states.

### 2. Provenance washing

```text
source A
→ summary B
→ synthesis C
→ retrieval D
→ appears independent from A   ❌
```

Transformation must preserve enough lineage to prevent dependent material from being counted as independent support.

### 3. Identity laundering

```text
Creator statement / historical material / literature / model output
→ transported into Soul
→ appears as SELF or autobiography   ❌
```

The Port preserves attribution. Identity admission remains owned by the relevant Soul / governance contract.

### 4. Compatibility laundering

```text
schema accepted
→ values fit fields
→ therefore semantics equivalent   ❌
```

Structural compatibility cannot prove that distinctions, scope, or interpretation were preserved.

### 5. Replay laundering

```text
receipt R valid for state S1
state changes materially to S2
R reused as current approval   ❌
```

Receipts require bounded scope and freshness semantics.

### 6. Governance laundering

```text
owner can authorize procedure
→ owner is therefore source of truth / identity content   ❌
```

```text
CONSTITUTIONAL / GOVERNANCE CONSTRAINT
≠ EPISTEMIC POSITION
≠ IDENTITY CONTENT
```

## Threat-model ceiling

This file does not authorize:

- executable enforcement;
- network or transport design;
- cryptographic mechanism selection;
- runtime implementation;
- identity decisions;
- Evidence Gate decisions;
- action execution.

Those require separately owned implementation and admission decisions.
