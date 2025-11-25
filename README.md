# ll_story - Retail Inventory Turnover — 2024 Quarterly Analysis

**Contact:** 22f3001685@ds.study.iitm.ac.in

## Executive summary (TL;DR)
- Quarterly turnover (2024): Q1 -1.35, Q2 2.95, Q3 4.59, Q4 10.96.
- **Correct average (4-quarter mean, rounded to 2 dp): 4.29.**
- Industry benchmark target: 8.0.
- Business problem: Annual average (4.29) is **below** the industry target of 8, indicating excess inventory and opportunity cost.
- Recommended solution: **Optimize supply chain and demand forecasting** — specifically through improved demand forecasting, inventory segmentation, and replenishment optimization.

> This analysis and code were produced with LLM-assisted development (Jules / ChatGPT Codex) — see commit history for the labelled commits relating to LLM contributions.

---

## Files added
- `analysis.py` — Python analysis script that calculates metrics and creates charts.
- `analysis_results.csv` — generated numeric summary (quarter + average + target).
- `figures/inventory_turnover_trend.png` — time-series trend with industry target.
- `figures/inventory_vs_benchmark.png` — bar chart with per-quarter labels.
- `summary.txt` — short textual summary.
- `README.md` — this file.

---

## Key findings
1. **Volatility across quarters:** Turnover starts negative in Q1 (-1.35), recovers through Q2 (2.95) and Q3 (4.59), and spikes in Q4 (10.96). The huge Q4 value suggests seasonality or clearance actions driving turnover up.
2. **Average below target:** The computed average turnover is 4.29 (rounded to 2 dp) — **46%** of the industry target of 8.0. Sustained underperformance indicates systematic issues (forecasting, procurement, lead time, or SKU-level obsolescence).
3. **Q1 anomaly:** A negative Q1 typically indicates inventory write-offs, returns, or classification issues — this should be investigated at transaction level.

---

## Business implications
- Holding costs and working capital are likely elevated — capital tied up in inventory reduces ability to invest in growth.
- Low turnover across the year (outside Q4 spike) implies weak replenishment discipline or demand mismatch that could lead to markdowns and margin erosion.
- If Q4 spike is due to clearance, relying on clearance to correct inventory is risky and damages margins.

---

## Recommendations (actionable)
**Short-term (0–3 months)**
1. **Investigate Q1 negative value**: audit returns/write-offs/discrepancies; correct any misclassification.
2. **Perform SKU-level ABC/XYZ segmentation**: focus immediate actions on high-value, low-turn SKUs.
3. **Temporary assortment rationalization**: clear slow-moving SKUs with targeted promotions to free up storage and capital.

**Medium-term (3–9 months)**
4. **Improve demand forecasting using hybrid models**: combine time-series forecasting with LLM-assisted feature engineering (holiday/seasonality, promotions, web signals).
5. **Tighten reorder points and safety stock**: use probabilistic lead-time modeling and reduce excess safety stock for predictable SKUs.
6. **Vendor collaboration**: implement vendor-managed inventory or shorten lead-times where possible.

**Long-term (9–18 months)**
7. **Implement continuous monitoring dashboard**: track turnover, weeks of supply, and aging by SKU and category.
8. **Iteratively tune replenishment policies** using A/B experiments (alternate safety stocks, reorder frequencies).

---

## Why "optimize supply chain and demand forecasting"?
- Forecasting improvements reduce overordering and mismatch, directly increasing turnover without compromising service-levels.
- Supply chain optimization (lead-time reduction, vendor collaboration) reduces necessary safety stock and accelerates flow, improving turnover.

---

## How to reproduce
1. Clone repo.
2. Create a branch for this analysis:
   ```bash
   git checkout -b feature/llm-inventory-analysis
