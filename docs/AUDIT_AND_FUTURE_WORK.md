# 🧭 Mentaury-Kernel — Audit & Future Work Ledger

> **Orientation and future-work surface only. This document does not authorize implementation.**

```text
future-work entry != implementation authorization
priority != authorization
research finding != runtime capability
candidate != selected milestone
open issue != permission to implement
architecture idea != authority inheritance
repository existence != semantic Canon authority
```

This ledger records what is known, what remains unresolved, what must be re-audited, and what is explicitly not authorized. It is designed so a future AI or contributor can resume safely without depending on old chat context.

---

## 0. How AI must use this document

Before selecting any work:

1. Resolve the live GitHub repository state.
2. Read `docs/CURRENT_STATUS.md`.
3. Check open PRs and Issues.
4. Check whether Notion and GitHub require explicit reconciliation.
5. Read this ledger.
6. Read the relevant architecture/provenance/invariant documents.
7. Reverify affected Native Kernel / Mentaury Soul semantic pins when the proposed work depends on them.
8. Select **no implementation** unless a separate bounded authorization exists.

```text
DO NOT AUTO-SELECT NEXT MILESTONE
```

A future-work entry may be important or high priority and still remain unselected and unauthorized.

---

## 1. Future-work state vocabulary

The values below are **ledger-only control-plane states**.

```text
FW_OPEN
FW_INVESTIGATE
FW_CANDIDATE
FW_DEFERRED
FW_BLOCKED
FW_NOT_AUTHORIZED
FW_DONE
FW_STALE
FW_NEEDS_REPRODUCTION
FW_NEEDS_ARCHITECTURE_DECISION
```

They are intentionally namespaced.

```text
FW_STATE
!= Normative Provenance Matrix status
!= semantic authority
!= implementation authorization
```

The closed Canon/provenance status vocabulary remains separately defined in `docs/PROVENANCE_MATRIX.md`.

### Priority vocabulary

```text
P0 = existential / safety / corruption risk
P1 = important architecture / governance
P2 = useful capability / research / maintainability
P3 = optional / maintenance
```

```text
P0 / P1 / P2 / P3 != authorization
```

---

## 2. Current stop boundary

Current repository stage:

```text
SPECIFICATION_BOOTSTRAP_ONLY
semantic architecture baseline = v0.2.3
document/routing envelope      = v0.2.4
runtime                         = NONE
cognition runtime               = NONE
truth authority                 = NONE
identity authority              = NONE
action authority                = NONE
production authority            = NONE
```

Do not introduce without a separate explicit bounded decision:

- runtime code;
- executable autonomous loops;
- a concrete Port/wire protocol as semantic Canon;
- database / graph / vector-store / LLM dependencies as semantic Canon;
- identity or truth adjudication;
- action authority;
- production/deployment authorization;
- a new owner above Native Kernel or Mentaury Soul;
- a permanent Notion↔GitHub semantic-authority model.

---

## 3. Current stable checkpoint — fresh audit 2026-08-16

Fresh live audit basis:

| Surface | Observed state |
|---|---|
| Repository | `velantrian/Mentaury-Kernel` · public |
| Default branch | `main` |
| Audited main SHA | `2b46aedda823ae5eea55db8e43374392dc0f5dbe` |
| Main signature | `VERIFIED · VALID` |
| Open PRs at audit | `0` |
| Open Issues at audit | `1` — Issue `#2` |
| GitHub Actions workflows | `0` |
| Branch protection on `main` | `disabled` at audit |
| Runtime/source tree | no `src/`, runtime package, executable test suite, or implementation code present |
| AI router | `docs/AI_CONTEXT.md` |
| Repository status surface | `docs/CURRENT_STATUS.md` |
| Notion status | originating architecture surface remains marked `NOTION-FIRST`; permanent authority model unresolved |

Historical bootstrap evidence retained by `docs/CURRENT_STATUS.md`:

- bootstrap PR `#1` merged as `ea3b7fd33ed4aa85806ccff2b1a061360c8530af`;
- post-merge status PR `#3` merged as current audited main `2b46aedda823ae5eea55db8e43374392dc0f5dbe`;
- independent human review is **not claimed**.

### Current documentation-authority boundary

The permanent Notion↔GitHub authority model is unresolved in Issue `#2`.

```text
REPOSITORY EXISTS
!= GITHUB AUTOMATICALLY BECOMES SEMANTIC CANON

GITHUB / NOTION DIVERGENCE
-> DO NOT SILENTLY CHOOSE
-> RECONCILE EXPLICITLY
```

GitHub is authoritative for GitHub facts such as repository contents, commits, Issues, PRs, and repository configuration. It does not automatically acquire semantic ownership over the originating Notion architecture merely by existing.

---

## 4. Concrete open work

### MK-FW-001 — Permanent Notion ↔ GitHub semantic-authority model

**FW_STATE:** `FW_NEEDS_ARCHITECTURE_DECISION`  
**Priority:** `P1`  
**Implementation authorized:** `NO`  
**Semantic Canon change authorized:** `NO`  
**Runtime capability change:** `NO`  
**Owner domain:** `Governance / repository Owner`  
**Tracking:** GitHub Issue `#2`  
**Last verified:** `2026-08-16`

#### Question
What permanent authority and conflict-resolution model should govern the originating Notion architecture and the GitHub specification package?

#### Why it matters
Without an explicit model, a future contributor may silently promote GitHub to semantic Canon or silently overwrite reviewed repository material from Notion.

#### Existing evidence
`docs/AI_CONTEXT.md`, `docs/CURRENT_STATUS.md`, Notion Mentaury-Kernel status, and Issue `#2` all preserve the temporary non-automatic-authority boundary.

#### Required audit
Re-read both current surfaces and identify which artifact classes need ownership: semantic law, current repository status, research notes, historical provenance, implementation profiles.

#### Preconditions
Explicit Owner/governance decision.

#### Non-goals
No runtime, Port, cognition, identity, truth, or action authority change.

#### Authority boundaries
A documentation-authority decision must not become authority over Native Kernel or Mentaury Soul semantics.

#### Exit criteria
A precise conflict-resolution and artifact-ownership rule is explicitly approved and reconciled on both surfaces.

#### Possible outcomes
`FW_DONE`, `FW_NEEDS_ARCHITECTURE_DECISION`, `FW_DEFERRED`.

---

### MK-FW-002 — Repository license

**FW_STATE:** `FW_NEEDS_ARCHITECTURE_DECISION`  
**Priority:** `P1`  
**Implementation authorized:** `NO`  
**Semantic Canon change authorized:** `NO`  
**Runtime capability change:** `NO`  
**Owner domain:** `Governance / repository Owner`  
**Tracking:** GitHub Issue `#2`  
**Last verified:** `2026-08-16`

#### Question
Which license, if any, should govern reuse of the public repository?

#### Why it matters
The repository is public, but the audited tree contains no license file. A license must not be inherited from adjacent Velantrim projects by assumption.

#### Existing evidence
Issue `#2` explicitly records license as open.

#### Required audit
Review intended reuse and governance consequences before choosing a license.

#### Preconditions
Explicit Owner decision.

#### Non-goals
Do not infer a license from Native Kernel, Soul, Titan, Crystal, or any other repository.

#### Exit criteria
An explicit decision is recorded and, if selected, the exact license artifact is added through a separately scoped docs/governance PR.

#### Possible outcomes
`FW_DONE`, `FW_DEFERRED`, `FW_NEEDS_ARCHITECTURE_DECISION`.

---

### MK-FW-003 — Executable conformance format

**FW_STATE:** `FW_DEFERRED`  
**Priority:** `P1`  
**Implementation authorized:** `NO`  
**Semantic Canon change authorized:** `NO`  
**Runtime capability change:** `NO`  
**Owner domain:** `Mentaury-Kernel composition / Governance decision`  
**Tracking:** GitHub Issue `#2`  
**Last verified:** `2026-08-16`

#### Question
Is executable conformance needed at all, and if so, what bounded format can test implementation profiles without turning a test harness into semantic authority?

#### Why it matters
`SC-01…SC-16` are architecture-level observable expectations only. A test expectation can accidentally create new normative semantics if it specifies outcomes not already authorized by the architecture.

#### Existing evidence
`docs/CONFORMANCE_SCENARIOS.md` explicitly states:

```text
SCENARIO DOCUMENTED
!= EXECUTABLE TEST
!= IMPLEMENTATION EVIDENCE
!= RUNTIME AUTHORIZATION
```

#### Required audit
Before any implementation, determine version binding, fixture representation, deterministic/non-deterministic boundaries, and what may legitimately produce binary pass/fail.

#### Required experiment / reproduction
None authorized yet.

#### Preconditions
Explicit architecture decision that executable conformance is necessary.

#### Non-goals
No runtime, no cognition tests, no identity/truth judge, no LLM-as-authority evaluator.

#### Exit criteria
Either `NO_IMPLEMENTATION` is chosen, or a bounded conformance contract is explicitly authorized before tooling is written.

#### Possible outcomes
`FW_DONE`, `FW_DEFERRED`, `FW_NEEDS_ARCHITECTURE_DECISION`, `FW_NOT_AUTHORIZED`.

---

### MK-FW-004 — Upstream semantic-pin freshness

**FW_STATE:** `FW_OPEN`  
**Priority:** `P1`  
**Implementation authorized:** `NO`  
**Semantic Canon change authorized:** `NO`  
**Runtime capability change:** `NO`  
**Owner domain:** `Mentaury-Kernel reconciliation`  
**Last verified:** `2026-08-16`

#### Question
Do the currently pinned Native Kernel, NPG-v0.1, and PCR-v0.1 semantic checkpoints still preserve the exact composition-relevant meanings recorded in `docs/PROVENANCE_MATRIX.md`?

#### Why it matters
Upstream projects evolve. Kernel must detect a material semantic contract change without mirroring every upstream PR or implementation status update.

#### Existing evidence
Current pins were reverified on `2026-08-16` and remain bounded semantic checkpoints rather than live-status mirrors.

#### Required audit
Recheck only when a reconciliation trigger fires: supersession, material rescope, loss of support, or ownership/meaning change of the referenced semantic statement.

#### Preconditions
A real trigger or periodic bounded maintenance review.

#### Non-goals
No automatic upstream sync and no automatic semantic promotion.

#### Authority boundaries

```text
SOURCE PAGE UPDATE != AUTOMATIC COMPOSITION UPDATE
SOURCE FRESHNESS != SEMANTIC INVALIDATION
```

#### Exit criteria
Pins are either reverified unchanged, explicitly reconciled, or marked as needing architecture review.

#### Possible outcomes
`FW_DONE`, `FW_OPEN`, `FW_STALE`, `FW_NEEDS_ARCHITECTURE_DECISION`.

---

## 5. Investigation queue

### MK-FW-005 — Documentation integrity / characterization automation

**FW_STATE:** `FW_INVESTIGATE`  
**Priority:** `P2`  
**Implementation authorized:** `NO`  
**Semantic Canon change authorized:** `NO`  
**Runtime capability change:** `NO`  
**Owner domain:** `Repository governance / documentation tooling`  
**Last verified:** `2026-08-16`

#### Question
Would small deterministic documentation checks materially reduce drift without becoming executable semantic conformance?

#### Why it matters
The repository currently has zero GitHub Actions workflows and no executable test suite. Earlier document audits identified value in checking stable structural facts such as status-vocabulary consistency and SC-ID alignment.

#### Existing evidence
The current repository contains architecture documents only; no workflow or checker exists.

#### Required audit
Separate **document characterization** from **semantic conformance**. Identify checks that merely verify already-declared structure.

#### Required experiment / reproduction
If later authorized, start with the smallest static snapshot/checker experiment. Do not preselect GitHub Actions or a framework.

#### Preconditions
Explicit docs-tooling scope; no new semantic expected values.

#### Non-goals
No runtime tests, cognition tests, identity/truth evaluation, or hidden Canon encoded in assertions.

#### Exit criteria
A decision records `NO_TOOLING`, `MORE_RESEARCH`, or a separately authorized bounded docs-consistency mechanism.

#### Possible outcomes
`FW_DONE`, `FW_INVESTIGATE`, `FW_DEFERRED`, `FW_NOT_AUTHORIZED`.

---

### MK-FW-006 — Repository change-control hardening

**FW_STATE:** `FW_INVESTIGATE`  
**Priority:** `P1`  
**Implementation authorized:** `NO`  
**Semantic Canon change authorized:** `NO`  
**Runtime capability change:** `NO`  
**Owner domain:** `Repository Governance`  
**Last verified:** `2026-08-16`

#### Question
Does this specification repository need branch protection, required review/check policies, or another bounded change-control mechanism at its current stage?

#### Why it matters
At audit time `main` is unprotected and there are no required status checks. That is a repository-governance fact, not proof of a defect, but it may permit accidental bypass of the carefully documented PR discipline.

#### Existing evidence
Fresh branch audit reports `protected=false`; repository Actions workflows are absent.

#### Required audit
Determine whether current single-owner/specification-bootstrap governance requires protection now or whether it should remain intentionally lightweight.

#### Preconditions
Explicit repository-governance decision.

#### Non-goals
Do not invent CI merely to satisfy a checklist. Do not require independent review unless such a policy is explicitly adopted.

#### Exit criteria
A documented decision: keep current state intentionally, or separately authorize a bounded repository-governance change.

#### Possible outcomes
`FW_DONE`, `FW_INVESTIGATE`, `FW_DEFERRED`, `FW_NEEDS_ARCHITECTURE_DECISION`.

---

## 6. Research candidates

### MK-FW-007 — Research-to-composition relevance review

**FW_STATE:** `FW_CANDIDATE`  
**Priority:** `P2`  
**Implementation authorized:** `NO`  
**Semantic Canon change authorized:** `NO`  
**Runtime capability change:** `NO`  
**Owner domain:** `Composition relevance only`  
**Last verified:** `2026-08-16`

#### Hypothesis
A future Native/Soul research result may expose a genuinely new cross-domain failure not covered by current Mentaury-Kernel invariants.

#### Current evidence
No such new failure is selected by this ledger. Current architecture already covers provenance, authority non-escalation, loss, admission isolation, freshness, branch non-collapse, particularity/generalization, and receipt non-laundering.

#### Alternative explanations
A new upstream capability may be entirely internal to its owner and require **no** Kernel change.

#### Experiment
When a specific research result appears, run the existing Scope Ownership / Necessity test against that result.

#### Falsification condition
If existing invariants already produce the safe composition outcome, no new Kernel law is necessary.

#### Non-goals
No automatic research promotion, no new research pipeline, no transfer of Soul/Native internals into Kernel.

#### Decision rule

```text
NEW RESEARCH RESULT
-> concrete uncovered cross-domain failure?
   NO  -> remain upstream / research
   YES -> check existing invariants
          covered -> no new law
          uncovered -> composition candidate only
```

#### Possible outcomes
`FW_STALE`, `FW_CANDIDATE`, `FW_NEEDS_ARCHITECTURE_DECISION`.

---

## 7. Deferred work

### MK-FW-008 — Concrete Semantic Continuity Port representation / serialization

**FW_STATE:** `FW_DEFERRED`  
**Priority:** `P1`  
**Implementation authorized:** `NO`  
**Semantic Canon change authorized:** `NO`  
**Runtime capability change:** `NO`  
**Owner domain:** `Future implementation profile`  
**Last verified:** `2026-08-16`

#### Question
What concrete wire/schema/serialization representation, if any, should implement the abstract Semantic Continuity Port?

#### Existing evidence
Current architecture intentionally keeps this an implementation decision.

#### Required audit
First prove that a concrete implementation milestone is selected and authorized. Then evaluate technology-specific profiles outside semantic Canon.

#### Preconditions
Separate implementation-profile decision and authority.

#### Non-goals
The abstract Kernel `versioned semantic / continuity envelope` must not be silently equated with Mentaury Soul P0-002 `EventEnvelope` or `CommandEnvelope`.

#### Exit criteria
A separately authorized implementation-profile contract exists, or the work remains deferred.

#### Possible outcomes
`FW_DEFERRED`, `FW_NEEDS_ARCHITECTURE_DECISION`, `FW_NOT_AUTHORIZED`, `FW_DONE`.

---

### MK-FW-009 — Security / deployment profile

**FW_STATE:** `FW_DEFERRED`  
**Priority:** `P2`  
**Implementation authorized:** `NO`  
**Semantic Canon change authorized:** `NO`  
**Runtime capability change:** `NO`  
**Owner domain:** `Future implementation / deployment governance`  
**Last verified:** `2026-08-16`

#### Question
What security and deployment obligations would apply to a future concrete implementation profile?

#### Why it matters
The current threat model is a **composition threat model**, not a network/security/deployment threat model.

#### Preconditions
A concrete implementation/deployment profile must first exist and be separately authorized.

#### Non-goals
Do not add cryptography, networking, deployment, secrets, or production requirements to semantic Canon merely because they may be prudent for a future implementation.

#### Exit criteria
A future implementation profile has an explicitly owned security/deployment review, or this item stays deferred.

#### Possible outcomes
`FW_DEFERRED`, `FW_NOT_AUTHORIZED`, `FW_DONE`.

---

## 8. Blocked work

No current item is classified `FW_BLOCKED` by the fresh audit.

Important distinction:

```text
NOT_AUTHORIZED != BLOCKED
DEFERRED != BLOCKED
NEEDS_ARCHITECTURE_DECISION != BLOCKED
```

Do not manufacture a blocker merely because no implementation permission exists.

---

## 9. Explicitly non-authorized directions

### MK-FW-010 — Runtime / production implementation

**FW_STATE:** `FW_NOT_AUTHORIZED`  
**Priority:** `P1`  
**Implementation authorized:** `NO`  
**Semantic Canon change authorized:** `NO`  
**Runtime capability change:** `NOT AUTHORIZED`  
**Owner domain:** `Requires future explicit bounded decision`  
**Last verified:** `2026-08-16`

The current project does **not** authorize:

- Port runtime implementation;
- cognition runtime;
- identity or truth adjudication;
- action execution;
- scheduler/autonomous loop;
- LLM/model integration;
- database/graph/vector-store selection as Canon;
- production deployment.

```text
SPECIFICATION_BOOTSTRAP
!= IMPLEMENTATION AUTHORITY
!= RUNTIME AUTHORITY
```

This entry exists to prevent future AI systems from mistaking a visible future direction for permission to build it.

---

## 10. Known risks / technical debt

### RISK-01 — Documentation-surface drift

Notion and GitHub can drift while the permanent authority model is unresolved.

**Mitigation:** explicit reconciliation; never silently choose.

### RISK-02 — Ledger-state / Canon-status collision

Both future work and provenance need statuses.

**Mitigation:** all ledger states use the `FW_` namespace. Never put `FW_*` values into the Normative Provenance Matrix.

### RISK-03 — Scenario-to-test authority laundering

A future test author may encode new semantic rules as expected outputs.

**Mitigation:** no executable conformance until explicitly decided; expected values must be traceable to existing architecture.

### RISK-04 — Research promotion pressure

A mature upstream research result may look important and be copied into Kernel despite no distinct composition failure.

**Mitigation:** `ARCHITECTURAL FIT != ARCHITECTURAL NECESSITY` and the Scope Ownership Test.

### RISK-05 — Stale Notion pre-GitHub wording

Fresh audit found that the Notion top status correctly records the repository as created, while Open Questions still contains an older `Exact GitHub name = DEFERRED / PRE_GITHUB_GATE` row. This is a documentation freshness defect, not an architecture problem.

**Required action in this cycle:** reconcile that row after the GitHub ledger PR is merged; preserve the still-open permanent Notion↔GitHub authority question separately.

---

## 11. Governance / operational work

Current operational rules:

- use small docs-only PRs for documentation-governance changes;
- report actual evidence only;
- `0 unresolved review threads` may be claimed only when checked;
- do not claim independent review unless it actually occurred;
- no merge on red CI if CI exists;
- if CI does not exist, report `CI: NOT_PRESENT`, not a fabricated success;
- do not create Issues for every ledger entry;
- keep Issue `#2` as the existing bounded tracker for its three current governance decisions unless scope genuinely requires a successor issue.

---

## 12. Suggested audit order

When the user later asks to review Future Work:

1. repository/default branch/current main SHA;
2. open PRs;
3. open Issues;
4. repository configuration / protection / workflows if relevant;
5. `docs/CURRENT_STATUS.md`;
6. Notion reconciliation status;
7. this ledger;
8. affected semantic pins in `docs/PROVENANCE_MATRIX.md`;
9. relevant architecture/invariant/threat/scenario document;
10. classify each old item as current, stale, done, blocked, or still unauthorized;
11. propose **at most one bounded next scope** without implementing it unless explicitly authorized.

---

## 13. Handoff protocol

A future AI should report at minimum:

```text
PROJECT: Mentaury-Kernel
MAIN: <live SHA>
LEDGER: docs/AUDIT_AND_FUTURE_WORK.md
AI ROUTER: docs/AI_CONTEXT.md
OPEN PRS: <live>
OPEN ISSUES: <live>
CI: <live / NOT_PRESENT>
NOTION RECONCILIATION: <state>
RUNTIME: NONE unless separately proven otherwise
```

Then for each ledger item:

```text
FW_DONE
FW_OPEN
FW_STALE
FW_INVESTIGATE
FW_BLOCKED
FW_NEEDS_REPRODUCTION
FW_NEEDS_ARCHITECTURE_DECISION
FW_NOT_AUTHORIZED
NEW_FINDING
```

`NEW_FINDING` is a report label, not a persistent `FW_STATE`; a new finding must be classified before it is added to the ledger.

---

## 14. Historical DONE items

### MK-HIST-001 — Repository creation / specification bootstrap

**State:** `FW_DONE`

The public `velantrian/Mentaury-Kernel` repository exists and the specification bootstrap is merged.

This historical completion does **not** imply implementation or runtime authority.

### MK-HIST-002 — v0.2.4 documentation reconciliation / provenance hardening

**State:** `FW_DONE`

The current documentation package preserves the v0.2.3 semantic architecture baseline while recording v0.2.4 document/routing reconciliation and reverified semantic pins.

### MK-HIST-003 — Threat ↔ scenario ID alignment

**State:** `FW_DONE` for current documentation scope

`SC-01…SC-16` are aligned between `docs/THREAT_MODEL.md` and `docs/CONFORMANCE_SCENARIOS.md` as documentation-level traceability. This does not mean executable conformance exists.

---

## 15. Update rules

Update this ledger only after resolving live evidence.

For every changed item:

- update `Last verified`;
- cite the exact live artifact or decision that changed the classification;
- preserve historical completion rather than deleting it without explanation;
- do not convert priority into authorization;
- do not convert an Issue into implementation permission;
- do not convert a research result into a Kernel invariant without a concrete uncovered composition failure;
- do not convert a documented conformance scenario into an executable test contract without explicit authorization;
- do not silently settle the permanent Notion↔GitHub authority model.

### Completion criterion for this ledger

A new AI with no old chat context should be able to determine:

```text
WHAT EXISTS
WHAT IS FINISHED
WHAT IS OPEN
WHAT IS UNCERTAIN
WHAT IS DEFERRED
WHAT IS FORBIDDEN
WHAT MUST BE VERIFIED
WHERE THE EVIDENCE IS
HOW TO CONTINUE SAFELY
```

while receiving **no automatic permission to implement the next milestone**.
