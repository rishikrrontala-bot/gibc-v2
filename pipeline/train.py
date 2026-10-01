"""Reproducible institution-grouped earnings experiment, never reconstructs private records."""
from pathlib import Path
import json, hashlib, time, platform, math
import numpy as np
import pandas as pd
import lightgbm as lgb
from sklearn.model_selection import GroupShuffleSplit
from sklearn.metrics import mean_absolute_error, median_absolute_error
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'public/data'; OUT.mkdir(parents=True,exist_ok=True)
START=time.time(); SEED=42

def write(p,obj):
    p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(obj,separators=(',',':'),allow_nan=False))
def num(s): return pd.to_numeric(s,errors='coerce')
def qcal(y,lo,hi):
    scores=np.maximum.reduce([lo-y,y-hi,np.zeros(len(y))])
    return float(np.quantile(scores,min(1,math.ceil((len(scores)+1)*.8)/len(scores)),method='higher'))
def band(x):
    return np.where(np.isnan(x),'Unknown size',np.where(x<30,'Under 30',np.where(x<100,'30–99','100+')))
def main():
    p=ROOT/'data/raw'
    d=pd.read_csv(p/'Most-Recent-Cohorts-Field-of-Study.csv',low_memory=False)
    inst=pd.read_csv(p/'Most-Recent-Cohorts-Institution.csv',usecols=['UNITID','STABBR'],low_memory=False)
    d=d.merge(inst.drop_duplicates('UNITID'),on='UNITID',how='left',validate='many_to_one')
    d['STABBR']=d.STABBR.fillna('Other')
    d['earn']=num(d.EARN_MDN_5YR);d['debt']=num(d.DEBT_ALL_STGP_EVAL_MDN)
    d['size']=pd.concat([num(d.IPEDSCOUNT1),num(d.IPEDSCOUNT2)],axis=1).sum(axis=1,min_count=1)
    d['key']=d.OPEID6.astype(str)+'-'+d.CIPCODE.astype(str)+'-'+d.CREDLEV.astype(str)
    # Outcomes may be pooled across branches. Keep one representative per pooled program.
    g=d.sort_values(['MAIN','UNITID'],ascending=[False,True]).drop_duplicates('key').copy().reset_index(drop=True)
    X=pd.DataFrame({'field':g.CIPCODE.astype(str),'broad_field':(g.CIPCODE//100).astype(str),'credential':g.CREDLEV.astype(str),'state':g.STABBR.astype(str),'control':g.CONTROL.astype(str),'log_completions':np.log1p(g['size'])})
    cat=['field','broad_field','credential','state','control']
    for c in cat: X[c]=X[c].astype('category')
    valid=np.flatnonzero(g.earn.notna() & (g.earn>0))
    first=GroupShuffleSplit(n_splits=1,test_size=.2,random_state=SEED)
    a,b=next(first.split(valid,groups=g.iloc[valid].OPEID6)); rest=valid[a];test=valid[b]
    second=GroupShuffleSplit(n_splits=1,test_size=.25,random_state=SEED+1)
    a,b=next(second.split(rest,groups=g.iloc[rest].OPEID6));train=rest[a];cal=rest[b]
    groups=[set(g.iloc[ix].OPEID6) for ix in [train,cal,test]]
    assert not groups[0]&groups[1] and not groups[0]&groups[2] and not groups[1]&groups[2]
    y=g.earn.to_numpy()
    predictions=[]; models=[]
    for alpha in [.1,.5,.9]:
        print('Training quantile',alpha,'on',len(train),'programs',flush=True)
        model=lgb.LGBMRegressor(objective='quantile',alpha=alpha,n_estimators=350,num_leaves=23,min_child_samples=35,learning_rate=.045,reg_lambda=2,n_jobs=4,random_state=SEED,verbosity=-1)
        model.fit(X.iloc[train],y[train],categorical_feature=cat)
        pred=model.predict(X)
        predictions.append(pred);models.append(model)
        model.booster_.save_model(str(ROOT/'pipeline'/f'model-{alpha}.txt'))
    raw=np.sort(np.stack(predictions,axis=1),axis=1); lo,med,hi=raw.T
    bands=band(g['size'].to_numpy()); global_q=qcal(y[cal],lo[cal],hi[cal]);calibration={}
    for label in sorted(set(bands)):
        ix=cal[bands[cal]==label]
        correction=qcal(y[ix],lo[ix],hi[ix]) if len(ix)>=100 else global_q
        calibration[label]={'n':len(ix),'correction':round(correction,2),'fallback':len(ix)<100}
        mask=bands==label;lo[mask]=np.maximum(0,lo[mask]-correction);hi[mask]+=correction
    # Baselines fitted ONLY on training outcomes, with global fallback.
    tr=g.iloc[train];fallback=float(np.median(y[train]))
    def baseline(cols):
        means=tr.groupby(cols).earn.median().to_dict()
        return np.array([means.get(tuple(row) if len(cols)>1 else row[0],fallback) for row in g.iloc[test][cols].itertuples(index=False,name=None)])
    def metrics(ix):
        return {'n':len(ix),'mae':round(mean_absolute_error(y[ix],med[ix]),2),'median_absolute_error':round(median_absolute_error(y[ix],med[ix]),2),'coverage':round(float(np.mean((y[ix]>=lo[ix])&(y[ix]<=hi[ix]))),5),'mean_width':round(float(np.mean(hi[ix]-lo[ix])),2)}
    support_map=tr.groupby(['CIPCODE','CREDLEV']).size().to_dict()
    support=np.array([support_map.get((r.CIPCODE,r.CREDLEV),0) for r in g.itertuples()])
    allowed=support>=30
    diagnostics={'model':metrics(test),'baselines':[{'name':'Field + credential median','mae':round(mean_absolute_error(y[test],baseline(['CIPCODE','CREDLEV'])),2)},{'name':'State + credential median','mae':round(mean_absolute_error(y[test],baseline(['STABBR','CREDLEV'])),2)},{'name':'Global median','mae':round(mean_absolute_error(y[test],np.repeat(fallback,len(test))),2)}],
      'by_size':[{**metrics(test[bands[test]==b]),'label':b} for b in sorted(set(bands)) if np.any(bands[test]==b)],
      'by_credential':[{**metrics(test[g.iloc[test].CREDLEV.to_numpy()==c]),'label':str(g.loc[g.CREDLEV==c,'CREDDESC'].iloc[0])} for c in sorted(g.CREDLEV.unique()) if np.sum(g.iloc[test].CREDLEV.to_numpy()==c)>10],
      'supported_test':metrics(test[allowed[test]]),'split':{'train':len(train),'calibration':len(cal),'test':len(test),'train_institutions':len(groups[0]),'calibration_institutions':len(groups[1]),'test_institutions':len(groups[2]),'group':'OPEID6','seed':SEED,'overlap':0},'calibration':calibration,'target_coverage':.8,
      'limitations':['Test labels are published outcomes. Coverage on privacy-suppressed programs is unknown.','Programs withheld from publication differ from the observed training population.','Intervals describe program-level medians, not individual graduate salaries.','Program branches can share a pooled outcome; validation and training use one record per OPEID6 × CIP × credential.','Features use current program metadata; evaluation is cross-sectional, not a forecast of future earnings.'],
      'features':list(X.columns),'training_seconds':round(time.time()-START,1),'versions':{'python':platform.python_version(),'lightgbm':lgb.__version__,'pandas':pd.__version__,'numpy':np.__version__}}
    predmap={k:(float(med[j]),float(lo[j]),float(hi[j]),int(support[j]),bool(allowed[j])) for j,k in enumerate(g.key)}
    schools=[];states={};suppressed=0;unavailable=0;estimated=0;published=0
    def n(v): return int(round(v)) if pd.notna(v) else None
    for unit,block in d.groupby('UNITID',sort=True):
        r=block.iloc[0]; state=str(r.STABBR)
        schools.append({'id':int(unit),'name':str(r.INSTNM),'state':state,'count':len(block)})
        arr=states.setdefault(state,[])
        for idx,r in block.iterrows():
            official=n(r.earn); debt=n(r.debt); pr,l,h,s,ok=predmap[r.key]
            rawvalue=str(r.EARN_MDN_5YR)
            status='published' if official is not None else ('suppressed' if rawvalue in ['PS','PrivacySuppressed'] else 'unavailable')
            published+=status=='published';suppressed+=status=='suppressed';unavailable+=status=='unavailable'
            show=status=='suppressed' and ok
            estimated+=show
            arr.append([int(idx),int(unit),int(r.CIPCODE),int(r.CREDLEV),official,debt,n(pr) if show else None,n(l) if show else None,n(h) if show else None,s,n(r['size']),status])
    for state,rows in states.items():write(OUT/'states'/f'{state}.json',rows)
    write(OUT/'schools.json',schools)
    write(OUT/'fields.json',{str(int(r.CIPCODE)):str(r.CIPDESC).rstrip('.') for r in d[['CIPCODE','CIPDESC']].drop_duplicates('CIPCODE').itertuples()})
    write(OUT/'credentials.json',{str(int(r.CREDLEV)):str(r.CREDDESC) for r in d[['CREDLEV','CREDDESC']].drop_duplicates('CREDLEV').itertuples()})
    source='https://ed-public-download.scorecard.network/downloads/'
    manifest={'release':'2026-06-10','target':'EARN_MDN_5YR','horizon':'5 years after completion','total':len(d),'published':published,'suppressed':suppressed,'unavailable':unavailable,'estimated':estimated,'schools':len(schools),'unique_pooled_programs':len(g),'training_support_minimum':30,'sources':[{'url':source+f'Most-Recent-Cohorts-{label}_06102026.zip','sha256':hashlib.sha256((p/file).read_bytes()).hexdigest()} for label,file in [('Field-of-Study','field.zip'),('Institution','institution.zip')]],'row_schema':['id','school','field','credential','published_earnings','published_debt','estimate','lower','upper','training_support','completions','status'],'license':'U.S. Department of Education College Scorecard. Data.gov metadata lists Creative Commons Attribution (CC BY): http://www.opendefinition.org/licenses/cc-by. Institution/program names retained for attribution and identification.'}
    write(OUT/'manifest.json',manifest);write(OUT/'metrics.json',diagnostics)
    sample=d.sample(1200,random_state=SEED)
    write(OUT/'field-sample.json',[[n(r.earn),*(n(x) for x in predmap[r.key][:3]),str(r.EARN_MDN_5YR) in ['PS','PrivacySuppressed'] and predmap[r.key][4]] for _,r in sample.iterrows()])
    pd.DataFrame({'key':g.iloc[test].key,'institution':g.iloc[test].OPEID6,'actual':y[test],'prediction':med[test],'lower':lo[test],'upper':hi[test],'size_band':bands[test],'support':support[test]}).to_csv(ROOT/'pipeline/test-predictions.csv',index=False)
    write(ROOT/'pipeline/splits.json',{name:g.iloc[ix].key.tolist() for name,ix in [('train',train),('calibration',cal),('test',test)]})
    print(json.dumps({'manifest':manifest,'metrics':diagnostics},indent=2),flush=True)
if __name__=='__main__':main()
