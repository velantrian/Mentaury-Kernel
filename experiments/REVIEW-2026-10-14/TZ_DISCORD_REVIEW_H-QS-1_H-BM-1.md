# Spec: refining Mentaury rules after the H-QS-1/H-BM-1 review

**Repository:** `velantrian/Mentaury-Kernel` · **branch:** `experiments` · **date:** 2026-10-14

## 1. Context
- Both experiments **PASSED** against their preregistered criteria (commit `25df0a8`):
  - **H-QS-1** (quorum): simple majority on traps scored 16.7%; quorum with source grouping scored 83.3%.
  - **H-BM-1** (belief revision): the change rule gave 0 false and 0 missed revisions; the K=5 counter failed in 4 of 6 scenarios.
- Review: independent scientific-technical review (ChatGPT, 2026-10-14).
- **Verdict: CONDITIONAL APPROVAL.** The direction is right, but the wording must **not** be carried into Soul without further work.
- PASS against preregistration ≠ proven fitness of the rule for the architecture.

## 2. Three proposals and verdicts
**(a) Track vote provenance:** ✅ justified.
- The echo effect under a shared basis was demonstrated.
- Independence means independent **evidential grounds**, not different models. Different models and prompts are only weak signals of independence.
- If there are not enough independent grounds, the aggregator returns `NO_DECISION`. A quorum never replaces the Evidence Gate.

**(b) Counter N:** 🟡 remove as an automatic revision trigger.
- Keep it as a statistic for prioritization (INIT-01) and audit.
- False trigger: a batch of new confirmations must not start a revision.
- Confidence does not rise automatically with the number of confirmations.

**(c) Revision on contradiction:** 🟡 yes, with conditions:
- the evidence is verified before any change to the belief;
- protection against repeat and paraphrase attacks;
- a revision budget, without silently losing important contradictions;
- **a contradiction triggers a review, not an automatic retraction of the belief.**

## 3. Weak points
- **P0, negation:** `ChangeRule.novel()` treats "stable" and "not stable" as near-duplicates (Jaccard 0.8). Polarity must be checked before the duplicate check.
- **P0, no minimum quorum:** `quorum()` is a majority after deduplication, so a single vote can decide. A check `effective_independent_sources >= minimum_required_sources` is needed.
- **P0, source ID depends on the prompt:** `source_id()` hashes the exact text, so slightly changed prompts produce "new" sources.
- **P1, positive signal:** `abs(signal - ema) >= 1.5` also fires on a batch of confirmations. The trigger must react only to contradictions.
- **P1:** authenticity and provenance of evidence are not checked; time, scope and evidence withdrawal are not modelled.
- **Methodology:** the cause of the H-QS-1 improvement is not isolated. It is unclear how much came from vote grouping, from the absence of the poisoned note, and from model choice. A factorial design is needed.
- **Soul P0-015:** it already has `source_group` and a minimum of 2 independent groups per side. The task is to **test its resistance to forgery**, not to build from scratch.
- **Terminal statuses** (`SUPPORTED` / `CONTRADICTED` / `SUPERSEDED`) must not return to `UNRESOLVED` without record lineage (`TERMINAL_RECONSIDERATION_LINEAGE_REQUIRED`).

## 4. CLASS-2 matrix (written by an independent author)
| ID | Attack | Expected behaviour |
|---|---|---|
| QS-01 | Three different models use one poisoned RAG document | No false independent quorum |
| QS-02 | One source varies prompts to get new source_ids | Dependent votes do not increase the quorum |
| QS-03 | Only one vote is available, the rest failed | No decision when the quorum is insufficient |
| QS-04 | Two models are wrong the same way, one gives a verifiable refutation | The majority is not automatically treated as truth |
| BM-01 | Added not, a different number, unit or sign | The contradiction is not discarded as a duplicate |
| BM-02 | Three independent confirmations in one batch | No false revision from an EMA jump |
| BM-03 | Hundreds of uniquely worded refutations from one source | Revisions are bounded; evidential weight does not grow artificially |
| BM-04 | A source withdraws an earlier confirmation | The change goes to review |
| BM-05 | Statements about different versions or time periods | No false contradiction |
| SOUL-01 | New evidence against a terminal SUPPORTED belief | No forbidden state transition |
| SOUL-02 | Conflict, repeated event, crash, replay | Determinism, history preserved, Evidence Gate not bypassed |

Priority: **QS-01, BM-01, SOUL-01.** PASS/FAIL thresholds are fixed in the preregistration before running.

## 5. Steps
1. Fix **H-BM-1**: polarity before the duplicate check, trigger only on contradictions, handle evidence withdrawal. Compare against baselines: a unique-source counter, periodic audit, and a hybrid.
2. Fix **H-QS-1**: minimum quorum and `NO_DECISION`; source identified by provenance, not prompt text. Re-run as a factorial design: model, shared note, RAG and prompt varied separately.
3. Review **Soul P0-015** (`source_group`) for forgery resistance, read-only.
4. An independent author writes and runs the **CLASS-2** matrix.
5. Only then write the Kernel → Soul bridge note (stage S3, Tier C), followed by the owner's decision.

## 6. Constraints
- **Soul is read-only** until items 1–4 are closed.
- Do not change `BeliefReducer` or the Evidence Gate; do not enable runtime or automatic revision.
- **Do not touch main**; all work happens in the `experiments` branch.
- Do not introduce a new `QuorumEngine` as another owner of truth.
