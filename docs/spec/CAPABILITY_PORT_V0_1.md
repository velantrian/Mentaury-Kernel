# Cross-Domain Capability Port v0.1

Status: SPECIFICATION DRAFT
Date: 2026-08-24

## Purpose

Mentaury Kernel defines how capabilities may be described when they cross domain boundaries without transferring semantic ownership or authority.

Operational plugin/capability systems such as OpenClaw motivate this contract, but no vendor/runtime-specific manifest becomes the canonical form.

## CapabilityPort

A conforming port SHOULD declare:

- `port_id`;
- `semantic_version`;
- `source_domain`;
- `target_domain`;
- `capability_name`;
- `capability_owner`;
- `transport` or transport-neutral interface identifier;
- `input_contract`;
- `output_contract`;
- `provenance_contract`;
- `transformations`;
- `declared_loss`;
- `side_effects`;
- `target_admission_required`;
- `compatibility_constraints`;
- `revocation_semantics`.

## Invariants

`composition != cognition`

`integration != authority transfer`

`transport success != semantic approval`

`delivered != true != identity-admitted`

`capability owner != transport host`

A Titan-hosted transport, for example, does not make Titan the semantic owner of a Crystal, Soul, Continuum, or Native capability.

## Target admission

A port may deliver a request or artifact to another domain. Delivery alone MUST NOT imply acceptance by the target domain.

The target domain keeps its own admission and governance rules. A port can declare that admission is required; it cannot grant that admission on the target's behalf.

## Declared loss

Any transformation that can discard, summarize, compress, normalize, or reinterpret information MUST declare expected loss or explicitly state that no loss is intended and how that claim is checked.

## Capability manifest relation

Runtime manifests may be projected into this contract for conformance checks, but runtime-specific fields remain implementation metadata. The cross-domain contract should retain only semantics needed to preserve ownership, compatibility, provenance, loss, and admission boundaries.

## Non-goals

This specification does not provide:

- runtime execution;
- cognition;
- truth validation;
- identity admission;
- autonomous action authority;
- a plugin loader;
- a marketplace;
- a scheduler.

It is a composition/conformance contract only.
