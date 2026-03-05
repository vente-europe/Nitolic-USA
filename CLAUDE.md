# Dashboard — Nitolic US

> **Living document** — Update after every bug fix or new pattern found. No permission needed for additions. Ask before removing.

---

## Language
All content in this project (visualizations, labels, comments, documentation) must be in **English**.

---

## Project Overview

- **Purpose:** Amazon US market analysis dashboard — Nitolic category
- **Active file:** `index.html` (dashboard root)
- **Git repo:** root of this folder
- **Tech stack:** HTML + vanilla JS, Chart.js 4.4.0 + chartjs-plugin-datalabels 2.2.0, no build step
- **Based on:** `_template/` (adapted — no pack sizes; uses Type + Focus dimensions instead)
- **Data source:** `Data/x-ray/Main-Xray_Nitolic_2026-03-01.csv` — 34 ASINs, 17 brands

---

## Tab Structure

| Tab | Content |
|-----|---------|
| 1 — Market Overview | KPIs, Focus split (Prevention/Treatment), Top 10 ASINs bar |
| 2 — Product Type | Revenue/units by Type (All-in-One, Conditioner, Set, Kit, Shampoo, Spray) |
| 3 — Prevention vs Treatment | Head-to-head comparison, type mix within each focus, top products |
| 4 — Brands | Brand revenue bar, brand summary table (17 brands) |
| 5 — All Products | Full sortable table of all 34 ASINs |

## Key Data Dimensions

- **Type** (product form): All-in-One, Conditioner, Set, Kit, Shampoo, Spray — replaces pack size
- **Focus**: Prevention vs Treatment — main market split
- All-in-One and Kit = Treatment only; Conditioner, Set, Spray = Prevention only; Shampoo = both

## Data Sources

| Source | What it contains | Use for |
|--------|-----------------|---------|
| `Data/x-ray/` CSV | **Last 30-day snapshot** — ALL columns reflect the 30-day window at export time | ASIN metadata only: Price, Brand, Title, Rating, Reviews, BSR, Age |
| `Data/sales-units/[ASIN]-sales-3y.csv` | **Full historical daily units** with dates — `Sales` column = units sold that day | 12M sales calculations |

## Data Convention — 12M

**All sales and revenue = 12-month totals.** Every chart title includes "(12M)".

- **12M Units** = sum of `Sales` column for dates in the last 12M window (from export date)
- **12M Revenue** = 12M units × ASIN listed price from X-Ray
- **Never use X-Ray "ASIN Sales" or "ASIN Revenue" for 12M** — both are 30-day figures
- New ASINs may not have full 12M of history in sales files — sum what's available, that IS their 12M

### Market figures (12M, Mar 2025 – Feb 2026):
- Total units: 778,443 · Total revenue: $16.4M · Avg price: $21.05
- Prevention: 340,275 units (43.7%) · $5.94M (36.3%) · avg price $17.46
- Treatment: 438,168 units (56.3%) · $10.44M (63.7%) · avg price $23.84

---

## Source Data

| Path | Description |
|------|-------------|
| `Data/sales-units/` | Per-ASIN sales CSVs (H10 Xray) — not git tracked |
| `Data/x-ray/` | Full X-Ray export (CSV) — not git tracked |
| `Data/reviews/` | Amazon review scraper JSONs — not git tracked |

---

## Known Bugs & Fixes

*(None yet — update as work progresses)*

---

## Chart Insertion Rule

**When adding a new chart to any existing section:**
- **NEVER remove or replace existing charts or content**
- **ALWAYS insert the new chart below existing charts and push everything else down**
- This applies even if the user says "add here" — preserve all existing elements, only insert

## Self-Update Rules

**Update this file when:**
- Dashboard is built → add active file path and tab structure
- A bug is found and fixed → add to Known Bugs & Fixes
- New data is added → update Source Data table

**Ask before:**
- Removing existing entries
- Changing core structure
