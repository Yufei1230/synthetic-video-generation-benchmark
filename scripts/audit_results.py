#!/usr/bin/env python3
"""Audit a transcription of published aggregates, never model predictions."""
import csv
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "experiments/paper_reported_results.csv"
METRICS = ("top1_pct", "shaking_pct", "swirling_pct", "buretting_pct")
COUNT_FIELDS = ("real_training_videos", "synthetic_training_videos", "total_training_videos")
EXPECTED_IDS = ("baseline", "aug_a", "aug_b", "aug_c", "aug_d", "combo_a", "combo_b", "combo_c")


def load_results(path=SOURCE):
    with Path(path).open(newline="", encoding="utf-8") as stream:
        rows = list(csv.DictReader(stream))
    if tuple(r.get("experiment_id") for r in rows) != EXPECTED_IDS:
        raise ValueError("Expected the eight distinct paper conditions in source order")
    for row in rows:
        for field in COUNT_FIELDS:
            row[field] = int(row[field])
        for field in METRICS:
            row[field] = Decimal(row[field])
            if not row[field].is_finite() or not 0 <= row[field] <= 100:
                raise ValueError(f"Invalid percentage: {field}")
        if row["evidence_status"] != "paper_reported":
            raise ValueError("This table must not be relabeled as independent replication")
        if row["evaluation_unit"] != "frame" or row["unit_evidence"] != "author_clarification_not_code_verified":
            raise ValueError("Retain the author clarification and its verification boundary")
        factors = [f for f in row["factors"].split(";") if f]
        if len(set(factors)) != len(factors) or not set(factors) <= {"camera", "clothing", "background", "hairstyle"}:
            raise ValueError("Invalid factor pool")
        if row["real_training_videos"] != 90 or row["synthetic_training_videos"] != 60 * len(factors):
            raise ValueError("Training composition disagrees with P1 Tables V–VI")
        if row["total_training_videos"] != sum(row[f] for f in COUNT_FIELDS[:2]):
            raise ValueError("Training total does not reconcile")
        expected_group = "baseline" if not factors else "single" if len(factors) == 1 else "multi"
        if row["group"] != expected_group or not row["source_location"]:
            raise ValueError("Missing provenance or inconsistent experiment group")
    return rows


def round_percent(correct, total):
    if total <= 0 or not 0 <= correct <= total:
        raise ValueError("Require 0 <= correct <= total and total > 0")
    return (Decimal(correct) * 100 / Decimal(total)).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


def matching_count(percent, total):
    """One possible integer count for a rounded rate; not an observed count."""
    value = Decimal(str(percent))
    if total <= 0 or not value.is_finite() or not 0 <= value <= 100:
        raise ValueError("Invalid percentage or denominator")
    center = int((value * total / 100).to_integral_value(rounding=ROUND_HALF_UP))
    return next((k for k in (center, center - 1, center + 1)
                 if 0 <= k <= total and round_percent(k, total) == value), None)


def minimum_common_denominator(percentages, max_total=1000):
    if not percentages or max_total < 1:
        raise ValueError("Require rates and a positive search limit")
    for total in range(1, max_total + 1):
        if all(matching_count(p, total) is not None for p in percentages):
            return total
    return None


def changes(value, baseline):
    value, baseline = Decimal(str(value)), Decimal(str(baseline))
    if not baseline > 0:
        raise ValueError("Relative change needs a positive baseline")
    return value - baseline, (value - baseline) / baseline * 100


def main():
    rows = load_results()
    print("PAPER-REPORTED AGGREGATES. No model or prediction records were evaluated.")
    print("Frame unit: author clarification; original evaluator remains unavailable.\n")
    print("Experiment | Top-1 (%) | change (pp) | relative change (%)")
    for r in rows:
        pp, relative = changes(r["top1_pct"], rows[0]["top1_pct"])
        print(f'{r["experiment_id"]} | {r["top1_pct"]:.2f} | {pp:+.2f} | {relative:+.2f}')
    denominators = [minimum_common_denominator([r[m] for r in rows]) for m in METRICS[1:]]
    print("\nMinimum common class denominators within 1..1000:", denominators)
    if all(n is not None for n in denominators):
        total = sum(denominators)
        for r in rows:
            counts = [matching_count(r[m], n) for m, n in zip(METRICS[1:], denominators)]
            compatible = round_percent(sum(counts), total) == r["top1_pct"]
            print(f'{r["experiment_id"]}: possible correct counts {counts}; '
                  f'overall {sum(counts)}/{total}; Top-1 compatible={compatible}')
    print("These are inferred compatible counts, NOT recovered frames or predictions.")
    print("All Top-1 rates compatible with one prediction/video for 21 videos:",
          all(matching_count(r["top1_pct"], 21) is not None for r in rows))


if __name__ == "__main__":
    main()
