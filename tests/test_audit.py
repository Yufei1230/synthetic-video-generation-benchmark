"""Regression and edge-case checks for the new documentation audit utilities."""
import csv
import json
from pathlib import Path
import shutil
import sys
import tempfile
import unittest
from decimal import Decimal

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from audit_results import load_results, round_percent, matching_count, minimum_common_denominator, changes
from verify_repository import check_preservation, check_local_links, check_result_tables


class ResultAuditTests(unittest.TestCase):
    def test_transcription_of_paper(self):
        rows = load_results()
        self.assertEqual([str(r["top1_pct"]) for r in rows],
                         ["77.78", "57.78", "93.33", "88.89", "95.56", "53.33", "91.11", "81.11"])
        self.assertEqual([r["total_training_videos"] for r in rows], [90, 150, 150, 150, 150, 210, 270, 330])

    def test_pp_is_not_relative_percent(self):
        pp, relative = changes("95.56", "77.78")
        self.assertEqual(pp, Decimal("17.78"))
        self.assertEqual(relative.quantize(Decimal(".01")), Decimal("22.86"))
        with self.assertRaises(ValueError):
            changes(10, 0)

    def test_rounding_and_invalid_counts(self):
        self.assertEqual(round_percent(70, 90), Decimal("77.78"))
        self.assertEqual(round_percent(1, 32), Decimal("3.13"))
        for correct, total in ((1, 0), (-1, 7), (8, 7)):
            with self.assertRaises(ValueError):
                round_percent(correct, total)

    def test_video_denominators_cannot_explain_rates(self):
        self.assertIsNone(matching_count("77.78", 21))
        self.assertIsNone(matching_count("86.21", 7))

    def test_inferred_denominator_is_compatibility_only(self):
        rows = load_results()
        self.assertEqual(minimum_common_denominator([r["shaking_pct"] for r in rows]), 17)
        self.assertEqual(minimum_common_denominator([r["swirling_pct"] for r in rows]), 29)
        self.assertEqual(minimum_common_denominator([r["buretting_pct"] for r in rows]), 44)
        self.assertIsNone(minimum_common_denominator(["86.21"], max_total=7))
        # A multiple also works: percentages do not identify actual counts.
        self.assertEqual(matching_count("86.21", 58), 50)

    def test_bad_budget_and_evidence_label_rejected(self):
        with (ROOT / "experiments/paper_reported_results.csv").open(newline="") as f:
            reader = csv.DictReader(f)
            names, original = reader.fieldnames, list(reader)
        with tempfile.TemporaryDirectory() as tmp:
            for field, bad in (("synthetic_training_videos", "20"), ("evidence_status", "reproduced"),
                               ("evaluation_unit", "video"), ("top1_pct", "101")):
                rows = [r.copy() for r in original]
                rows[1][field] = bad
                path = Path(tmp) / "bad.csv"
                with path.open("w", newline="") as f:
                    w = csv.DictWriter(f, fieldnames=names)
                    w.writeheader()
                    w.writerows(rows)
                with self.assertRaises(ValueError, msg=field):
                    load_results(path)

    def test_local_links_and_result_tables(self):
        self.assertEqual(check_local_links()[0], [])
        self.assertEqual(check_result_tables(), [])

    def test_original_preserved_and_mutation_detected(self):
        self.assertEqual(check_preservation(), [])
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            names = ["README.md", "references/benchmark_integrity.json"]
            manifest = json.loads((ROOT / names[1]).read_text())
            for name in names + list(manifest["files"]):
                target = root / name
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(ROOT / name, target)
            with (root / "notebooks/CogVideoX.ipynb").open("ab") as f:
                f.write(b" ")
            self.assertTrue(any("CogVideoX" in e for e in check_preservation(root)))
            readme = root / "README.md"
            readme.write_text(readme.read_text().replace("# Synthetic Video Generation Benchmark", "# Changed benchmark"))
            self.assertIn("Original README content changed", check_preservation(root))


if __name__ == "__main__":
    unittest.main()
