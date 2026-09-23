# 🔐 GitHub Governance Runbook

> Repository-administration runbook for `velantrian/Mentaury-Kernel`. This file governs repository mechanics only; it does not grant semantic, runtime, truth, identity, action, or production authority.

## Current verified prerequisite

As of `2026-09-23`:

- `main@86e1efe6cf5cb2ec0423093379608cea4bd3b933`;
- merge commit signature: `VERIFIED · VALID`;
- CapabilityPort Conformance runs on **every pull request**;
- the same workflow runs on **every push to `main`**;
- PR #14 exact-head CI: `SUCCESS`;
- PR #14 post-merge CI: `SUCCESS`;
- `main` protection: not enabled;
- repository rulesets: none.

The workflow-side prerequisite for a required status check is therefore complete.

## Required repository-admin policy

Configure either a repository ruleset or branch-protection rule targeting `main` with these constraints:

1. **Require a pull request before merging.**
2. **Require status checks to pass before merging.**
   - Required check: the existing `Python stdlib conformance` job / CapabilityPort Conformance workflow.
3. **Block force pushes to `main`.**
4. **Block deletion of `main`.**
5. Do **not** require an independent reviewer merely to satisfy a checklist; reviewer requirements need a separate governance decision.
6. Prefer **squash merge** as the sole merge method for evidence consistency.
7. Enable automatic deletion of head branches after merge.
8. Remove stale historical branches only after confirming that no unique unmerged content remains.

## Branch cleanup classification

The 2026-09-23 audit established:

- `research/history-provenance-boundary-2026-09-18`: `ahead=0`; safe cleanup candidate.
- `claude/documentation-analysis-owkx58`: historical audit branch; live findings were incorporated by PR #12; cleanup candidate after preserving the audit only if historical retention is desired.
- `audit/reconcile-2026-09-23` and `ci/always-run-repository-gate-2026-09-23`: merged remediation branches; cleanup candidates.
- older merged PR branches: cleanup candidates after confirming no intentionally retained historical purpose.

Because squash merges do not preserve branch ancestry, an old merged branch may still appear `ahead` in a raw Git comparison even when its effective content has already been incorporated. Do not interpret `ahead > 0` alone as evidence that the branch contains required current work.

## Verification after applying settings

Confirm all of the following:

```text
MAIN PROTECTED / RULESET ACTIVE        YES
PR REQUIRED                            YES
REQUIRED CONFORMANCE CHECK             YES
FORCE PUSH TO MAIN                     BLOCKED
DELETE MAIN                            BLOCKED
SQUASH-ONLY MERGE                      YES
AUTO-DELETE MERGED HEAD BRANCHES       YES
```

Then update Issue #13 and this repository checkpoint.

## Non-authorizations

```text
REPOSITORY PROTECTION != SEMANTIC CANON
REQUIRED CHECK != TRUTH AUTHORITY
MERGE SUCCESS != RUNTIME AUTHORIZATION
BRANCH CLEANUP != HISTORY ERASURE
```
