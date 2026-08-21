# EITI Composition Research Input

Status: **RESEARCH · COMPOSITION/CONFORMANCE ONLY · NO CENTRAL AUTHORITY**  
Recorded: 2026-08-21

EITI already implements local retrieval, association, context and learning mechanisms. Mentaury Kernel should not absorb those mechanisms as a central brain. Its relevant responsibility is to specify how typed information can cross domain boundaries without semantic loss or authority escalation.

```text
composition != cognition
transport != admission
schema compatibility != authorization
shared vocabulary != shared ownership
integration != authority transfer
```

## Relevant contract questions

### ProposalEnvelope

Can EITI/Titan transport a proposed learning or cognitive change while making `proposal_only` authority explicit and preserving producer, source, purpose, scope and target owner?

### EvidenceRef

Can evidence references preserve digest, source locator/revision, lineage/independence class, scope and resolvability without converting a reference into target-domain evidence automatically?

### CompositionEnvelope

When EITI composes Crystal evidence, Soul state and Titan retrieval context for a user-facing answer, the envelope should declare source domains, semantic roles, versioned transformations and any known loss.

### Admission protocol

Mentaury Kernel may specify conformance for `AdmissionRequest`, `CapabilityLease`, `AdmissionDecision` and `ConsumptionReceipt`, but the target domain remains the authority that decides ALLOW/DENY for its own state.

## Conformance invariants

- unknown or unsupported semantic fields fail closed when authority could change;
- transport cannot silently promote `claim -> belief`, `retrieval candidate -> evidence`, or `proposal -> approved change`;
- provenance is preserved across composition;
- declared lossy transforms cannot masquerade as lossless;
- capability scope/audience/operation cannot inflate during translation;
- a contract version bump alone never grants new admission rights;
- Mentaury Kernel does not become an always-online sovereign service.

## EITI-specific role

EITI is a useful client/reference producer and consumer of envelopes. Its working mechanisms provide test vectors for composition, but EITI implementation details remain EITI-owned and do not become Mentaury Kernel Canon by inheritance.
