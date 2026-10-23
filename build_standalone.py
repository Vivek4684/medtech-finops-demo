#!/usr/bin/env python3
"""Inline Chart.js + data into a single self-contained HTML file."""
import pathlib

root = pathlib.Path(__file__).parent
html = (root / "FinOps_Dashboard.html").read_text()
chartjs = (root / "data" / "chart.umd.min.js").read_text()
embed = (root / "data" / "_embed.js").read_text()

chart_tag = '<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.1/dist/chart.umd.min.js"></script>'
data_tag = '<script src="data/_embed.js"></script>'

assert chart_tag in html, "chart tag not found"
assert data_tag in html, "data tag not found"

html = html.replace(
    chart_tag,
    "<script>\n/* Chart.js v4.4.1 (inlined, MIT License, https://www.chartjs.org/) */\n"
    + chartjs + "\n</script>")

html = html.replace(
    data_tag,
    "<script>\n/* Embedded dummy FinOps data */\n" + embed + "\n</script>")

out = root / "FinOps_Dashboard_Standalone.html"
out.write_text(html)
print(f"Wrote {out} ({len(html):,} bytes)")
assert "FINOPS_DATA" in html and "Chart.js v4.4.1" in html
print("Inlining verified.")
