#!/usr/bin/env python3
"""Render two static figures from the paper transcription, not invented runs."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
from audit_results import ROOT, load_results


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11,
                         "svg.fonttype": "none", "svg.hashsalt": "classlab-paper-results",
                         "axes.labelcolor": "#233446", "text.color": "#233446"})
    rows = load_results()
    output = ROOT / "assets/figures"
    output.mkdir(parents=True, exist_ok=True)
    for group, title, name in [
        ("single", "Single-factor augmentation", "single_factor_accuracy"),
        ("multi", "Multi-factor augmentation", "multi_factor_accuracy"),
    ]:
        selected = [r for r in rows if r["group"] in ("baseline", group)]
        fig, ax = plt.subplots(figsize=(12, 5.6 if group == "single" else 5.3))
        fig.subplots_adjust(left=0.35 if group == "multi" else 0.20, right=0.91, top=0.74, bottom=0.23)
        labels = []
        for r in selected:
            label = r["label"]
            if group == "multi":
                label = {"combo_a": "Camera + Clothing", "combo_b": "Camera + Clothing\n+ Background",
                         "combo_c": "Camera + Clothing\n+ Background + Hairstyle"}.get(r["experiment_id"], label)
            labels.append(label)
        values = [float(r["top1_pct"]) for r in selected]
        ax.barh(range(len(selected)), values, color=["#7A8997"] + ["#277DA8"] * (len(selected)-1), height=0.58)
        ax.set_yticks(range(len(selected)), labels)
        ax.invert_yaxis()
        ax.set_xlim(0, 100)
        ax.set_xticks([0, 20, 40, 60, 80, 100])
        ax.xaxis.set_major_formatter(PercentFormatter(100, decimals=0))
        ax.set_xlabel("Top-1 accuracy (%)", labelpad=10)
        ax.set_axisbelow(True)
        ax.grid(axis="x", color="#E0E5EB", linewidth=0.8)
        baseline = float(rows[0]["top1_pct"])
        ax.axvline(baseline, linestyle=(0, (4, 3)), color="#465563", linewidth=1.1, zorder=3)
        for i, value in enumerate(values):
            # Right column keeps long values away from the 100% axis boundary.
            ax.text(1.025, i, f"{value:.2f}%", va="center", transform=ax.get_yaxis_transform(), fontsize=11)
        ax.tick_params(axis="y", length=0, pad=13)
        ax.tick_params(axis="x", colors="#536171")
        for side in ("top", "right", "left"):
            ax.spines[side].set_visible(False)
        ax.spines["bottom"].set_color("#B8C3CF")
        fig.text(0.05, 0.92, title, fontsize=19, weight="bold")
        fig.text(0.05, 0.86, "Paper-reported results · Not independently reproduced", fontsize=12, color="#536171")
        budget = "90 real + 60 synthetic training videos per single factor." if group == "single" else "90 real + 120 / 180 / 240 synthetic videos; combination budgets differ."
        fig.text(0.05, 0.80, budget, fontsize=10.5, color="#536171")
        fig.text(0.05, 0.105, "Dashed line: real-only baseline (77.78%). Paper-reported rates; saved records are audited separately.", fontsize=9.7)
        source = "Section IV-B and Table VII" if group == "single" else "Section IV-B and Table VIII"
        fig.text(0.05, 0.055, f"Source: supplied manuscript, {source}. See docs/DRIVE_AUDIT.md for counts and version differences.", fontsize=9.7, color="#536171")
        destination = output / f"{name}.svg"
        fig.savefig(destination, metadata={"Date": None, "Creator": "paper-reported result chart"})
        # Matplotlib inserts trailing spaces in SVG path lines; normalize for Git.
        destination.write_text("\n".join(line.rstrip() for line in destination.read_text().splitlines()) + "\n")
        plt.close(fig)
        print(output / f"{name}.svg")


if __name__ == "__main__":
    main()
