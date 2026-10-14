"""H-BM-1: deterministic offline simulation. Review trigger by evidence CHANGE vs count threshold.
Python stdlib only. No LLM, no network. Conceptual mapping: review == UNRESOLVED belief returns to work (INIT-01)."""
import hashlib, json, re, sys

K = 5; JACCARD_DUP = 0.8; W_MIN = 0.5; DRIFT = 1.0; JUMP = 1.5; ALPHA = 0.3

def toks(t):
    return set(re.findall(r"[a-zа-я0-9]+", t.lower()))

def norm(t):
    return " ".join(sorted(toks(t)))

class CountRule:
    name = "count_threshold"
    def __init__(self): self.n = 0
    def step(self, items):
        self.n += len(items)
        if self.n >= K:
            self.n = 0
            return True, "count>=K"
        return False, ""

class ChangeRule:
    name = "evidence_change"
    def __init__(self):
        self.seen = []; self.seen_norm = set(); self.ema = 0.0; self.drift = 0.0
    def novel(self, text):
        n = norm(text)
        if n in self.seen_norm: return False
        t = toks(text)
        for s in self.seen:
            if len(t | s) and len(t & s) / len(t | s) >= JACCARD_DUP: return False
        self.seen.append(t); self.seen_norm.add(n); return True
    def step(self, items):
        sig = 0.0; reason = ""
        for it in items:
            if not self.novel(it["text"]): continue
            v = it["polarity"] * it["weight"]; sig += v
            if it["polarity"] < 0:
                self.drift += it["weight"]
                if it["weight"] >= W_MIN: reason = reason or "novel_contradiction"
        if not reason and self.drift >= DRIFT: reason = "drift"
        if not reason and abs(sig - self.ema) >= JUMP: reason = "jump_vs_baseline"
        self.ema = ALPHA * sig + (1 - ALPHA) * self.ema  # adaptation
        if reason:
            self.drift = 0.0
            return True, reason
        return False, ""

def ev(text, pol, w): return {"text": text, "polarity": pol, "weight": w}

HIST = [[ev("sensor log A shows module stable over week one", 1, 0.6)],
        [ev("independent review B confirms stable latency", 1, 0.6)],
        [ev("benchmark C passes under nominal load", 1, 0.6)]]

def scenarios():
    s = {}
    s["S1_new_contradiction"] = (HIST + [[ev("crash report D: module fails under cold start", -1, 0.9)]], True)
    s["S2_exact_repeats"] = (HIST + [[ev("sensor log A shows module stable over week one", 1, 0.6)] for _ in range(20)], False)
    pf = ["again", "today", "still", "once more", "per log", "reported", "noted", "confirmed", "seen", "recorded"]
    s["S3_near_dup_flood"] = (HIST + [[ev(f"sensor log A shows module stable over week one {pf[i % 10]}", 1, 0.6)] for i in range(20)], False)
    s["S4_slow_drift"] = (HIST + [[ev(f"minor anomaly report {i}: latency spike case number {i}", -1, 0.2)] for i in range(8)], True)
    s["S5_novel_support"] = (HIST + [[ev(f"new independent check {i}: stable result in environment {i}", 1, 0.6)] for i in range(8)], False)
    flood = [[ev("benchmark C passes under nominal load", 1, 0.6)] for _ in range(10)]
    s["S6_hidden_contradiction"] = (HIST + flood[:5] + [[ev("benchmark C passes under nominal load", 1, 0.6), ev("field failure E: data corruption after restart", -1, 0.8)]] + flood[5:], True)
    return s

def run_rule(rule_cls, steps):
    r = rule_cls(); trig = []
    for i, items in enumerate(steps):
        t, why = r.step(items)
        if t and i >= len(HIST): trig.append({"step": i, "reason": why})
        elif t: trig.append({"step": i, "reason": why, "history": True})
    return trig

def evaluate():
    rows = []
    for sid, (steps, expect) in scenarios().items():
        for rc in (CountRule, ChangeRule):
            trig = [t for t in run_rule(rc, steps) if not t.get("history")]
            got = bool(trig)
            rows.append({"scenario": sid, "rule": rc.name, "expected_review": expect, "review": got,
                         "n_reviews": len(trig), "first": trig[0] if trig else None,
                         "FP": int(got and not expect), "FN": int(expect and not got)})
    for r in rows:
        r["sha256"] = hashlib.sha256(json.dumps({k: v for k, v in r.items() if k != "sha256"}, sort_keys=True).encode()).hexdigest()
    return rows

def verdict(rows):
    ch = [r for r in rows if r["rule"] == "evidence_change"]; bl = [r for r in rows if r["rule"] == "count_threshold"]
    if any(r["FN"] for r in ch if r["scenario"][:2] in ("S1", "S6")) or any(r["FP"] for r in ch if r["scenario"][:2] in ("S2", "S3")): return "FAIL"
    if sum(r["FP"] + r["FN"] for r in ch) == 0 and sum(r["FP"] + r["FN"] for r in bl) >= 1: return "PASS"
    return "INCONCLUSIVE"

if __name__ == "__main__":
    rows = evaluate()
    out = sys.argv[1] if len(sys.argv) > 1 else "results.jsonl"
    with open(out, "w") as f:
        for r in rows: f.write(json.dumps(r, sort_keys=True, ensure_ascii=False) + "\n")
    agg = hashlib.sha256(open(out, "rb").read()).hexdigest()
    print(json.dumps({"verdict": verdict(rows), "results_sha256": agg}, ensure_ascii=False))
    for r in rows: print(r["scenario"], r["rule"], "review" if r["review"] else "-", r["n_reviews"], "FP" if r["FP"] else "", "FN" if r["FN"] else "")
