"""Build the universal catalogue table from its normalized presentation index."""
from __future__ import annotations
import argparse,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
HEADER='| Geometry | Ambient presentation | Dimension | Recorded Chern index | Ambient matrix rank | h(1,1) | Analysis |'

def analysis_label(row):
 text=row['status']
 if row.get('atomic_invariants_link'):
  text+=' · [Atomic invariants]('+row['atomic_invariants_link']+')'
 return text

def render_table(records):
 records=sorted(records,key=lambda r:(-r['dimension'],-r['index'],r['title']))
 return HEADER+'\n|---|---|---:|---:|---:|---:|---|\n'+''.join(f'| [{r["title"]}]({r["link"]}) | {r["ambient"]} | {r["dimension"]} | {r["index"]} | {r["matrix_rank"]} | {r["h11"]} | {analysis_label(r)} |\n' for r in records)

def render_index():
 page=ROOT/'docs/catalog/index.md'
 prefix=page.read_text().split(HEADER)[0]
 records=json.loads((ROOT/'docs/data/catalog-records.json').read_text())['records']
 return prefix+render_table(records)

def main():
 parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--check',action='store_true');args=parser.parse_args()
 path=ROOT/'docs/catalog/index.md';text=render_index()
 if args.check:
  assert path.read_text()==text,'Master catalogue table disagrees with canonical records'
 else:path.write_text(text)
 print('Universal catalogue index synchronized')
if __name__=='__main__':main()
