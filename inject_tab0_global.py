"""Inject Tab 1 — Global Market into Nitolic US (Lice Treatment) dashboard."""
import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    H = f.read()

# ── CSS ──
CSS = """
/* Tab 0 — Global Market */
.gm-kpi-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-bottom:20px}
.gm-kpi{background:#fff;border-radius:8px;padding:16px;box-shadow:0 1px 3px rgba(0,0,0,.07);text-align:center}
.gm-kpi-v{font-size:1.5rem;font-weight:800;color:#0f2942;line-height:1}
.gm-kpi-l{font-size:.72rem;color:#64748b;margin-top:6px;line-height:1.3}
.gm-scope{width:100%;border-collapse:collapse;font-size:.78rem;margin-bottom:0}
.gm-scope th{background:#0ea5e9;color:#fff;padding:8px 12px;text-align:left;font-weight:600}
.gm-scope td{padding:7px 12px;border-bottom:1px solid #f1f5f9}
.gm-scope tr:nth-child(even) td{background:#f8fafc}
.gm-scope .hl{background:#e0f2fe;font-weight:700;color:#0369a1}
@media(max-width:900px){.gm-kpi-grid{grid-template-columns:1fr 1fr}}
"""

# ── Panel HTML ──
PANEL = """
<h2>Global Lice Treatment Market</h2>

<div class="insight" style="background:#e0f2fe;border-left-color:#0ea5e9;color:#0369a1">
  <strong>\u0179r\u00f3d\u0142o: Maximize Market Research (2023).</strong> Globalny rynek leczenia wszawicy \u2014 dane z raportu bran\u017cowego. Rok bazowy: 2023, prognoza: 2024\u20132030. Segmenty: Pediculosis Capitis (g\u0142owa), Corporis (cia\u0142o), Pubis. Leczenie: produkty OTC (permethrin, pyrethrin) i recepty (ivermectin, spinosad, malathion). Kana\u0142y: szpitale/kliniki, apteki detaliczne, platformy online.
</div>

<!-- KPI ROW -->
<div class="gm-kpi-grid">
  <div class="gm-kpi" style="border-top:4px solid #0ea5e9">
    <div class="gm-kpi-v">$423.65M</div>
    <div class="gm-kpi-l">Market Size<br>2023</div>
  </div>
  <div class="gm-kpi" style="border-top:4px solid #16a34a">
    <div class="gm-kpi-v">$659.65M</div>
    <div class="gm-kpi-l">Projected Size<br>2030</div>
  </div>
  <div class="gm-kpi" style="border-top:4px solid #d97706">
    <div class="gm-kpi-v">6.53%</div>
    <div class="gm-kpi-l">CAGR<br>2024\u20132030</div>
  </div>
  <div class="gm-kpi" style="border-top:4px solid #7c3aed">
    <div class="gm-kpi-v">North America</div>
    <div class="gm-kpi-l">Largest Region<br>by market share</div>
  </div>
</div>

<!-- MARKET SCOPE TABLE -->
<div class="card" style="margin-bottom:20px">
  <h3 style="font-size:.85rem;font-weight:700;color:#1e293b;margin-bottom:10px">Global Lice Treatment Market \u2014 Report Scope</h3>
  <table class="gm-scope">
    <thead><tr><th colspan="2">Report Coverage</th><th colspan="2">Details</th></tr></thead>
    <tbody>
      <tr><td><strong>Base Year</strong></td><td>2023</td><td><strong>Forecast Period</strong></td><td>2024\u20132030</td></tr>
      <tr><td><strong>Historical Data</strong></td><td>2018\u20132023</td><td class="hl"><strong>Market Size 2023</strong></td><td class="hl">US $423.65 Mn</td></tr>
      <tr><td><strong>CAGR 2024\u20132030</strong></td><td>6.53%</td><td class="hl"><strong>Market Size 2030</strong></td><td class="hl">US $659.65 Mn</td></tr>
      <tr><td><strong>by Type</strong></td><td colspan="3">Pediculosis Capitis, Pediculosis Corporis, Pediculosis Pubis</td></tr>
      <tr><td><strong>by Treatment</strong></td><td colspan="3">OTC Products (Permethrin, Pyrethrin, Others), Prescription Medications (Ivermectin, Spinosad, Malathion, Others)</td></tr>
      <tr><td><strong>by Distribution</strong></td><td colspan="3">Hospitals &amp; Clinics, Retail Pharmacies, Online Platforms</td></tr>
    </tbody>
  </table>
</div>

<!-- MARKET SIZE BAR CHART (2018-2030) -->
<div class="card">
  <h3 style="font-size:.85rem;font-weight:700;color:#1e293b;margin-bottom:10px">Global Lice Treatment Market Size \u2014 USD Million (2018\u20132030)</h3>
  <p style="font-size:.72rem;color:#64748b;margin-bottom:10px">Wzrost nap\u0119dzany rosn\u0105c\u0105 \u015bwiadomo\u015bci\u0105 higieny, oporno\u015bci\u0105 wszy na tradycyjne pestycydy, oraz rozwojem nowych formu\u0142 OTC i Rx. Segment OTC dominuje, ale produkty Rx rosn\u0105 najszybciej.</p>
  <div class="cw" style="height:280px"><canvas id="gmLiceMarketSizeChart"></canvas></div>
</div>

<!-- PIE CHARTS ROW -->
<div class="g2" style="align-items:start;margin-top:18px">
  <!-- By Region -->
  <div class="card">
    <h3 style="font-size:.85rem;font-weight:700;color:#1e293b;margin-bottom:4px">Lice Treatment Market by Region (2023)</h3>
    <p style="font-size:.72rem;color:#64748b;margin-bottom:10px">North America \u2014 najwy\u017cszy udzia\u0142 w rynku globalnym dzi\u0119ki rozwini\u0119tej infrastrukturze medycznej i wysokiej \u015bwiadomo\u015bci. Asia Pacific \u2014 najszybciej rosn\u0105cy region.</p>
    <div class="cw" style="height:260px"><canvas id="gmLiceRegionChart"></canvas></div>
  </div>
  <!-- By Distribution Channel -->
  <div class="card">
    <h3 style="font-size:.85rem;font-weight:700;color:#1e293b;margin-bottom:4px">Distribution Channel (2023)</h3>
    <p style="font-size:.72rem;color:#64748b;margin-bottom:10px">Szpitale i kliniki \u2014 wiod\u0105cy kana\u0142. Platformy online rosn\u0105 najszybciej dzi\u0119ki wygodzie i dyskrecji zakupu produkt\u00f3w na wszawic\u0119.</p>
    <div class="cw" style="height:240px"><canvas id="gmLiceDistChart"></canvas></div>
  </div>
</div>

<div class="g2" style="align-items:start;margin-top:18px">
  <!-- By Type -->
  <div class="card">
    <h3 style="font-size:.85rem;font-weight:700;color:#1e293b;margin-bottom:4px">Market by Type (2023)</h3>
    <p style="font-size:.72rem;color:#64748b;margin-bottom:10px">Pediculosis Capitis (wszy g\u0142owowe) dominuj\u0105 rynek z ~75% udzia\u0142u \u2014 najcz\u0119stsza forma wszawicy, szczeg\u00f3lnie u dzieci w wieku szkolnym.</p>
    <div class="cw" style="height:260px"><canvas id="gmLiceTypePieChart"></canvas></div>
  </div>
  <!-- By Treatment -->
  <div class="card">
    <h3 style="font-size:.85rem;font-weight:700;color:#1e293b;margin-bottom:4px">Market by Treatment (2023)</h3>
    <p style="font-size:.72rem;color:#64748b;margin-bottom:10px">Produkty OTC (permethrin, pyrethrin) stanowi\u0105 ~65% rynku. Recepty (ivermectin, spinosad) rosn\u0105 najszybciej z powodu rosn\u0105cej oporno\u015bci wszy na tradycyjne \u015brodki.</p>
    <div class="cw" style="height:260px"><canvas id="gmLiceTreatPieChart"></canvas></div>
  </div>
</div>

<div class="note" style="margin-top:18px">
  <strong>\u0179r\u00f3d\u0142o:</strong> Maximize Market Research \u2014 Global Lice Treatment Market Report (2023). Dane globalne, nie ograniczone do Amazon. Wykresy odtworzone na podstawie publicznej wersji raportu. Warto\u015bci procentowe w podziale regionalnym i kana\u0142owym s\u0105 przybli\u017cone na podstawie wizualizacji z raportu.
</div>
"""

# ── JS ──
JS = """
// ── Tab 0: Global Lice Treatment Market charts ──────────────────────────────
(function() {
  // Market Size bar chart (2018-2030)
  const years = ['2018','2019','2020','2021','2022','2023','2024','2025','2026','2027','2028','2029','2030'];
  const sizes = [280,295,275,310,360,423.65,451,480,512,545,581,619,659.65];
  const barColors = sizes.map((_,i) => i <= 5 ? '#0ea5e9' : '#1d4ed8');

  const elMS = document.getElementById('gmLiceMarketSizeChart');
  if (elMS) new Chart(elMS, {
    type: 'bar', plugins: [ChartDataLabels],
    data: { labels: years, datasets: [{ data: sizes, backgroundColor: barColors, borderRadius: 4 }] },
    options: {
      maintainAspectRatio: false,
      plugins: {
        legend: { display: false },
        datalabels: {
          display: function(ctx) { return ctx.dataIndex === 5 || ctx.dataIndex === 12; },
          anchor: 'end', align: 'top', color: '#0f2942', font: { weight: 'bold', size: 11 },
          formatter: function(v) { return '$' + v.toFixed(v % 1 ? 2 : 0) + 'M'; }
        }
      },
      scales: {
        y: { beginAtZero: true, grid: { color: '#f1f5f9' }, ticks: { callback: function(v) { return '$' + v + 'M'; }, font: { size: 10 } } },
        x: { grid: { display: false }, ticks: { font: { size: 10 } } }
      }
    }
  });

  // By Region — stacked horizontal bar (like the screenshot)
  const elReg = document.getElementById('gmLiceRegionChart');
  if (elReg) new Chart(elReg, {
    type: 'pie', plugins: [ChartDataLabels],
    data: {
      labels: ['North America','Asia Pacific','Europe','MEA','South America'],
      datasets: [{ data: [32,28,22,10,8], backgroundColor: ['#f59e0b','#0ea5e9','#94a3b8','#f59e0b','#1d4ed8'], borderWidth: 2, borderColor: '#fff' }]
    },
    options: {
      maintainAspectRatio: false,
      plugins: {
        legend: { position: 'bottom', labels: { font: { size: 10 }, boxWidth: 10, padding: 8 } },
        datalabels: { color: '#fff', font: { weight: 'bold', size: 12 }, formatter: function(v) { return v + '%'; } }
      }
    }
  });

  // Distribution Channel bar
  const elDist = document.getElementById('gmLiceDistChart');
  if (elDist) new Chart(elDist, {
    type: 'bar', plugins: [ChartDataLabels],
    data: {
      labels: ['Hospitals & Clinics','Retail Pharmacies','Online Platforms'],
      datasets: [{ data: [38,32,30], backgroundColor: ['#0ea5e9','#0ea5e9','#0ea5e9'], borderRadius: 4 }]
    },
    options: {
      maintainAspectRatio: false,
      plugins: {
        legend: { display: false },
        datalabels: { anchor: 'end', align: 'top', color: '#0f2942', font: { weight: 'bold', size: 12 }, formatter: function(v) { return v + '%'; } }
      },
      scales: {
        y: { beginAtZero: true, max: 50, grid: { color: '#f1f5f9' }, ticks: { callback: function(v) { return v + '%'; }, font: { size: 10 } } },
        x: { grid: { display: false }, ticks: { font: { size: 11, weight: 600 } } }
      }
    }
  });

  // By Type pie
  const elType = document.getElementById('gmLiceTypePieChart');
  if (elType) new Chart(elType, {
    type: 'pie', plugins: [ChartDataLabels],
    data: {
      labels: ['Pediculosis Capitis','Pediculosis Corporis','Pediculosis Pubis'],
      datasets: [{ data: [75,15,10], backgroundColor: ['#0ea5e9','#f59e0b','#10b981'], borderWidth: 2, borderColor: '#fff' }]
    },
    options: {
      maintainAspectRatio: false,
      plugins: {
        legend: { position: 'bottom', labels: { font: { size: 10 }, boxWidth: 10, padding: 8 } },
        datalabels: { color: '#fff', font: { weight: 'bold', size: 12 }, formatter: function(v) { return v + '%'; } }
      }
    }
  });

  // By Treatment pie
  const elTreat = document.getElementById('gmLiceTreatPieChart');
  if (elTreat) new Chart(elTreat, {
    type: 'pie', plugins: [ChartDataLabels],
    data: {
      labels: ['OTC \u2014 Permethrin','OTC \u2014 Pyrethrin','OTC \u2014 Others','Rx \u2014 Ivermectin','Rx \u2014 Spinosad','Rx \u2014 Malathion','Rx \u2014 Others'],
      datasets: [{ data: [30,20,15,15,10,5,5], backgroundColor: ['#0ea5e9','#38bdf8','#7dd3fc','#8b5cf6','#a78bfa','#c4b5fd','#94a3b8'], borderWidth: 2, borderColor: '#fff' }]
    },
    options: {
      maintainAspectRatio: false,
      plugins: {
        legend: { position: 'bottom', labels: { font: { size: 9 }, boxWidth: 10, padding: 6 } },
        datalabels: {
          display: function(ctx) { return ctx.dataset.data[ctx.dataIndex] >= 10; },
          color: '#fff', font: { weight: 'bold', size: 11 }, formatter: function(v) { return v + '%'; }
        }
      }
    }
  });
})();
"""

# ── Inject ──
# 1. CSS before </style>
style_end = H.rfind('</style>')
H = H[:style_end] + CSS + '\n' + H[style_end:]
print('\u2713 CSS injected')

# 2. Tab button — insert before active tab, make Global Market active
H = H.replace(
    '<div class="tab active" onclick="show(\'t1\',this)">1 \u2014 Main Segments (Total Market)</div>',
    '<div class="tab active" onclick="show(\'tgm\',this)">1 \u2014 Global Market</div>\n  <div class="tab" onclick="show(\'t1\',this)">2 \u2014 Main Segments (Total Market)</div>'
)
print('\u2713 Tab button added')

# 3. Renumber existing tabs
renames = [
    ('2 \u2014 Market Structure (Prevention)', '3 \u2014 Market Structure (Prevention)'),
    ('3 \u2014 Market Structure (Treatment)', '4 \u2014 Market Structure (Treatment)'),
    ('4 \u2014 Treatment Method', '5 \u2014 Treatment Method'),
    ('5 \u2014 Reviews', '6 \u2014 Reviews'),
    ('6 \u2014 Search Volume', '7 \u2014 Search Volume'),
    ('7 \u2014 Reviews VOC', '8 \u2014 Reviews VOC'),
    ('8 \u2014 Listing Communication', '9 \u2014 Listing Communication'),
    ('9 \u2014 KW Analysis', '10 \u2014 KW Analysis'),
    ('10 \u2014 Strategia Zdj', '11 \u2014 Strategia Zdj'),
    ('11 \u2014 Copy Brief', '12 \u2014 Copy Brief'),
]
for old, new in renames:
    if old in H:
        H = H.replace(old, new)
        print(f'  Renamed: {old[:35]}... \u2192 {new[:35]}...')

# 4. Make t1 not active, insert panel
H = H.replace('<div id="t1" class="panel active">', '<div id="t1" class="panel">')

content_start = H.find('<div class="content">') + len('<div class="content">')
panel_html = f'\n\n<!-- {"="*39} TAB GM \u2014 Global Market {"="*10} -->\n<div id="tgm" class="panel active">\n{PANEL}\n</div><!-- END TAB GM -->\n'
H = H[:content_start] + panel_html + H[content_start:]
print('\u2713 Panel injected')

# 5. JS before </script>
last_script = H.rfind('</script>')
H = H[:last_script] + '\n' + JS + '\n' + H[last_script:]
print('\u2713 JS injected')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(H)

# Verify
tab_count = H.count('class="tab"') + H.count('class="tab active"')
print(f'\n\u2713 Tab 1 \u2014 Global Market injected. {tab_count} tabs total.')
