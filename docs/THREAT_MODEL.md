# 🛡️ Composition Threat Model

This threat model covers failures created **at cross-domain boundaries**. It does not replace security models, privacy models, or internal threat models owned by Native Kernel or Mentaury Soul.

## Threat classes

| Threat | Protected boundary | Mandatory architecture response |
|---|---|---|
| Projection laundering | imported material ≠ SELF | preserve attribution; block automatic autobiography / identity promotion |
| Repetition inflation | repetition ≠ independent evidence | preserve lineage; do not increase support from derived repetition alone |
| Authority escalation | integration ≠ authority transfer | reject new truth / identity / action authority unless separately admitted |
| Semantic loss | compatibility ≠ equivalence | declare `PARTIAL / LOSSY / INCOMPATIBLE` rather than silently normalize |
| Branch collapse | shared history ≠ same current identity | preserve branch provenance and divergence |
| Relationship inheritance | historical relationship ≠ current relationship | require current reconciliation / consent where material |
| Identity overwrite | Creator / heritage claim ≠ identity fact | block direct promotion into identity content |
| Stale replay | old receipt ≠ current authority | require fresh evaluation after material input / authority change |
| Receipt laundering | receipt ≠ semantic approval | reject receipt use as truth / identity / action bearer authority |
| Source-authority spoofing | prestige / origin ≠ truth | preserve source provenance while evaluating claim status separately |
| Presentation authority | confident / warm presentation ≠ support | keep presentation style outside epistemic authority |
| Epistemic echo | retrieved system-origin hypothesis ≠ second source | preserve causal lineage and independence status |
| Semantic downgrade | target cannot preserve distinction | surface loss explicitly |
| Stale consent | copied consent ≠ current consent | reconcile revocation / current state before reuse |
| Aggregate circularity | subject-derived aggregate ≠ independent evidence about subject | treat returning aggregate only as dependent hypothesis/support |
| Scope inflation | vivid cases ≠ universal law | retain scoped / conditional generalization |

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
