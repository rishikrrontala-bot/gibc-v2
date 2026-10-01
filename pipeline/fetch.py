"""Download the exact official release, verify hashes, extract the two CSVs."""
from pathlib import Path
import urllib.request,hashlib,json,zipfile,shutil
ROOT=Path(__file__).resolve().parents[1]
p=ROOT/'data/raw';p.mkdir(parents=True,exist_ok=True)
manifest=json.loads((ROOT/'public/data/manifest.json').read_text())
for source,name in zip(manifest['sources'],['field','institution']):
    path=p/f'{name}.zip'
    print('Fetching',source['url'],flush=True)
    with urllib.request.urlopen(source['url'],timeout=180) as r,path.open('wb') as f:shutil.copyfileobj(r,f)
    digest=hashlib.sha256(path.read_bytes()).hexdigest()
    if digest!=source['sha256']:raise RuntimeError('Source hash changed. Review the upstream release before retraining.')
    with zipfile.ZipFile(path) as z:
        for member in z.namelist():
            if member.endswith('.csv') and '__MACOSX' not in member:
                with z.open(member) as r,(p/Path(member).name).open('wb') as f:shutil.copyfileobj(r,f)
print('Verified downloads and extracted CSV files.')
