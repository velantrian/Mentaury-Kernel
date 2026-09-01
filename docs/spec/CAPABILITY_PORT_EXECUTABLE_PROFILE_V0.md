# CapabilityPort Executable Conformance Profile v0

Status: BOUNDED IMPLEMENTATION PROFILE · DRAFT
Date: 2026-08-31
Owning specification: `docs/spec/CAPABILITY_PORT_V0_1.md`

## Decision

This profile deterministically checks a concrete JSON-compatible representation of the already documented CapabilityPort v0.1 fields. It is an implementation profile, not semantic Canon.

```text
CONFORMANCE PASS != TARGET ADMISSION
CONFORMANCE PASS != CAPABILITY INVOCATION
CONFORMANCE PASS != TRUTH / IDENTITY / ACTION AUTHORITY
EXECUTABLE PROFILE != RUNTIME PORT
```

## Representation

The profile requires all v0.1 fields. Strings must be explicit and non-empty. `semantic_version` uses `MAJOR.MINOR.PATCH`. Cross-domain source and target must differ. `target_admission_required` must be exactly `true`.

`transformations` and `side_effects` are either `NONE` or a non-empty unique string list. `declared_loss` contains exactly:

- `classification` — a declared loss classification;
- `check` — how that declaration is checked.

The profile rejects embedded claims of truth, identity, action, production, admission waiver, or other authority escalation. Rejection means only that the representation is non-conforming.

## Evidence

- validator: `conformance/capability_port.py`
- executable scenarios: `tests/test_capability_port.py`
- CI: `.github/workflows/conformance.yml`

## Non-goals

No transport execution, plugin loading, target decision, evidence evaluation, cognition, identity admission, action execution, networking, storage, LLM evaluation, deployment, or production authorization.
