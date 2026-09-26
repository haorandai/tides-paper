"""Update the static result charts and tables from the paper's reported values."""
from pathlib import Path
from html import escape
import json,re
ROOT=Path(__file__).resolve().parents[1]
data=json.loads((ROOT/'assets/results-data.json').read_text())
BENCH=data['benchmarks']

def bar(label,value,emphasis=False):
    assert 0 <= value <= 100
    return f'<div class="plot-row{" emphasis" if emphasis else ""}"><span class="plot-label">{escape(label)}</span><span class="plot-track" aria-hidden="true"><span class="plot-bar" style="width:{value}%"></span></span><span class="plot-value">{value:.1f}</span></div>'

def scale():
    return '<div class="plot-scale" aria-hidden="true"><span></span><span class="plot-axis"><span>0</span><span>50</span><span>100</span></span><span></span></div>'

def cell(pair):
    return '–' if pair is None else f'{pair[0]:.1f} <span class="pm">± {pair[1]:.1f}</span>'

charts=['<div class="ras-charts">']
for model in data['models']:
    rows=[r for r in model['rows'] if r['cells']['Avg']['ras'] is not None]
    chart_id=model['id']+'-ras'
    charts.append(f'<figure class="comparison-plot" aria-labelledby="{chart_id}"><figcaption id="{chart_id}">{escape(model["name"])}<span>Average RAS (%)</span></figcaption>')
    charts.extend(bar(r['method'],r['cells']['Avg']['ras'][0],r['method']=='TIDES') for r in rows)
    charts.append(scale()+'</figure>')
charts.append('</div>')

table=['<div class="table-wrap" tabindex="0" role="region" aria-label="Average results from Table 1"><table><caption>Averages over five benchmarks · Table 1 · mean ± standard deviation</caption><thead><tr><th scope="col">Backbone</th><th scope="col">Method</th><th scope="col">Pass@1 (%)</th><th scope="col">RAS (%) ↑</th></tr></thead>']
for model in data['models']:
    table.append('<tbody>')
    for index,row in enumerate(model['rows']):
        avg=row['cells']['Avg']
        table.append('<tr class="ours">' if row['method']=='TIDES' else '<tr>')
        if index==0:table.append(f'<th scope="rowgroup" rowspan="{len(model["rows"])}">{escape(model["name"])}</th>')
        table.append(f'<th scope="row">{escape(row["method"])}</th><td>{cell(avg["pass_at_1"])}</td><td>{cell(avg["ras"])}</td></tr>')
    table.append('</tbody>')
table.append('</table></div>')

full=['<div class="table-wrap" tabindex="0" role="region" aria-label="Per-benchmark results from Table 1"><table class="benchmark-table"><caption>Per-benchmark results · Table 1 · mean ± standard deviation</caption><thead><tr><th scope="col" rowspan="2">Backbone</th><th scope="col" rowspan="2">Method</th>']
full.extend(f'<th scope="colgroup" colspan="2">{escape(b)}</th>' for b in BENCH)
full.append('</tr><tr>'+'<th scope="col">Pass@1</th><th scope="col">RAS ↑</th>'*len(BENCH)+'</tr></thead>')
for model in data['models']:
    full.append('<tbody>')
    for index,row in enumerate(model['rows']):
        full.append('<tr class="ours">' if row['method']=='TIDES' else '<tr>')
        if index==0:full.append(f'<th scope="rowgroup" rowspan="{len(model["rows"])}">{escape(model["name"])}</th>')
        full.append(f'<th scope="row">{escape(row["method"])}</th>')
        for b in BENCH:
            c=row['cells'][b]; full.append(f'<td>{cell(c["pass_at_1"])}</td><td>{cell(c["ras"])}</td>')
        full.append('</tr>')
    full.append('</tbody>')
full.append('</table></div>')

ablation=['<figure class="ablation-plot" aria-labelledby="ablation-plot-heading"><figcaption id="ablation-plot-heading">Relative Attack Score (%)<span>Layer-wise and strongest-vector strategies</span></figcaption>']
for row in data['ablation']:
    ablation.append(f'<div class="ablation-group"><h4>{escape(row["benchmark"])}</h4>')
    ablation.append(bar('Layer-wise',row['layer_wise_ras_percent'],True))
    ablation.append(bar('Strongest',row['strongest_ras_percent']))
    ablation.append('</div>')
ablation.append(scale()+'<p class="chart-source">Values from Figure 4.</p></figure>')

path=ROOT/'index.html'
html=path.read_text()
for name,markup in [('ras-charts',charts),('full-results',table),('benchmark-results',full),('ablation-chart',ablation)]:
    pattern=re.compile(r'<!-- start:'+re.escape(name)+r' -->[\s\S]*?<!-- end:'+re.escape(name)+r' -->')
    assert len(pattern.findall(html))==1,name
    html=pattern.sub(lambda _:f'<!-- start:{name} -->\n'+''.join(markup)+f'\n<!-- end:{name} -->',html)
path.write_text(html)
n=sum(len(m['rows']) for m in data['models'])
print(f'Rendered {len(data["models"])} RAS comparisons, {n} average rows, {n} per-benchmark rows, and six ablation values.')
