"""
analysis.py
Retail Inventory Turnover Analysis (Quarterly 2024)

Generates:
 - metrics printed to console
 - time-series chart saved as 'figures/inventory_turnover_trend.png'
 - bar chart vs benchmark saved as 'figures/inventory_vs_benchmark.png'

This analysis was produced with programmatic assistance from LLM tooling
(e.g., Jules / ChatGPT Codex). Contact: 22f3001685@ds.study.iitm.ac.in
"""

from pathlib import Path
import math
import matplotlib.pyplot as plt
import csv

# --- Data (quarterly 2024) ---
quarters = ["Q1 2024", "Q2 2024", "Q3 2024", "Q4 2024"]
values = [-1.35, 2.95, 4.59, 10.96]
industry_target = 8.0

# Ensure output directories exist
out_dir = Path("figures")
out_dir.mkdir(parents=True, exist_ok=True)

# --- Compute metrics carefully (digit-by-digit reasoning done programmatically) ---
n = len(values)
total = sum(values)  # -1.35 + 2.95 + 4.59 + 10.96 = 17.15
average_raw = total / n  # 17.15 / 4 = 4.2875
average_rounded = round(average_raw, 2)  # 4.29

# Print metrics
print("Quarterly Inventory Turnover (2024):")
for q, v in zip(quarters, values):
    print(f"  {q}: {v:.2f}")
print(f"Total (sum of quarters): {total:.2f}")
print(f"Average turnover (raw): {average_raw}")
print(f"Average turnover (rounded to 2 dp): {average_rounded:.2f}")

# --- Save computed numbers as CSV for reproducibility ---
csv_path = Path("analysis_results.csv")
with csv_path.open("w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["quarter", "turnover"])
    for q, v in zip(quarters, values):
        writer.writerow([q, v])
    writer.writerow(["average", f"{average_rounded:.2f}"])
    writer.writerow(["industry_target", f"{industry_target:.2f}"])
print(f"Wrote CSV summary to {csv_path}")

# --- Visualization 1: Trend line with benchmark ---
plt.figure(figsize=(8, 4.5))
plt.plot(quarters, values, marker='o', linewidth=2)
plt.axhline(industry_target, linestyle='--', linewidth=1.5, label=f'Industry target = {industry_target:.0f}')
plt.title("Inventory Turnover Ratio — 2024 Quarterly Trend")
plt.ylabel("Inventory Turnover Ratio")
plt.ylim(min(min(values), industry_target) - 2, max(max(values), industry_target) + 2)
plt.grid(axis='y', alpha=0.3)
plt.legend()
plt.tight_layout()
trend_path = out_dir / "inventory_turnover_trend.png"
plt.savefig(trend_path, dpi=150)
plt.close()
print(f"Saved trend chart to {trend_path}")

# --- Visualization 2: Bar chart comparing each quarter + target ---
plt.figure(figsize=(8, 4.5))
bars = plt.bar(quarters, values)
# Highlight Q4 (strong spike)
bars[-1].set_edgecolor('black')
bars[-1].set_linewidth(1.5)
plt.axhline(industry_target, color='gray', linestyle='--', linewidth=1.5, label=f'Target = {industry_target:.0f}')
plt.title("Inventory Turnover by Quarter (2024) vs Industry Target")
plt.ylabel("Inventory Turnover Ratio")
plt.ylim(min(min(values), industry_target) - 2, max(max(values), industry_target) + 4)
plt.legend()
for i, v in enumerate(values):
    plt.text(i, v + 0.2 if v >= 0 else v - 0.6, f"{v:.2f}", ha='center', va='bottom' if v>=0 else 'top')
plt.tight_layout()
bars_path = out_dir / "inventory_vs_benchmark.png"
plt.savefig(bars_path, dpi=150)
plt.close()
print(f"Saved bar chart to {bars_path}")

# --- Short narrative summary saved as text for convenience (could be used in README) ---
summary_text = f"""
Inventory Turnover — 2024 Quarterly Summary
-------------------------------------------
Quarters: {', '.join(quarters)}
Values: {', '.join(f'{v:.2f}' for v in values)}
Average (4 quarter mean, rounded to 2 dp): {average_rounded:.2f}
Industry target: {industry_target:.2f}
Observations:
 - Large negative turnover in Q1 ({values[0]:.2f}) likely indicates returns, accounting adjustments, or write-offs.
 - Progressive recovery Q2/Q3, with a large spike in Q4 ({values[3]:.2f}) pushing the annual average above 4.
 - Average turnover (4.29) remains below industry target (8.0), implying excess inventory / suboptimal turnover.
"""
with open("summary.txt", "w") as f:
    f.write(summary_text.strip())
print("Wrote textual summary to summary.txt")

print("\nAnalysis complete. Files created:")
print(" - analysis_results.csv")
print(f" - {trend_path}")
print(f" - {bars_path}")
print(" - summary.txt")
