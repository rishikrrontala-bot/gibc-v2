"""Independently check splits and recompute published test metrics from CSV."""
import csv,json,math
from pathlib import Path
root=Path(__file__).resolve().parents[1]
m=json.loads((root/'public/data/metrics.json').read_text())
s=json.loads((root/'pipeline/splits.json').read_text())
g={k:{x.split('-')[0] for x in v} for k,v in s.items()}
assert not g['train']&g['test'] and not g['train']&g['calibration'] and not g['test']&g['calibration']
r=list(csv.DictReader((root/'pipeline/test-predictions.csv').open()))
assert len(r)==m['model']['n']
mae=sum(abs(float(x['actual'])-float(x['prediction'])) for x in r)/len(r)
coverage=sum(float(x['lower'])<=float(x['actual'])<=float(x['upper']) for x in r)/len(r)
assert abs(mae-m['model']['mae'])<.01
assert abs(coverage-m['model']['coverage'])<.00001
assert all(float(x['lower'])<=float(x['prediction'])<=float(x['upper']) for x in r)
print(f'Verified {len(r)} held-out outcomes, MAE ${mae:,.2f}, coverage {coverage:.3%}, zero institution-family overlap.')
