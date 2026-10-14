import os, sys, unittest
sys.path.insert(0, os.path.dirname(__file__))
import hbm1

class T(unittest.TestCase):
    def test_deterministic(self):
        self.assertEqual(hbm1.evaluate(), hbm1.evaluate())
    def test_change_rule_cases(self):
        rows = {(r["scenario"], r["rule"]): r for r in hbm1.evaluate()}
        self.assertTrue(rows[("S1_new_contradiction", "evidence_change")]["review"])
        self.assertFalse(rows[("S2_exact_repeats", "evidence_change")]["review"])
        self.assertFalse(rows[("S3_near_dup_flood", "evidence_change")]["review"])
        self.assertTrue(rows[("S6_hidden_contradiction", "evidence_change")]["review"])
    def test_duplicates_not_novel(self):
        r = hbm1.ChangeRule()
        self.assertTrue(r.novel("a b c d e"))
        self.assertFalse(r.novel("E d c b a"))
    def test_count_rule_fires_on_volume(self):
        r = hbm1.CountRule()
        self.assertEqual([r.step([1])[0] for _ in range(5)], [False]*4 + [True])

if __name__ == "__main__":
    unittest.main()
