/** Record a real browser walkthrough; ffmpeg encodes frames without synthesizing UI. */
import {createServer} from 'vite';
import {chromium} from 'playwright';
import {spawn} from 'node:child_process';
import {once} from 'node:events';
import fs from 'node:fs';
const timeline=JSON.parse(fs.readFileSync('submission/video/timeline.json','utf8'));
const duration=timeline.at(-1).start+timeline.at(-1).duration;
const server=await createServer({server:{host:'127.0.0.1',port:4173}});await server.listen();
const browser=await chromium.launch({executablePath:process.env.CHROMIUM_PATH||undefined,headless:true,args:['--no-sandbox','--disable-dev-shm-usage','--disable-gpu','--no-zygote']});
const page=await browser.newPage({viewport:{width:1440,height:810},deviceScaleFactor:1});
page.on('pageerror',e=>{console.error(e);process.exitCode=1;});
const wait=ms=>new Promise(r=>setTimeout(r,ms));
async function scrollTo(selector,offset=25){await page.locator(selector).evaluate((el,off)=>window.scrollTo({top:el.getBoundingClientRect().top+scrollY-off,behavior:'smooth'}),offset);await wait(500);}
async function click(selector){const el=page.locator(selector);await el.scrollIntoViewIfNeeded();const box=await el.boundingBox();if(box)await page.mouse.move(box.x+box.width/2,box.y+box.height/2,{steps:14});await wait(200);await el.click();}
await page.goto('http://127.0.0.1:4173');await page.waitForFunction(()=>document.querySelector('#suppression-number').textContent==='70.8%');await page.evaluate(()=>document.fonts.ready);
await page.addStyleTag({content:'html{scroll-behavior:smooth} #demo-cursor{position:fixed;width:18px;height:18px;border:2px solid #402c3880;border-radius:50%;pointer-events:none;z-index:9998;transform:translate(-50%,-50%);background:#f4efeb40}'});
await page.evaluate(()=>{const cursor=document.createElement('div');cursor.id='demo-cursor';cursor.style.left='96%';cursor.style.top='90%';document.body.append(cursor);document.addEventListener('mousemove',ev=>{cursor.style.left=ev.clientX+'px';cursor.style.top=ev.clientY+'px';});});
const out=spawn('ffmpeg',['-hide_banner','-loglevel','warning','-y','-f','image2pipe','-vcodec','mjpeg','-framerate','12','-i','pipe:0','-an','-vf','scale=1920:1080','-c:v','libx264','-preset','veryfast','-crf','26','-pix_fmt','yuv420p','/tmp/withheld-screen.mp4'],{stdio:['pipe','inherit','inherit']});
const actions={
 intro:async()=>{await wait(6000);await click('#reveal');},
 search:async()=>{await click('[data-example="Rutgers University-New Brunswick"]');await page.locator('.program-row').first().waitFor();await scrollTo('#explorer');},
 estimate:async()=>{await scrollTo('#program-detail',110);},
 evidence:async()=>{await click('.evidence-note summary');await scrollTo('.evidence-note',150);},
 loan:async()=>{await scrollTo('.loan-section',140);await page.locator('#loan-amount').fill('12000');await wait(1800);await page.locator('#loan-rate').fill('0');},
 published:async()=>{await click('#pin-program');await scrollTo('.explorer-toolbar',60);await page.locator('#program-query').fill('Computer');await page.locator('#credential-filter').selectOption('3');await page.locator('#status-filter').selectOption('published');await click('.program-row');await scrollTo('#program-detail',95);},
 compare:async()=>{await click('#pin-program');await click('nav [data-view="compare"]');await scrollTo('.comparison-grid',65);await wait(9000);await click('#export-compare');await scrollTo('.comparison-grid',65);},
 metrics:async()=>{await click('nav [data-view="method"]');await wait(5000);await scrollTo('.method-summary',160);},
 baselines:async()=>{await scrollTo('.method-columns',100);},
 pipeline:async()=>{await scrollTo('.method-flow',90);},
 limits:async()=>{await scrollTo('.limits',90);},
 close:async()=>{await click('nav [data-view="explore"]');await page.evaluate(()=>scrollTo({top:0,behavior:'smooth'}));}
};
const start=performance.now();
let actionError;
const journey=(async()=>{for(const scene of timeline){await wait(Math.max(0,scene.start*1000-(performance.now()-start)));console.log('Scene',scene.id);await actions[scene.id]();}})().catch(e=>{actionError=e;});
try {
 for(let f=0;f<Math.ceil(duration*12);f++){
   await wait(Math.max(0,f/12*1000-(performance.now()-start)));
   const buffer=await page.screenshot({type:'jpeg',quality:85});
   if(!out.stdin.write(buffer))await once(out.stdin,'drain');
 }
 await journey;if(actionError)throw actionError;
}finally{out.stdin.end();await once(out,'exit');await browser.close();await server.close();}
console.log('Recorded',duration,'seconds');
