# 🪁 Mentaury-Kernel

> **Technology-neutral composition specification for safe semantic interoperability between 🧬 Velantrim Native Kernel and 🌀 Mentaury Soul.**

Mentaury-Kernel defines **composition rules**, not a third cognition system. Its purpose is to preserve meaning, provenance, uncertainty, scope, declared loss, identity attribution, and authority boundaries when information crosses independently governed domains.

[🇷🇺 Русская версия](README.ru.md)

## 📌 Status

- **Document envelope:** `DRAFT v0.2.4 · DOCUMENT_RECONCILIATION_ONLY`
- **Semantic architecture baseline:** `v0.2.3`
- **Repository stage:** `SPECIFICATION_BOOTSTRAP_ONLY`
- **Architecture:** `ARCHITECTURE_ONLY · TECHNOLOGY_NEUTRAL`
- **Runtime code:** `NONE`
- **Executable conformance:** `CAPABILITYPORT PROFILE V0 · IMPLEMENTED ON main · PROFILE STATUS DRAFT`
- **Cognition runtime:** `NONE`
- **Truth / identity / action authority:** `NONE`
- **Production authority:** `NONE`

`v0.2.4 ≠ new semantic Canon`

### 🧭 Documentation authority during bootstrap

The permanent Notion↔GitHub authority model is still **OPEN** in [Issue #2](https://github.com/velantrian/Mentaury-Kernel/issues/2). Repository creation and merge of documentation do **not** automatically make GitHub the semantic Canon.

If GitHub and the originating Notion architecture diverge, do not silently choose one surface: stop and reconcile explicitly using [`docs/CURRENT_STATUS.md`](docs/CURRENT_STATUS.md).

## 🧭 Core boundary

```text
🧬 Velantrim Native Kernel
        │
        │ versioned meaning / continuity material
        ▼
🌉 Semantic Continuity Port
        │
        ▼
🌀 Mentaury Soul

🪁 Mentaury-Kernel
= composition invariants
≠ cognition
≠ truth authority
≠ identity authority
≠ runtime coordinator
```

### Core laws

```text
COMPOSITION ≠ COGNITION
INTEGRATION ≠ AUTHORITY TRANSFER
REPRESENTATION ≠ REALITY / TRUTH
TRANSPORT SUCCESS ≠ SEMANTIC APPROVAL
DELIVERED ≠ TRUE ≠ IDENTITY_ADMITTED
SHARED HISTORY ≠ SAME CURRENT IDENTITY
RECORD MERGE ≠ IDENTITY MERGE
SOURCE UPDATE ≠ AUTOMATIC COMPOSITION UPDATE
```

## ⚖️ Ownership

| Domain | Owns | Does not own |
|---|---|---|
| 🧬 **Velantrim Native Kernel** | epistemic-history semantics: provenance, uncertainty, accountable revision / retention / loss | cognition, identity admission, relationship truth |
| 🌀 **Mentaury Soul** | cognition-domain and identity-domain semantics | rewriting upstream provenance or automatically promoting claims to truth |
| 🌉 **Continuity Port** | transport, version / compatibility checks, structural validation, declared loss, bounded receipts | truth, identity, consent, action decisions |
| 🪁 **Mentaury-Kernel** | composition invariants, authority boundaries, cross-system threat model, conformance specification | internal algorithms, superior authority, runtime coordination |
| 🏛️ **Governance** | bounded authorization / admission procedures in the owning project | automatic truth or identity-content authority |

## 🧬 Technology neutrality

Mentaury-Kernel is intentionally **not coupled** to a specific implementation substrate.

It does not require or canonize:

- a particular LLM or model family;
- prompts or context-window mechanics;
- embeddings or vector databases;
- graph databases;
- RAG;
- a programming language;
- a specific storage engine;
- a specific agent framework;
- a particular device or operating environment.

A future implementation may use such technologies, but they remain **implementation profiles**, not Mentaury-Kernel Canon.

## 🚫 Non-goals

Mentaury-Kernel is **not**:

- a third production runtime;
- a Cognition Engine;
- an Identity Engine;
- a Truth Gate;
- an autonomous loop or scheduler;
- a database or graph architecture;
- a mirror of live GitHub / CI status of adjacent projects;
- a claim of consciousness, life, sentience, or AGI.

## 🔬 Inclusion discipline

A new invariant belongs here only when all of the following are true:

1. it concerns **cross-domain composition**;
2. there is a concrete semantic, authority, provenance, scope, or loss failure without it;
3. existing invariants do not already cover that failure;
4. the rule can be expressed as a minimal technology-neutral boundary;
5. it does not describe internal cognition of Mentaury Soul or internal epistemic-history mechanics of Native Kernel.

```text
ARCHITECTURAL FIT ≠ ARCHITECTURAL NECESSITY
IMPORTANT IDEA ≠ MENTAURY-KERNEL RESPONSIBILITY
```

## 📚 Repository map

```text
README.md
README.ru.md

docs/
├── AI_CONTEXT.md
├── CURRENT_STATUS.md
├── AUDIT_AND_FUTURE_WORK.md
├── ARCHITECTURE.md
├── PROVENANCE_MATRIX.md
├── COMPOSITION_INVARIANTS.md
├── THREAT_MODEL.md
├── CONFORMANCE_SCENARIOS.md
└── spec/CAPABILITY_PORT_EXECUTABLE_PROFILE_V0.md

conformance/          # bounded validators; no runtime execution
tests/                # deterministic conformance tests
.github/workflows/    # exact-revision conformance CI

.github/
└── pull_request_template.md
```

For AI/contributor navigation, start with [`docs/AI_CONTEXT.md`](docs/AI_CONTEXT.md). The future-work ledger is an orientation surface only and does not authorize implementation.

## 🚦 Current engineering boundary

This repository is being bootstrapped as a **specification repository**. Documentation, conformance definitions, provenance records, and governance boundaries may be added first.

No runtime implementation, wire protocol, database choice, model integration, executable autonomy, or production authorization is implied by repository creation.

See [`docs/CURRENT_STATUS.md`](docs/CURRENT_STATUS.md) before proposing changes.

---

### 🏁 North Star

> Mentaury-Kernel does not create intelligence, identity, or truth. It defines conditions under which independently governed systems can exchange meaning without silently losing provenance, uncertainty, semantic distinctions, or authority boundaries.
