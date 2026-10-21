"""Reject malformed saved evidence and exercise the recovered sampler directly."""
import ast
import csv
import json
from pathlib import Path
import shutil
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from audit_drive_results import read_predictions, summarize_counts, audit_released_counts
from verify_repository import check_recovered_notebook


class SavedPredictionTests(unittest.TestCase):
    def write_predictions(self, folder, rows):
        path = Path(folder) / "predictions.csv"
        with path.open("w", newline="") as f:
            w = csv.writer(f); w.writerow(["label", "prediction", "result"]); w.writerows(rows)
        return path

    def rows(self):
        return [(0, 0, "correct")] * 32 + [(1, 2, "incorrect")] * 32 + [(2, 2, "correct")] * 32

    def test_clip_repetition_does_not_multiply_independent_predictions(self):
        with tempfile.TemporaryDirectory() as tmp:
            summary, counts = read_predictions(self.write_predictions(tmp, self.rows()))
            self.assertEqual(summary["scored_rows"], 96)
            self.assertEqual(summary["uniform_blocks"], 3)
            self.assertEqual(summary["top1_pct"], "66.67")
            self.assertEqual(counts[(1, 2)], 32)

    def test_inconsistent_result_flags_rejected(self):
        rows = self.rows(); rows[0] = (0, 0, "incorrect")
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaisesRegex(ValueError, "flag"):
                read_predictions(self.write_predictions(tmp, rows))

    def test_partial_or_nonuniform_blocks_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            for rows in ([], self.rows()[:-1]):
                with self.assertRaisesRegex(ValueError, "Incomplete"):
                    read_predictions(self.write_predictions(tmp, rows))
            rows = self.rows(); rows[1] = (0, 1, "incorrect")
            with self.assertRaisesRegex(ValueError, "differing"):
                read_predictions(self.write_predictions(tmp, rows))

    def test_unknown_class_rejected(self):
        rows = [(3, 3, "correct")] * 32
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaisesRegex(ValueError, "Unknown"):
                read_predictions(self.write_predictions(tmp, rows))

    def test_missing_negative_or_zero_class_counts_rejected(self):
        counts = {(a, b): int(a == b) for a in range(3) for b in range(3)}
        for bad in ({(0, 0): 1}, {**counts, (0, 0): -1}, {k: 0 for k in counts}):
            with self.assertRaises(ValueError):
                summarize_counts(bad)

    def test_all_released_versions_reconcile(self):
        rows = audit_released_counts()
        self.assertEqual(len(rows), 8)
        self.assertEqual({s["scored_rows"] for s in rows}, {2880})
        self.assertEqual([s["top1_pct"] for s in rows],
                         ["77.78", "48.89", "93.33", "88.89", "95.56", "80.00", "91.11", "68.89"])

    def test_aggregate_mutation_detected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            shutil.copytree(ROOT / "experiments", root / "experiments")
            p = root / "experiments/recovered/results.csv"
            p.write_text(p.read_text().replace(",2240,77.78,", ",2240,78.00,", 1))
            with self.assertRaisesRegex(ValueError, "mismatch"):
                audit_released_counts(root)

    def test_recovered_source_is_sanitized_and_fingerprinted(self):
        self.assertEqual(check_recovered_notebook(), [])


class RecoveredSamplerTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Execute only the inspected pure function, never notebook imports or commands.
        notebook = json.loads((ROOT / "action_recognition/notebooks/slowfast_research.ipynb").read_text())
        source = "".join(notebook["cells"][15]["source"])
        function = next(n for n in ast.parse(source).body
                        if isinstance(n, ast.FunctionDef) and n.name == "clip_sampler_uniform")
        scope = {"CLIP_DURATION": 32}
        exec(compile(ast.Module(body=[function], type_ignores=[]), "recovered_sampler", "exec"), scope)
        cls.sampler = staticmethod(scope["clip_sampler_uniform"])

    def windows(self, frames):
        windows = []; end = flag = None
        for _ in range(100):
            start, end, flag = self.sampler(end, flag, list(range(frames)))
            windows.append((start, end))
            if flag == "Yes":
                return windows
        self.fail("Sampler failed to stop")

    def test_exact_multiple_loses_last_full_block(self):
        self.assertEqual(self.windows(128), [(0, 32), (32, 64), (64, 96)])

    def test_tail_and_boundary_behavior(self):
        self.assertEqual(len(self.windows(129)), 4)
        self.assertEqual(self.windows(63), [(0, 32)])


if __name__ == "__main__":
    unittest.main()
