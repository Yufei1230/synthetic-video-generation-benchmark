#!/usr/bin/env python3
"""Plot paper aggregates beside independently recounted saved-output records."""
import csv
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]


def main():
    with (ROOT / "experiments/paper_reported_results.csv").open(newline="") as f:
        paper = list(csv.DictReader(f))
    with (ROOT / "experiments/recovered/results.csv").open(newline="") as f:
        saved = list(csv.DictReader(f))
    labels = ["Real only", "Camera angle", "Clothing", "Background", "Hairstyle",
              "Camera + Clothing", "Camera + Clothing + Background", "All four factors"]
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 10,
                         "svg.hashsalt": "paper-saved-comparison-v1"})
    fig, ax = plt.subplots(figsize=(11, 6.1), facecolor="white")
    for i, row in enumerate(paper):
        values = [float(s["top1_pct"]) for s in saved if s["paper_experiment_id"] == row["experiment_id"]]
        ax.scatter(float(row["top1_pct"]), i - .13, marker="o", s=58, facecolor="white",
                   edgecolor="#64748b", linewidth=1.5, label="Paper" if i == 0 else None, zorder=3)
        ax.annotate(f'{float(row["top1_pct"]):.2f}', (float(row["top1_pct"]), i - .13),
                    xytext=(-6, -1), textcoords="offset points", ha="right", va="center", fontsize=9, color="#475569")
        for j, value in enumerate(values):
            color = "#0f766e" if j == 0 else "#c2410c"
            ax.scatter(value, i + .13, marker="D" if j == 0 else "s", s=45, color=color,
                       label="Saved predictions" if i == 0 else "Earlier three-factor version" if j == 1 else None, zorder=3)
            ax.annotate(f"{value:.2f}", (value, i + .13), xytext=(-6, -1), textcoords="offset points",
                        ha="right", va="center", fontsize=9, color=color)
        if not values:
            ax.text(5, i + .13, "Prediction export not recovered", fontsize=9, color="#64748b", va="center")
    ax.set_yticks(range(len(labels)), labels)
    ax.set_ylim(7.6, -.6); ax.set_xlim(0, 100)
    ax.set_xlabel("Top-1 accuracy (%)")
    ax.grid(axis="x", color="#e2e8f0", linewidth=.7); ax.set_axisbelow(True)
    for side in ("top", "right", "left"): ax.spines[side].set_visible(False)
    ax.spines["bottom"].set_color("#cbd5e1"); ax.tick_params(axis="y", length=0, pad=10)
    fig.suptitle("Paper results and recovered experiment records", x=.03, ha="left", fontsize=16, weight="bold", color="#0f172a")
    ax.legend(loc="upper center", bbox_to_anchor=(.5, 1.14), ncol=3, frameon=False, fontsize=9)
    fig.text(.03, .045, "Saved exports recounted; models not rerun. One clip prediction is repeated across 32 sampled-frame rows.", fontsize=9, color="#475569")
    fig.text(.03, .018, "Different source versions and dataset sizes limit direct comparison. See docs/DRIVE_AUDIT.md.", fontsize=9, color="#475569")
    fig.subplots_adjust(left=.32, right=.965, top=.81, bottom=.15)
    target=ROOT / "assets/figures/paper_vs_saved_results.svg"
    fig.savefig(target, metadata={"Date": None}, facecolor="white")
    target.write_text("\n".join(line.rstrip() for line in target.read_text().splitlines())+"\n")
    plt.close(fig)
    print(f"Wrote {target.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
