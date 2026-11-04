CAM='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><rect x="3" y="6" width="18" height="13" rx="2"/><circle cx="12" cy="12.5" r="3.5"/><path d="M8 6l1.5-2h5L16 6"/></svg>'
TRO='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><path d="M8 4h8v5a4 4 0 01-8 0V4zM8 6H5a3 3 0 003 4M16 6h3a3 3 0 01-3 4M12 13v4M8 20h8M9 17h6"/></svg>'
USR='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" aria-hidden="true"><circle cx="12" cy="8" r="4"/><path d="M4 21c1-4 4.5-6 8-6s7 2 8 6"/></svg>'
veh=[("Car 1","car"),("Car 2","car"),("Car 3","car"),("Motorcycle 1","motorcycle"),("Motorcycle 2","motorcycle")]
vehicles="".join(f'<div class="card ph-card rv" style="--d:{i*80}ms"><div class="slot"><div>{CAM}Photo on request</div></div><h3>{n}</h3><p>[Add make / model / year]</p><span class="tag tag-ph">Details on request</span></div>' for i,(n,k) in enumerate(veh))
team=[("jay","Jerickson Baes","Coach Jay","Chief Instructor",12),("ronnel","Ronnel Pasia","Coach Ronnel","Driving Instructor",11),("ericson","Ericson Hernandez","Coach Ericson","Driving Instructor",10),("noel","Noel Perez","Coach Noel","Theoretical and Practical Driving Instructor",6),("marlon","Marlon T. Balbuena","Coach Marlon","Operations Manager &amp; Instructor",6),("janica","Janica Dimaunahan","Janica","Accounting Staff &amp; Admin",6),("kim","Kim De Chavez","Coach Kim","Driving Instructor",2)]
emps="".join(f'<figure class="card person rv" style="--d:{i*70}ms"><img src="assets/team/{s}.jpg" width="400" height="500" loading="lazy" alt="{n}, {r}"><figcaption><span class="yrs">{y} yrs</span><h3>{n}</h3><p>{r}</p></figcaption></figure>' for i,(s,n,c,r,y) in enumerate(team))
founder='<figure class="card founder rv"><img src="assets/team/founder.jpg" width="480" height="600" loading="lazy" alt="Mark Rhein Lester Pulido, Founder and CEO"><figcaption><div class="kicker">Founder &amp; CEO</div><h3>Mark Rhein Lester Pulido</h3><p>The founder of TeamAces Driving Academy, built on a mission to raise the standard of driving education in the Philippines through safety, discipline and responsible driving.</p><blockquote>&ldquo;TeamAces was built on the belief that proper driving education creates safer roads, responsible drivers, and a better community for everyone.&rdquo;<cite>Mark Rhein Lester Pulido</cite></blockquote></figcaption></figure>'
emps=founder+'<div class="team">'+emps+'</div>'
awards=["Best Driving School","Best Trusted Driving School Batangas 2017","Q-Asia&#39;s Product Quality Best Driving School CALABARZON 2018","Premiere Driving School","Top Choice Driving School Batangas 2018","Most Outstanding Driving School, Business Initiative Directions Gold Category International 2018","Trusted Driving School Specialist","Best Driving School"]
alts=["Gold BEST seal","Globe award seal","BEST award seal","Mark of Excellence seal","Framed award certificate","Framed award certificate","Framed award certificate with gold frame","BEST award trophy","Glass award trophy","Black and glass award trophy","Framed award certificate","Trusted Excellence Achiever seal"]
aw="".join(f'<figure class="aw-tile rv" style="--d:{i*40}ms"><img src="assets/awards/award-{i+1:02d}.jpg" width="400" height="400" loading="lazy" alt="{a}"></figure>' for i,a in enumerate(alts))
titles="".join(f'<li>{a}</li>' for a in awards)
aw=f'<div class="aw-grid">{aw}</div><ul class="aw-titles">{titles}</ul>'
tick=["LTO-accredited DS-2020-00027-04","Theoretical Driving Course (TDC)","PDC Motorcycle","PDC 4 Wheels","Batangas City head office","8 awards recognised","Business for sale","Financial documents on request (NDA)"]
t="".join(f"<span>{x}</span>" for x in tick)
tpl=open("index.tpl.html").read()
for k,v in dict(VEHICLES=vehicles,EMPLOYEES=emps,AWARDS=aw,TICK=t,TICK2=t.replace("<span>",'<span aria-hidden="true">')).items(): tpl=tpl.replace("{{"+k+"}}",v)
import json,shutil,pathlib
from PIL import Image,ImageDraw,ImageFont
BASE="https://teamaces.johnnybodegas.com/"
ld={"@context":"https://schema.org","@graph":[{"@type":"Organization","@id":BASE+"#org","name":"TEAMACES DRIVING ACADEMY INC.","logo":BASE+"assets/logo-wordmark.png","address":{"@type":"PostalAddress","addressLocality":"Batangas City","addressCountry":"PH"}},{"@type":"WebPage","@id":BASE,"url":BASE,"name":"Business for Sale: TEAMACES DRIVING ACADEMY INC.","about":{"@id":BASE+"#org"},"inLanguage":"en"}]}
tpl=tpl.replace("{{JSONLD}}",'<script type="application/ld+json">'+json.dumps(ld)+'</script>')
open("index.html","w").write(tpl)
O=pathlib.Path("docs")
if O.exists(): shutil.rmtree(O)
O.mkdir(); shutil.copytree("assets",O/"assets")
for f in ["index.html","styles.css","data.js","main.js"]: shutil.copy(f,O/f)
(O/"CNAME").write_text("teamaces.johnnybodegas.com\n"); (O/".nojekyll").write_text("")
(O/"robots.txt").write_text("User-agent: *\nAllow: /\nSitemap: "+BASE+"sitemap.xml\n")
(O/"sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><url><loc>'+BASE+'</loc><lastmod>2026-11-04</lastmod></url></urlset>\n')
FB="/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf";FR="/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
W,H=1200,630;im=Image.new("RGB",(W,H),"#061B3C");d=ImageDraw.Draw(im,"RGBA")
for x in range(0,W,56): d.line([(x,0),(x,H)],fill=(255,255,255,12))
for y in range(0,H,56): d.line([(0,y),(W,y)],fill=(255,255,255,12))
d.rectangle([0,H-14,W,H],fill="#F5B301")
logo=Image.open("assets/logo-wordmark.png").convert("RGBA");lw=560;logo=logo.resize((lw,int(logo.height*lw/logo.width)))
pad=Image.new("RGBA",(lw+48,logo.height+36),(255,255,255,0));ImageDraw.Draw(pad).rounded_rectangle([0,0,pad.width-1,pad.height-1],18,fill=(255,255,255,240));pad.paste(logo,(24,18),logo)
im.paste(pad,(80,70),pad)
f1=ImageFont.truetype(FB,54);f2=ImageFont.truetype(FB,26);f3=ImageFont.truetype(FR,26)
y=110+pad.height
d.rounded_rectangle([80,y,80+d.textlength("BUSINESS FOR SALE",font=f2)+40,y+46],23,fill="#F5B301");d.text((100,y+8),"BUSINESS FOR SALE",font=f2,fill="#061B3C")
d.text((80,y+70),"LTO-accredited driving academy",font=f1,fill="#EEF3FA");d.text((80,y+140),"Batangas City, Philippines",font=f1,fill="#FFC845")
d.text((80,H-70),"teamaces.johnnybodegas.com  |  Documents on request (NDA)",font=f3,fill="#94A3B8")
im.save(O/"og.png",optimize=True)
ic=Image.open("assets/logo-shield.png").convert("RGBA")
ic.save(O/"favicon.ico",sizes=[(16,16),(32,32),(48,48)]);ic.resize((32,32)).save(O/"favicon-32.png");ic.convert("RGB").resize((180,180)).save(O/"apple-touch-icon.png")
