# MedTech Data Platform — FinOps Demo

A self-contained dashboard + Excel dataset to demonstrate **FinOps visibility of a data-platform
technology stack** across sectors and projects. All figures are **dummy data** reconciling to a
**~$20M** annual data-platform budget.

## What's in this folder

| File | Purpose |
|------|---------|
| **`FinOps_Dashboard_Standalone.html`** | ⭐ **The demo.** Fully self-contained — Chart.js and all data are embedded. **Just double-click to open in Chrome.** No server, no internet, works offline. |
| `FinOps_Dashboard.html` | Same dashboard but loads data/chart from `data/` (dev version; needs a local web server). |
| `data/finops_data.xlsx` | The "source of truth" workbook for the Chief — 6 tabs incl. raw data, with native Excel charts. |
| `data/finops_data.json` | The structured data the dashboard reads. |
| `generate_finops_data.py` | Regenerates the Excel + JSON (edit numbers here). |
| `build_standalone.py` | Rebuilds the standalone HTML after regenerating data. |

> For the demo, you only need **`FinOps_Dashboard_Standalone.html`** and, optionally,
> **`data/finops_data.xlsx`** to show the underlying numbers.

## The three-level drill-down (the Chief's ask)

1. **Enterprise Overview** — total ~$20M, split into **Shared/Enterprise** (licenses + platform)
   vs **Sector-Attributed**, with spend by technology and fully-loaded cost by sector.
2. **Click a technology** (e.g. Databricks) → its spend **across the 4 sectors**, plus the
   **projects driving that cost**.
   **Click a sector** (e.g. Commercial) → its platforms and projects.
3. **Click/double-click a project** (CDL, Radar, STAR, Datavantage, Artemis/Hubble)
   → the **platforms driving that project's cost** and its monthly trend.

Breadcrumbs at the top let you jump back up at any level.

## Cost model (talking points for the Chief)

- **13 line items:** AWS, Databricks, Snowflake, Informatica, Power BI, Tableau, Confluent Kafka,
  Fivetran, Denodo, Collibra, dbt Cloud + an **"Other / Everything Else"** catch-all so the numbers
  always reconcile to the full budget.
- **Two cost buckets per technology:**
  - *Shared / Enterprise* — enterprise licenses + platform base fees (a shared pool).
  - *Sector-Attributed* — direct consumption, split across Supply Chain, Commercial, R&D, Enterprise.
- **Fully-loaded sector view:** the shared pool is **also allocated to sectors** (70% by consumption,
  30% evenly) — a FinOps hallmark that shows true cost per sector. The 4 fully-loaded sector numbers
  sum back to the ~$20M total.
- **Sectors:** Supply Chain · Commercial · R&D · Enterprise.
- **Projects → sector:** CDL → Supply Chain · Radar → R&D · STAR, Datavantage, Artemis/Hubble → Commercial.
  Each sector also has an *"Other … Projects"* catch-all.
- **12-month trend** on the enterprise, per-technology, and per-project views.

## How to change the numbers

```bash
# from this folder
PYTHONPATH=./.pylibs python3 generate_finops_data.py   # regenerates xlsx + json
python3 build_standalone.py                            # rebuilds the standalone HTML
```

Edit the `TECHS`, `PROJECTS`, sector weights, or `shared_frac` values near the top of
`generate_finops_data.py` to retune the story. The script asserts the technology totals sum to $20M.

---
*Illustrative dummy data for solution demonstration. Chart.js (MIT License) is embedded in the
standalone file for offline use.*
