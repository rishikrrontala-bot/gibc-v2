"""Optional local demo narration. Requires kokoro-onnx + soundfile and external weights."""
import json,os,re
from pathlib import Path
import numpy as np
import soundfile as sf
from kokoro_onnx import Kokoro
root=Path(__file__).resolve().parents[1]
weights=Path(os.environ.get('WITHHELD_TTS_DIR',root.parent/'tts'))
k=Kokoro(str(weights/'model.onnx'),str(weights/'voices.bin'))
scenes=json.loads((root/'submission/video/scenes.json').read_text())
all_audio=[];position=0;captions=[]
for scene in scenes:
    audio,sr=k.create(scene['text'],voice='af_heart',speed=.94,lang='en-us')
    lead=np.zeros(int(sr*.6),dtype=np.float32);tail=np.zeros(int(sr*.9),dtype=np.float32)
    scene['start']=position;scene['duration']=(len(audio)+len(lead)+len(tail))/sr
    parts=re.findall(r'[^.!?]+[.!?]?',scene['text']);total=sum(len(x) for x in parts);at=position+.6
    for part in parts:
        duration=len(audio)/sr*len(part)/total
        captions.append((at,at+duration,part.strip()));at+=duration
    all_audio.extend([lead,audio,tail]);position+=scene['duration']
    print(scene['id'],round(scene['duration'],2),flush=True)
def stamp(t):
    ms=round(t*1000);return f'{ms//3600000:02}:{ms//60000%60:02}:{ms//1000%60:02},{ms%1000:03}'
sf.write(root/'submission/video/narration.wav',np.concatenate(all_audio),sr)
(root/'submission/video/timeline.json').write_text(json.dumps(scenes,indent=2))
(root/'submission/video/captions.srt').write_text('\n\n'.join(f'{i+1}\n{stamp(a)} --> {stamp(b)}\n{text}' for i,(a,b,text) in enumerate(captions))+'\n')
print('TOTAL',position)
