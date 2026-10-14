"""H-QS-1: naive majority vs source-independence quorum. stdlib only.
run: python3 hqs1.py run  (paid, needs OPENROUTER_API_KEY; hard cap)   |  python3 hqs1.py analyze raw.jsonl"""
import collections, hashlib, json, os, re, sys, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
CAP_USD = 0.80  # this experiment's share of the $1.00 total cap
A_MODEL = "openai/gpt-6-luna"; A_VOTES = 5
B_SOURCES = [("google/gemini-2.5-flash-lite", "Answer this multiple-choice question. Reply with only the letter."),
             ("meta-llama/llama-4-scout", "You are a careful quiz expert. Output a single capital letter A-D, nothing else."),
             ("deepseek/deepseek-v4-flash", "Pick the correct option. Respond with exactly one letter.")]
A_SYSTEM = "Use the provided reference note. Reply with only the letter of the correct option."

def load_q(): return json.load(open(os.path.join(HERE, "questions.json")))

def fmt(q, note=None):
    s = (note + "\n\n" if note else "") + q["q"] + "\n" + "\n".join(f"{k}) {v}" for k, v in q["opts"].items())
    return s

def source_id(model, context):
    return hashlib.sha256((model + "\x00" + context).encode()).hexdigest()[:12]

def parse(text):
    m = re.search(r"\b([ABCD])\b", (text or "").strip().upper())
    return m.group(1) if m else None

def call(model, system, user, temperature, http=None):
    body = json.dumps({"model": model, "messages": [{"role": "system", "content": system}, {"role": "user", "content": user}],
                       "temperature": temperature, "max_tokens": 400, "usage": {"include": True},
                       **({"reasoning": {"effort": "low"}} if "luna" in model else {})}).encode()
    req = urllib.request.Request("https://openrouter.ai/api/v1/chat/completions", data=body,
                                 headers={"Authorization": "Bearer " + os.environ["OPENROUTER_API_KEY"], "Content-Type": "application/json"})
    with (http or urllib.request.urlopen)(req, timeout=90) as r:
        d = json.load(r)
    return d["choices"][0]["message"].get("content") or "", float(d.get("usage", {}).get("cost") or 0.0)

def plan(qs):
    jobs = []
    for q in qs:
        ctx = fmt(q, q["note"])
        for i in range(A_VOTES): jobs.append({"qid": q["id"], "cond": "A", "vote": i, "model": A_MODEL, "system": A_SYSTEM, "user": ctx, "temperature": 1.0})
        for m, sysp in B_SOURCES: jobs.append({"qid": q["id"], "cond": "B", "vote": 0, "model": m, "system": sysp, "user": fmt(q), "temperature": 0.7})
    return jobs

def run(out, caller=call):
    spent = 0.0; n = 0
    with open(out, "w") as f:
        for j in plan(load_q()):
            if spent >= CAP_USD - 0.02: print("STOP: cap reached"); break
            try: text, cost = caller(j["model"], j["system"], j["user"], j["temperature"])
            except Exception as e: text, cost = "ERROR:" + type(e).__name__, 0.0
            spent += cost; n += 1
            rec = {"qid": j["qid"], "cond": j["cond"], "vote": j["vote"], "model": j["model"],
                   "source": source_id(j["model"], j["system"] + j["user"]), "raw": text[:200], "answer": parse(text), "cost": cost}
            rec["sha256"] = hashlib.sha256(json.dumps(rec, sort_keys=True).encode()).hexdigest()
            f.write(json.dumps(rec, sort_keys=True, ensure_ascii=False) + "\n")
    return spent, n

def majority(votes):
    votes = [v for v in votes if v]
    if not votes: return None
    c = collections.Counter(votes).most_common()
    return None if len(c) > 1 and c[0][1] == c[1][1] else c[0][0]

def quorum(recs):
    by_src = collections.defaultdict(list)
    for r in recs: by_src[r["source"]].append(r["answer"])
    return majority([majority(v) for v in by_src.values()])

def analyze(path):
    qs = {q["id"]: q for q in load_q()}
    recs = [json.loads(l) for l in open(path)]
    per = collections.defaultdict(list)
    for r in recs: per[r["qid"]].append(r)
    res = {"per_q": {}}
    acc = collections.Counter(); tot = collections.Counter(); agreeA = []; parsed = sum(1 for r in recs if r["answer"])
    for qid, rs in per.items():
        q = qs[qid]; t = q["type"]
        A = [r for r in rs if r["cond"] == "A"]
        naive = majority([r["answer"] for r in rs]); qu = quorum(rs); a_maj = majority([r["answer"] for r in A])
        b_maj = majority([r["answer"] for r in rs if r["cond"] == "B"])
        aa = [r["answer"] for r in A if r["answer"]]
        agreeA.append(collections.Counter(aa).most_common(1)[0][1] / len(aa) if aa else 0)
        for k, v in (("naive", naive), ("quorum", qu), ("A_only", a_maj), ("B_only", b_maj)):
            acc[(k, t)] += int(v == q["ans"]); tot[(k, t)] += 1
        res["per_q"][qid] = {"type": t, "truth": q["ans"], "naive": naive, "quorum": qu, "A_only": a_maj, "B_only": b_maj,
                             "votes": [(r["cond"], r["model"].split("/")[0], r["answer"]) for r in rs]}
    res["accuracy"] = {f"{k}_{t}": round(acc[(k, t)] / tot[(k, t)], 3) for (k, t) in tot}
    res["A_mean_agreement"] = round(sum(agreeA) / len(agreeA), 3)
    res["parsed_rate"] = round(parsed / len(recs), 3); res["n_calls"] = len(recs); res["cost_usd"] = round(sum(r["cost"] for r in recs), 6)
    a = res["accuracy"]; ntr = tot[("naive", "trap")]; nco = tot[("naive", "control")]
    d_trap = a["quorum_trap"] - a["naive_trap"]; d_ctl = (a["quorum_control"] - a["naive_control"]) * nco
    echo = res["A_mean_agreement"] >= 0.8 and a["A_only_trap"] <= 0.5
    if res["parsed_rate"] < 0.8: v = "INCONCLUSIVE"
    elif d_trap >= 0.33 - 1e-9 and d_ctl >= -1 and echo: v = "PASS"
    elif d_trap <= 0 or (a["A_only_trap"] > 0.5 and d_trap <= 0): v = "FAIL"
    else: v = "INCONCLUSIVE"
    res["verdict"] = v; res["raw_sha256"] = hashlib.sha256(open(path, "rb").read()).hexdigest()
    return res

if __name__ == "__main__":
    if sys.argv[1] == "run":
        print(run(os.path.join(HERE, "raw_results.jsonl")))
    else:
        r = analyze(sys.argv[2]); json.dump(r, open(os.path.join(HERE, "analysis.json"), "w"), indent=1, ensure_ascii=False)
        print(json.dumps({k: v for k, v in r.items() if k != "per_q"}, indent=1))
