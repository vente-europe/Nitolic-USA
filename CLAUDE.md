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
- **Data source:** `Data/x-ray/Lice-US-x-ray.csv` — 60 ASINs, 22 brands

---

## Tab Structure

| Tab | Content |
|-----|---------|
| 1 — Main Segments (Total Market) | KPIs, Focus split (Prevention/Treatment), seasonality charts |
| 2 — Market Structure (Prevention) | Prevention segment breakdown by type, top products |
| 3 — Market Structure (Treatment) | Treatment segment breakdown by type, top products |
| 4 — Treatment Method | Treatment method analysis |
| 5 — Reviews | Review distribution across ASINs, star ratings |
| 6 — Search Volume | SV trends by segment (Prevention/Treatment/General), 3 views + methodology |
| 7 — Reviews VOC | Voice of Customer analysis from 705 competitor reviews (see below) |

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

### Market figures (12M, seasonality-adjusted from 30d X-Ray):
- Total units: 1,001,135 · Total revenue: $21.3M · Avg price: $21.32
- Prevention: 450,987 units (45.1%) · $9.6M · avg price varies
- Treatment: 550,148 units (54.9%) · $11.7M · avg price varies

### Seasonality approach (for ASINs without sales-unit files):
- Start from X-Ray ASIN Sales (last 30 days) as anchor
- Determine which month the X-Ray was exported → find that month's seasonality index
- Back-calculate baseline: `baseline = 30d_sales / month_index`
- Apply all month indices to get monthly projections
- Seasonality indices derived from 17+17 ASINs with actual daily sales data (42 files total)

---

## Source Data

| Path | Description |
|------|-------------|
| `Data/sales-units/` | Per-ASIN sales CSVs (H10 Xray) — not git tracked |
| `Data/x-ray/` | Full X-Ray export (CSV) — not git tracked |
| `Data/reviews/` | Amazon review scraper JSONs — not git tracked |
| `Data/sv/` | Search Volume CSVs by segment (general/, prevention/, treatment/) — not git tracked |

---

## Known Bugs & Fixes

- **Month label quoting bug (2026-03-19):** `rebuild-dashboard.js` used `jsStrArr()` with single quotes, breaking JS when month labels contained apostrophes (e.g. `Mar'25`). Fix: use double quotes in generated arrays. Original hand-written dashboard didn't have this issue.
- **Model ID for API calls:** `claude-sonnet-4-5-20250929` is the correct model ID for Anthropic API. Other formats (`claude-sonnet-4-6-*`, `claude-sonnet-4-5-20241022`) return 404.

---

## Tab 7 — Reviews VOC

Uses the **data-driven template** from `tab_templates/tabs/reviews-voc.html`. Only `VOC_DATA` was customised.

**How this tab was built (do NOT use API calls — analyse reviews in-context):**
1. Read all reviews from `Data/reviews/reviews_nitolic_competitors.json` (705 reviews, stars + text)
2. Tag reviews by keyword matching (regex patterns for themes like ineffective, smell_bad, school_lice, etc.)
3. Analyse all reviews directly in Claude Code context (read samples of 1★, 2★, 3★, 4★, 5★)
4. Write VOC_DATA object manually based on analysis — all sections filled from actual review content
5. Generate tagged reviews array (`REVIEWS_RAW`) via `gen-reviews.js` for the Review Browser
6. Insert both `REVIEWS_RAW` and `VOC_DATA` + rendering engine into `index.html` as a new panel

**Data source:** `Data/reviews/reviews_nitolic_competitors.json` — 705 reviews, avg 2.75★

**VOC_DATA sections:**
- `totalReviews`, `avgRating`, `starDist` — basic stats
- `cpSummary`, `cpWho/When/Where/What` — Customer Profile (4 stacked bar charts)
- `usageScenarios` — 8 real-world use cases
- `csSummary`, `negativeTopics`, `positiveTopics` — expandable sentiment topics with bullets + quotes
- `negativeInsights`, `positiveInsights` — CPG/Amazon strategy tables (badges + findings + implications)
- `buyersMotivation` — 9 purchase triggers
- `customerExpectations` — 9 unmet needs
- `themeFilters`, `tagStyles` — Review Browser filter config
- `reviews` — loaded from `REVIEWS_RAW` (300 tagged reviews for browser)

**Key rule:** To update this tab, ONLY edit the `VOC_DATA` block and `REVIEWS_RAW` array. Never modify the rendering engine below.

**Helper scripts (not git tracked):**
- `gen-reviews.js` — generates `REVIEWS_RAW` JS array from `tagged-reviews.json`
- `build-voc-tab.js` — attempted API-based analysis (deprecated — direct in-context analysis is faster and more reliable)

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
