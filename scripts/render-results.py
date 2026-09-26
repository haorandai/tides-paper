"""Update the static result charts and table from the paper's reported means."""
from pathlib import Path
from html import escape
import json,re
ROOT=Path(__file__).resolve().parents[1]
data=json.loads((ROOT/'assets/results-data.json').read_text())

def bar(label,value,emphasis=False):
    assert 0 <= value <= 100
    return f'<div class="plot-row{" emphasis" if emphasis else ""}"><span class="plot-label">{escape(label)}</span><span class="plot-track" aria-hidden="true"><span class="plot-bar" style="width:{value}%"></span></span><span class="plot-value">{value:.1f}</span></div>'

def scale():
    return '<div class="plot-scale" aria-hidden="true"><span></span><span class="plot-axis"><span>0</span><span>50</span><span>100</span></span><span></span></div>'

charts=['<div class="ras-charts">']
for model in data['models']:
    rows=[r for r in model['rows'] if r['ras'] is not None]
    chart_id=model['id']+'-ras'
    charts.append(f'<figure class="comparison-plot" aria-labelledby="{chart_id}"><figcaption id="{chart_id}">{escape(model["name"])}<span>Mean RAS (%)</span></figcaption>')
    charts.extend(bar(r['method'],r['ras'],r['method']=='TIDES') for r in rows)
    charts.append(scale()+'</figure>')
charts.append('</div>')

table=['<div class="table-wrap" tabindex="0" role="region" aria-label="All average results from Table 1"><table><caption>Five-benchmark averages · Table 1, page 7</caption><thead><tr><th scope="col">Backbone</th><th scope="col">Method</th><th scope="col">Short-trace Pass@1 (%)</th><th scope="col">RAS (%)</th></tr></thead>']
for model in data['models']:
    table.append('<tbody>')
    for index,row in enumerate(model['rows']):
        attrs=' class="ours"' if row['method']=='TIDES' else ''
        table.append(f'<tr{attrs}>')
        if index==0:table.append(f'<th scope="rowgroup" rowspan="{len(model["rows"])}">{escape(model["name"])}</th>')
        ras='Not applicable' if row['ras'] is None else f'{row["ras"]:.1f}'
        table.append(f'<th scope="row">{escape(row["method"])}</th><td>{row["pass_at_1"]:.1f}</td><td>{ras}</td></tr>')
    table.append('</tbody>')
table.append('</table></div>')

ablation=['<figure class="ablation-plot" aria-labelledby="ablation-plot-heading"><figcaption id="ablation-plot-heading">Relative Attack Score (%)<span>Layer-wise and strongest-vector strategies</span></figcaption>']
for row in data['ablation']:
    ablation.append(f'<div class="ablation-group"><h4>{escape(row["benchmark"])}</h4>')
    ablation.append(bar('Layer-wise',row['layer_wise_ras_percent'],True))
    ablation.append(bar('Strongest',row['strongest_ras_percent']))
    ablation.append('</div>')
ablation.append(scale()+'<p class="chart-source">Values from Figure 4, page 16.</p></figure>')

path=ROOT/'index.html'
html=path.read_text()
for name,markup in [('ras-charts',charts),('full-results',table),('ablation-chart',ablation)]:
    pattern=re.compile(r'<!-- start:'+re.escape(name)+r' -->[\s\S]*?<!-- end:'+re.escape(name)+r' -->')
    assert len(pattern.findall(html))==1,name
    html=pattern.sub(lambda _:f'<!-- start:{name} -->\n'+''.join(markup)+f'\n<!-- end:{name} -->',html)
path.write_text(html)
print('Rendered two RAS comparisons, all 12 source rows, and six ablation values.')
