import json, os, sys, tempfile, unittest
sys.path.insert(0, os.path.dirname(__file__))
import hqs1

def fake(model, system, user, temperature):
    # mocked: shared misleading note -> echo wrong answer; independent sources -> correct
    q = next(q for q in hqs1.load_q() if q["q"] in user)
    if "Authoritative" in user:
        return (q["note"].split("option ")[1][0], 0.0001)
    return (q["ans"], 0.0001)

class T(unittest.TestCase):
    def test_parse(self):
        self.assertEqual(hqs1.parse("B"), "B"); self.assertEqual(hqs1.parse("Answer: C."), "C"); self.assertIsNone(hqs1.parse("none"))
    def test_quorum_collapses_echo(self):
        recs = [{"source": "s1", "answer": "A"}] * 5 + [{"source": f"b{i}", "answer": "C"} for i in range(3)]
        self.assertEqual(hqs1.majority([r["answer"] for r in recs]), "A")
        self.assertEqual(hqs1.quorum(recs), "C")
    def test_mocked_pipeline_deterministic(self):
        d = tempfile.mkdtemp(); p1, p2 = os.path.join(d, "1"), os.path.join(d, "2")
        hqs1.run(p1, fake); hqs1.run(p2, fake)
        self.assertEqual(open(p1).read(), open(p2).read())
        r = hqs1.analyze(p1)
        self.assertEqual(r["accuracy"]["naive_trap"], 0.0); self.assertEqual(r["accuracy"]["quorum_trap"], 1.0)
        self.assertEqual(r["verdict"], "PASS")
    def test_cap_stops(self):
        d = tempfile.mkdtemp(); _, n = hqs1.run(os.path.join(d, "x"), lambda *a: ("A", 0.5))
        self.assertLess(n, 3)

if __name__ == "__main__":
    unittest.main()
