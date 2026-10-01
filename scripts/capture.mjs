import {createServer} from 'vite';
import {chromium} from 'playwright';
import fs from 'node:fs';
const server=await createServer({server:{host:'127.0.0.1',port:4173}});await server.listen();
const browser=await chromium.launch({executablePath:process.env.CHROMIUM_PATH||undefined,headless:true,args:['--no-sandbox','--disable-dev-shm-usage','--disable-gpu','--no-zygote']});
try {
const page=await browser.newPage({viewport:{width:1500,height:1000},deviceScaleFactor:1});
await page.goto('http://127.0.0.1:4173');await page.waitForFunction(()=>document.querySelector('#suppression-number').textContent==='70.8%');await page.evaluate(()=>document.fonts.ready);
async function shot(name,text){await page.locator('#toast').evaluate(x=>x.classList.remove('visible'));await page.evaluate(text=>{let x=document.getElementById('gallery-caption');if(!x){x=document.createElement('aside');x.id='gallery-caption';x.style.cssText='position:fixed;z-index:9999;bottom:0;left:0;right:0;background:#402c38;color:#f4efeb;padding:20px 55px;font:16px Inter,sans-serif;border-top:1px solid #705965;';document.body.append(x);}x.textContent=text;},text);await page.screenshot({path:`submission/gallery/${name}.png`});await page.locator('#gallery-caption').evaluate(x=>x.remove());}
await shot('01-the-gap','01 / THE GAP — 70.8% of program records suppress earnings. Keep the missing information visible.');
await page.locator('#reveal').click();await page.waitForTimeout(1200);await shot('02-the-model-view','02 / THE MODEL’S VIEW — Public observations, supported estimates and records we decline to estimate.');
await page.getByRole('button',{name:'Rutgers',exact:true}).click();await page.locator('.program-row').first().waitFor();await shot('03-program-evidence','03 / THE EVIDENCE — A labelled estimate, its uncertainty interval and a user-controlled benchmark.');
await page.locator('#pin-program').click();await page.locator('#program-query').fill('Computer');await page.locator('#credential-filter').selectOption('3');await page.locator('#status-filter').selectOption('published');await page.locator('.program-row').first().click();await page.locator('#pin-program').click();await page.locator('nav [data-view="compare"]').click();await shot('04-comparison','04 / COMPARE — Official observations and model estimates keep their distinct sources. CSV export includes provenance.');
await page.locator('nav [data-view="method"]').click();await page.locator('.method-summary').scrollIntoViewIfNeeded();await page.locator('.method-summary').evaluate(el=>scrollTo(0,el.getBoundingClientRect().top+scrollY-45));await shot('05-validation','05 / VALIDATION — Better than a simple baseline, with a coverage shortfall reported openly.');
await page.locator('.limits').scrollIntoViewIfNeeded();await shot('06-limitations','06 / THE LIMIT — Hidden outcomes have no public ground truth. Published-data performance is not a guarantee.');
await page.locator('nav [data-view="explore"]').click();await page.setViewportSize({width:1500,height:1000});await shot('thumbnail','WITHHELD / College outcomes, with the gaps left in. Built by Rishik Rontala.');
console.log('Saved 6 captioned gallery images and thumbnail.');
}finally{await browser.close();await server.close();}
