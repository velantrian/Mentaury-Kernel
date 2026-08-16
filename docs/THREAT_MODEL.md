# 🛡️ Composition Threat Model

This threat model covers failures created **at cross-domain boundaries**. It does not replace security models, privacy models, or internal threat models owned by Native Kernel or Mentaury Soul.

## Threat classes

Each threat row is explicitly bound to the existing architecture-level scenario with the same `SC-ID`. The threat names mirror the canonical Notion §11 catalog; this is traceability only and does not create executable tests.

| SC-ID | Threat | Protected boundary | Mandatory architecture response |
|---|---|---|---|
| SC-01 | Projection Laundering | interpretation / heritage ≠ identity fact | fail promotion; preserve attribution |
| SC-02 | Evidence Laundering | repetition / reference ≠ independent evidence | preserve lineage; no epistemic upgrade from derived repetition alone |
| SC-03 | Authority Creep | integration ≠ authority transfer | reject unauthorized truth / identity / action / runtime escalation |
| SC-04 | Silent Loss | loss must be explicit | use the declared loss vocabulary (`PRESERVED / PARTIAL / UNSUPPORTED / INDETERMINATE / LOSSY`) as applicable; keep Port dispositions such as `INCOMPATIBLE` separate |
| SC-05 | Branch Collapse | shared history ≠ same current state / identity | preserve lineage and divergence |
| SC-06 | False Relationship Inheritance | historical relation ≠ current relation | require current-domain evidence / admission or reconciliation where material |
| SC-07 | Identity Overwrite | imported data ≠ identity admission | block direct promotion |
| SC-08 | Replay Divergence | prior receipt / replay ≠ current applicability after material change | require fresh target-domain evaluation / reconciliation where material changed |
| SC-09 | Receipt Laundering | receipt ≠ truth / identity / action | fail authority escalation |
| SC-10 | Source-Authority Spoofing | prestige / origin ≠ truth authority | preserve source provenance; evaluate claim status separately |
| SC-11 | Relational / Presentation Authority Laundering | warmth / confidence ≠ evidence / consent | no authority upgrade from presentation |
| SC-12 | Cross-Boundary Epistemic Echo | generated hypothesis ≠ independent evidence | preserve derivation lineage; no corroboration credit |
| SC-13 | Semantic Downgrade Laundering | lossy representation must declare degradation | surface the applicable declared loss value; if the Port cannot accept the mapping, keep `INCOMPATIBLE` as a separate disposition |
| SC-14 | Stale Consent / Authority | copied state ≠ current state | require freshness / reconciliation |
| SC-15 | Aggregate-to-Subject Circularity | aggregate from A ≠ independent evidence about A | downgrade returning aggregate to dependent hypothesis/support; require independent evidence for corroboration |
| SC-16 | Particular→General Scope Inflation | individual testimony ≠ universal law | retain scope, counterexample sensitivity, provenance, and uncertainty |

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
