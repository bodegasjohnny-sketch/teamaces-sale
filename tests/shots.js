const { chromium } = require('/tmp/pwk/node_modules/playwright-core');
const fs=require('fs'),path=require('path');
const exe=require('child_process').execSync('ls -d ~/.cache/ms-playwright/chromium_headless_shell-*/*/chrome-headless-shell').toString().trim();
const axe=fs.readFileSync('/tmp/pwk/node_modules/axe-core/axe.min.js','utf8');
const url='http://127.0.0.1:8931/';
(async()=>{const b=await chromium.launch({executablePath:exe});
for(const [name,w,h,mob] of [['desktop',1366,768,false],['mobile',390,844,true]]){
  const p=await b.newPage({viewport:{width:w,height:h},isMobile:mob,deviceScaleFactor:1});
  const errs=[],ext=[];p.on('console',m=>m.type()==='error'&&errs.push(m.text()));p.on('pageerror',e=>errs.push(e.message));
  p.on('request',r=>{if(!r.url().startsWith('http://127.0.0.1:8931'))ext.push(r.url())});
  await p.goto(url);await p.waitForTimeout(2000);
  await p.screenshot({path:`shots/${name}-fold.png`});
  const H=await p.evaluate(()=>document.body.scrollHeight);
  for(let y=0;y<H;y+=400){await p.evaluate(y=>scrollTo(0,y),y);await p.waitForTimeout(60);}
  await p.evaluate(()=>{__revealAll();scrollTo(0,0)});await p.waitForTimeout(2200);
  await p.screenshot({path:`shots/${name}-full.png`,fullPage:true});
  const ov=await p.evaluate(()=>({sw:document.documentElement.scrollWidth,cw:document.documentElement.clientWidth,wide:[...document.querySelectorAll('body *')].filter(e=>e.getBoundingClientRect().right>document.documentElement.clientWidth+1&&!e.closest('.ticker')).map(e=>e.className||e.tagName).slice(0,5)}));
  const vals=await p.$$eval('[data-count]',e=>[...new Set(e.map(x=>x.textContent))]);
  await p.addScriptTag({content:axe});const r=await p.evaluate(async()=>(await axe.run()).violations.map(v=>v.id+' ('+v.impact+') x'+v.nodes.length));
  console.log(name,JSON.stringify({overflow:ov,errs,ext,axe:r,vals}));
}
await b.close();})();
