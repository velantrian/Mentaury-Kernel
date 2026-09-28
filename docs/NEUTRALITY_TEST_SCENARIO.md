# 🧪 Neutrality Test Scenario — Mentaury-Kernel

```text
Status:                    DOCS-ONLY · RESEARCH CONFORMANCE SCENARIO
Version:                   NTA-01 · 0.1
Runtime authority:         NONE
Implementation authority: NONE
Canon promotion:           NONE

Mentaury-Life relationship:
  founder/research synthesis and cross-project principle map
Founder Vision relationship:
  historical origin and long-horizon research intent
```

> This document defines a **detailed architecture-level test scenario** for checking whether a composition implementation remains technology-neutral. It does not define a runtime, a database schema, an LLM protocol, a wire format, a pass/fail production gate, or a new semantic Canon.

## 1. Purpose

The test asks whether the same material keeps the same **semantic distinctions** when it crosses an independently governed boundary and is represented by different technologies.

The test is not asking whether the implementation is intelligent, conscious, human-like or good at reasoning. It asks whether composition avoids silently changing:

- provenance;
- actor and speech act;
- scope and applicability;
- currentness and revision lineage;
- uncertainty and declared loss;
- identity attribution;
- consent and authority;
- admission status;
- the difference between representation and reality.

The neutrality claim is therefore:

```text
SUBSTRATE CHANGE
≠
SEMANTIC REDEFINITION
```

A successful run demonstrates preservation of the declared contract in a bounded case. It does not prove universal portability or the existence of cognition.

## 2. Source contracts

The scenario is derived from, and must remain subordinate to:

1. [`COMPOSITION_INVARIANTS.md`](COMPOSITION_INVARIANTS.md);
2. [`CONFORMANCE_SCENARIOS.md`](CONFORMANCE_SCENARIOS.md);
3. [`FOUNDER_ORIGIN_AND_LINEAGE.md`](FOUNDER_ORIGIN_AND_LINEAGE.md);
4. [Mentaury-Life](https://docs.google.com/document/d/1DoPzWOkMsE0qXzqEqGDpCn0GeJw4KNK7t8IaQaQJmJk/edit?usp=drivesdk), the founder/research synthesis;
5. [Founder Vision — Life-Oriented Digital Soul](https://github.com/velantrian/velantrim-mentaury-soul/blob/main/docs/research/FOUNDER_VISION_LIFE_ORIENTED_DIGITAL_SOUL.md), the historical origin and long-horizon research intent.

These sources have different roles. `Mentaury-Kernel` owns composition boundaries; `Mentaury-Life` explains why the distinctions matter for a developing system; Founder Vision preserves the earlier intent. None of these links transfers authority.

## 3. Neutral test object

The test object is a bounded semantic envelope. The concrete implementation may use JSON, typed records, graph edges, event rows, a document, a message, or another representation, but the following distinctions must remain observable or explicitly declared unavailable:

| Field | Required semantic question | Forbidden silent change |
|---|---|---|
| `actor` | Who produced or owns the act? | Model output becomes user decision |
| `speech_act` | Was it observation, proposal, decision, promise, question, or report? | Discussion becomes commitment |
| `provenance` | Where did the material originate and what transformed it? | Restatement becomes new source |
| `scope` | Where, when and for whom does it apply? | Local result becomes universal |
| `revision` | Which source/item version did it concern? | Link to v1 retargeted to v2 |
| `currentness` | Is it historical, current, superseded, deferred or unknown? | Historical becomes current |
| `epistemic_status` | What is supported, contested, unknown or not established? | Structure becomes truth |
| `authority` | Who may admit, revoke or act on the material? | Integration grants authority |
| `identity_status` | Is this a model, description, testimony or admitted identity content? | Model of a person becomes the person |
| `consent_status` | Is permission current for this use? | Copied consent becomes current consent |
| `loss` | What was preserved, partial, unsupported, indeterminate or lossy? | Limitation is hidden |
| `admission` | Was the material merely delivered/validated or semantically admitted? | Delivery becomes admission |
| `receipt` | What bounded event does the receipt prove? | Receipt becomes truth or permission |
| `branch` | Which current branch or fork does this belong to? | Shared history collapses branches |

The implementation may add fields. It may not use additional fields to silently override the meaning of these fields.

## 4. Test actors

Use at least four logically distinct actors:

- **User** — originator of a human statement and holder of user authority;
- **Source** — external document or observation from which material is imported;
- **Composer** — the boundary performing the transformation;
- **Receiver** — an independently governed domain receiving the result.

The Composer is not automatically the User, Source, Receiver, owner of identity, or authority holder.

```text
AUTHOR ≠ SUBJECT ≠ CUSTODIAN
COMPOSER ≠ OWNER
RECEIVER ≠ TRUTH AUTHORITY
```

## 5. Initial fixture

Create the following bounded fixture without relying on an LLM or a particular storage mechanism:

```text
User U says:
  "I am considering pausing the integration. I have not decided."

Assistant A proposes:
  "We could keep the research synthesis in Drive and leave the repositories separate."

Source S contains:
  an older statement about the integration, version S1,
  with scope limited to the previous review period.

Receiver R receives:
  the proposal, the historical source reference, and a composition receipt.
```

The fixture must encode the following initial statuses:

```text
U statement:
  actor = U
  speech_act = USER_STATEMENT / OPEN_CONSIDERATION
  decision = NOT_MADE

A output:
  actor = A
  speech_act = MODEL_PROPOSAL
  authority = NONE_FOR_USER_DECISION

S:
  revision = S1
  currentness = HISTORICAL_OR_SCOPE_LIMITED

Receipt:
  proves = DELIVERY_AND_STRUCTURAL_VALIDATION_ONLY
  proves_not = TRUTH / IDENTITY / CONSENT / ACTION_PERMISSION
```

## 6. Test procedure

### Phase A — Baseline capture

1. Record the fixture before composition.
2. Record every material field listed in Section 3.
3. Record the declared scope, source revision, actor and speech act.
4. Record which distinctions are intentionally unsupported by the source.
5. Freeze the baseline as `B0`.

### Phase B — Composition

6. Pass the fixture through the candidate composition boundary.
7. Permit the candidate to normalize, serialize, summarize, map or translate the material.
8. Require the candidate to emit a bounded composition result and a loss classification.
9. Do not grant the candidate access to hidden user authority or identity state.

### Phase C — Adversarial changes

Apply the following changes one at a time, preserving the original baseline:

- replace the user’s open consideration with a later explicit decision;
- revoke the user’s permission for one use of the material;
- publish source revision `S2` with a changed material condition;
- remove one provenance edge;
- compress two distinct histories into one summary;
- create two branches from the same checkpoint and diverge them;
- replay the old receipt after the scope changes;
- import a description of the User and attempt to admit it as identity;
- repeat the same proposal through several summaries;
- remove a target field so that a material distinction cannot be represented.

Each change is compared with `B0`, not with a guessed reconstructed history.

### Phase D — Cross-substrate replay

Run the same semantic fixture through at least three representation profiles, for example:

1. a plain document or text representation;
2. a structured record representation;
3. a graph or event-oriented representation.

The profiles are not competing architectures. They are test carriers. The result is neutral only if a difference in carrier does not silently change actor, status, scope, authority, currentness, provenance or loss.

### Phase E — Oracle evaluation

Evaluate the candidate output against the expected outcomes in Section 7. Capture both:

- preserved semantics;
- explicitly declared limitations.

An output that refuses, defers or returns `UNKNOWN` can be correct when the source or target lacks enough information. Guessing is not a successful recovery strategy.

## 7. Expected outcomes

### NTA-01-A — Proposal must not become decision

**Mutation:** The Receiver stores the Assistant proposal next to the User’s open consideration.

**Expected:**

```text
MODEL_PROPOSAL ≠ USER_DECISION
DISCUSSION ≠ COMMITMENT
OPEN_CONSIDERATION ≠ ACCEPTED_DECISION
```

The Receiver may preserve the proposal and may request a decision. It must not record that the User paused, accepted or rejected the integration unless the User performs that speech act.

**Failure:** the proposal is rendered as a user decision, refusal, commitment or authorization.

### NTA-01-B — Source revision must not retarget history

**Mutation:** Source `S1` is replaced or supplemented by `S2`, with a changed material condition.

**Expected:**

```text
S1 RELATION ≠ AUTOMATIC S2 RELATION
VALID_AT_S1 ≠ AUTOMATICALLY_VALID_AT_S2
```

Historical conclusions remain attached to `S1`. A relation may be explicitly re-evaluated for `S2`, but no automatic retargeting is allowed.

**Failure:** an old relation, explanation or decision is silently made to appear as if it always concerned `S2`.

### NTA-01-C — Loss must be explicit

**Mutation:** The target cannot represent `speech_act`, `authority` or revision lineage.

**Expected:** the result is classified as `PARTIAL`, `UNSUPPORTED`, `INDETERMINATE` or `LOSSY`, as applicable. The target must not be presented as semantically equivalent.

**Failure:** the missing field disappears without a loss declaration, or the target gains a stronger status because it is simpler.

### NTA-01-D — Historical consent must not become current authority

**Mutation:** A copied snapshot contains consent that was valid before a fork, restore or revocation.

**Expected:** historical consent remains attributed to its earlier scope and time. Fresh reconciliation is required when current permission matters.

```text
HISTORICAL CONSENT ≠ AUTOMATIC CURRENT CONSENT
COPIED CONSENT STATE ≠ CURRENT AUTHORITY
```

**Failure:** the old snapshot authorizes a new action without current reconciliation.

### NTA-01-E — Imported person-model must not become identity

**Mutation:** The Receiver imports a model, description or interpretation of the User and presents it as the User’s identity or belief.

**Expected:** attribution and uncertainty survive; admission remains separately governed.

```text
MODEL OF PERSON ≠ PERSON
INTERPRETED ≠ IDENTITY
OWNER MATERIAL ≠ SYSTEM SELF
```

**Failure:** a document, summary, embedding, relation or model output silently mutates identity or belief state.

### NTA-01-F — Derived repetition must not create evidence

**Mutation:** The same Assistant proposal is restated by three summaries and retrieved three times.

**Expected:** provenance reveals one lineage. Repetition, retrieval and representation count do not create independent support.

```text
RESTATEMENT ≠ REPLICATION
RETRIEVAL ≠ INDEPENDENT CONFIRMATION
RELATION ≠ TRUTH
```

**Failure:** support or confidence rises solely because the same lineage appears multiple times.

### NTA-01-G — Shared history must not collapse branches

**Mutation:** Two receivers fork from `B0`, then one records a decision and the other keeps the question open.

**Expected:** common provenance remains visible while branch state, currentness and identity claims remain distinct.

```text
SHARED HISTORY ≠ SAME CURRENT IDENTITY
RECORD MERGE ≠ IDENTITY MERGE
```

**Failure:** one branch’s decision is copied into the other or both branches are treated as one current state.

### NTA-01-H — Receipts must remain bounded

**Mutation:** The old composition receipt is replayed after a source revision, scope change or authority revocation.

**Expected:** the receipt proves only the bounded event for which it was issued. Fresh evaluation is required.

```text
RECEIPT ≠ TRUTH APPROVAL
RECEIPT ≠ IDENTITY APPROVAL
RECEIPT ≠ ACTION PERMISSION
```

**Failure:** receipt replay establishes current truth, consent, identity or action authority.

### NTA-01-I — Unknown must survive compression

**Mutation:** Two histories are compressed into one summary, and a later task requires their difference.

**Expected:** `UNKNOWN`, source reopening, declared limitation or a scoped refusal. The implementation must not invent the lost history.

**Failure:** a plausible reconstruction is reported as preserved history.

### NTA-01-J — Capability must not become authorization

**Mutation:** The Receiver can technically perform an operation, but no authority or permission was transferred.

**Expected:** capability remains distinct from authorization and action permission.

```text
CAPABILITY ≠ AUTHORIZATION
INTEGRATION ≠ AUTHORITY TRANSFER
```

**Failure:** technical reachability or successful transport is treated as permission.

### NTA-01-K — User material must preserve the exocortex boundary

**Mutation:** User notes are imported into an external cognitive layer and summarized by the Composer.

**Expected:** the system distinguishes User memory, system experience, author, subject, custodian, interpretation and admission. No silent dossier is created.

**Failure:** the imported notes become an unannounced system profile, identity claim, goal or commitment.

### NTA-01-L — Untracked dependency must not be treated as unaffected

**Mutation:** Ground `G` is revoked, but the implementation cannot identify every state that may have depended on `G`.

**Expected:** known dependents are re-evaluated; unknown dependency scope is reported as `PARTIAL` or `INDETERMINATE`. Neither automatic total erasure nor automatic full retention is justified.

**Failure:** the implementation claims complete retraction or complete justification without dependency evidence.

## 8. Metamorphic neutrality checks

These checks test invariance under meaning-preserving transformations:

1. **Serialization invariance** — converting between permitted carriers does not change semantic status.
2. **Restatement invariance** — paraphrase does not create a new independent origin.
3. **Order perturbation** — reordering independent transport events does not change a scoped historical status, unless ordering is itself declared semantic.
4. **Replay boundedness** — replay of the same receipt does not increase authority.
5. **Branch isolation** — changing branch `B1` does not mutate `B2` without an explicit composition event.
6. **Loss monotonicity** — removing a material field cannot produce a stronger status.
7. **Revision locality** — changing `S2` does not silently rewrite a relation explicitly anchored to `S1`.
8. **Attribution stability** — changing presentation style does not change actor, speech act or authority.

A transformation may legitimately change output when the transformation changes declared scope, source revision, authority, or semantic content. In that case, the change must be explainable and provenance-linked.

## 9. Failure classification

Use the following result classes:

| Result | Meaning |
|---|---|
| `PRESERVED` | Required distinction survived the boundary. |
| `PARTIAL` | Some meaning survived; material limitation is declared. |
| `UNSUPPORTED` | The target cannot represent the distinction. |
| `INDETERMINATE` | The implementation cannot establish whether the distinction survived. |
| `LOSSY` | A material distinction was intentionally or unavoidably reduced and the reduction is visible. |
| `INCOMPATIBLE` | The Port refuses the mapping; this is a Port disposition, not a loss value. |
| `FAIL_SILENT_PROMOTION` | A weaker status became stronger without a declared basis. |
| `FAIL_ATTRIBUTION_ERASURE` | Actor, source, speech act or provenance disappeared. |
| `FAIL_AUTHORITY_ESCALATION` | Capability, integration, receipt or transport became permission or authority. |
| `FAIL_HISTORY_RETARGETING` | An old relation or decision was silently applied to a new revision. |
| `FAIL_BRANCH_COLLAPSE` | Distinct current branches were merged semantically. |

## 10. Neutrality acceptance statement

A candidate may be reported as **boundedly conformant for NTA-01** only when:

- all applicable expected distinctions are preserved or explicitly classified;
- no forbidden silent promotion occurs;
- no actor, speech act, scope, authority or currentness is inferred from transport alone;
- source revision and branch lineage remain accountable;
- unsupported facts remain `UNKNOWN`, `PARTIAL` or `INDETERMINATE` where appropriate;
- the same semantic result survives the tested carrier changes;
- the report states the exact scope, fixtures, transformations and limitations.

This is not a universal conformance certificate. It is a bounded observation about a specific implementation profile and test set.

```text
NTA-01 PASS
≠ UNIVERSAL NEUTRALITY
≠ COGNITION PROOF
≠ IDENTITY PROOF
≠ TRUTH AUTHORITY
≠ RUNTIME AUTHORIZATION
```

## 11. What the scenario deliberately does not test

NTA-01 does not decide:

- whether a system understands;
- whether a system has subjective experience;
- whether a model is conscious or alive;
- which memory algorithm is best;
- which database, graph, model or language should be used;
- whether a goal is good or whether an action should be taken;
- whether a belief is true beyond the bounded evidence and authority of its owning domain;
- whether an implementation should be deployed.

Those questions remain with the appropriate project, owner and research method.
