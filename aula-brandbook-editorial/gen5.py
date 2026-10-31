import json,pathlib
from gen4 import ic,page
T=json.load(open('tokens/_t.json'));C=json.load(open('tokens/contrast.json'))
VN=[('museos','Museos'),('justicia','Justicia'),('policia','Policía'),('educacion','Educación')]
FOOT='Aviso legal · Privacidad · no afiliada al Ministerio de Cultura'
def site(m):
  pad='20px' if m else '72px'
  nav='' if m else '<nav style="display:flex;gap:32px;font-size:15px">'+''.join(f'<a style="text-decoration:none">{x}</a>' for x in ['Oposiciones','Método','Simulacros','Preguntas'])+'</nav>'
  verts=''.join(f'<span class="vtag" style="margin-right:16px" data-vertical="{k}"><span class="marker"></span>{n}</span>' for k,n in VN)
  img='' if m else '<img src="../screens/explanation.png" style="width:300px;border-radius:32px;border:1px solid var(--line);box-shadow:0 24px 60px rgba(20,42,61,.16)">'
  feats=[('book','Todo el temario','Por bloques y temas, con tus errores siempre a mano.'),('timer','Simulacros reales','Mismo número de preguntas, tiempo y penalización que el examen.'),('source','Explicado con la norma','Cada respuesta cita su fuente. Si no la hay, lo decimos: «Sin fuente».')]
  return page(f'''<header style="display:flex;justify-content:space-between;align-items:center;padding:20px {pad};border-bottom:1px solid var(--line)"><img src="../logo/aula-umbrella-horizontal.svg" height="{30 if m else 36}" alt="Aula.">{nav}<a class="btn btn-primary" style="{'padding:10px 14px;font-size:15px' if m else ''}">{'Empezar' if m else 'Empezar gratis'}</a></header>
<section style="padding:{'40px 20px' if m else '80px 72px'};display:flex;gap:56px;align-items:center;justify-content:space-between">
<div style="max-width:620px"><p class="eyebrow">Oposiciones · Preparación con método</p>
<h1 style="font-size:{44 if m else 72}px;line-height:1.04;margin:14px 0 18px">Menos ruido<span class="dot">.</span><br>Más temario<span class="dot">.</span></h1>
<p style="font-size:{17 if m else 20}px;color:var(--muted);margin:0 0 26px">Lecciones cortas, simulacros con el formato real y explicaciones que citan la norma. Estudia con método, no con suerte.</p>
<div style="display:flex;gap:12px;flex-wrap:wrap"><a class="btn btn-primary big" style="{'width:100%' if m else ''}">Empezar gratis</a><a class="btn btn-ghost big" style="{'width:100%' if m else ''}">Ver cómo funciona</a></div>
<div style="display:flex;flex-wrap:wrap;gap:10px 0;margin-top:28px">{verts}</div></div>{img}</section>
<section style="padding:{'8px 20px 40px' if m else '0 72px 72px'};display:grid;grid-template-columns:{'1fr' if m else 'repeat(3,1fr)'};gap:20px">
{''.join(f'<div style="border-top:2px solid var(--ink);padding-top:18px">{ic(i,24)}<h3 class="serif" style="font-size:22px;margin:12px 0 6px;font-weight:600">{t}</h3><p class="muted" style="margin:0">{d}</p></div>' for i,t,d in feats)}</section>
<footer style="background:var(--navy);color:#F4F1EA;padding:{'32px 20px' if m else '48px 72px'}"><div style="display:flex;justify-content:space-between;align-items:{'flex-start' if m else 'center'};flex-direction:{'column' if m else 'row'};gap:20px"><img src="../logo/aula-umbrella-on-dark.svg" height="32" alt="Aula."><span style="font-size:14px;color:#B9BCC8">{FOOT}</span></div>
<p style="font-size:13px;color:#B9BCC8;margin:20px 0 0">© 2026 Aula · aulaoposiciones.es · hola@aulaoposiciones.es</p></footer>''',w=390 if m else 1280,h=844 if m else 800)
open('web/site-desktop.html','w').write(site(False));open('web/site-mobile.html','w').write(site(True))
# UI kit
def kit(theme):
  sw=lambda n,v,fg: f'<div><div style="height:56px;border-radius:8px;background:{v};border:1px solid var(--line)"></div><small class="mono subtle" style="font-size:11px">{n}<br>{v}</small></div>'
  P=T['dark'] if theme=='dark' else {**T['brand'],**T['neutral'],**T['semantic']}
  keys=['bg','surface','surface-2','line','ink','muted','subtle','gold','success','error','warning','ai'] if theme=='dark' else ['paper','surface','surface-2','line','navy','muted','subtle','gold','gold-700','success','error','ai']
  return page(f'''<div style="padding:40px 48px"><div style="display:flex;justify-content:space-between;align-items:center"><img src="../logo/aula-umbrella-{'on-dark' if theme=='dark' else 'horizontal'}.svg" height="34"><span class="eyebrow">UI kit · {'oscuro' if theme=='dark' else 'claro'} · D Editorial</span></div>
<div style="display:grid;grid-template-columns:repeat(12,1fr);gap:10px;margin:28px 0">{''.join(sw(k,P[k],0) for k in keys)}</div>
<div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:28px">
<div><p class="eyebrow">Botones</p><div style="display:flex;flex-direction:column;gap:10px;align-items:flex-start"><a class="btn btn-primary">Empezar lección</a><a class="btn btn-ghost">Ver temario</a><a class="btn btn-gold">Ver simulacro</a><a class="btn btn-link">Repasar errores</a><a class="btn btn-primary" disabled>Comprobar</a></div>
<p class="eyebrow" style="margin-top:22px">Formulario</p><input class="input" value="lucia@correo.es"><div style="height:10px"></div><input class="input focus" value="Tema 18"><div style="display:flex;gap:12px;align-items:center;margin-top:12px"><span class="toggle on"></span> Recordatorio diario <span class="toggle"></span> Sonido</div></div>
<div><p class="eyebrow">Respuestas</p><button class="opt"><span class="k">A</span>Ley 39/2015</button><button class="opt sel"><span class="k">B</span>Ley 16/1985</button><button class="opt ok"><span class="k">B</span>Ley 16/1985<span class="tag">Correcta</span></button><button class="opt bad"><span class="k">A</span>Ley 39/2015<span class="tag">Tu respuesta</span></button>
<p class="eyebrow" style="margin-top:16px">Badges y motivación</p><div style="display:flex;gap:8px;flex-wrap:wrap"><span class="badge ai">{ic('sparkle',12)} Contenido generado por IA</span><span class="badge warn">Sin fuente</span><span class="badge ok">Dominado</span><span class="badge bad">A repasar</span><span class="streak">{ic('flame',16)} 12 días</span><span class="xp">{ic('star',14)} 340 XP</span></div></div>
<div><p class="eyebrow">Tarjeta y vertical</p><div class="card"><span class="vtag"><span class="marker"></span>Museos · Tema 18</span><h2 style="font-size:22px;margin:10px 0 4px">Funciones del museo</h2><p class="subtle" style="font-size:14px">10 preguntas · ~6 min</p><div class="progress gold"><i style="width:64%"></i></div></div>
<div style="display:flex;gap:16px;margin:14px 0;flex-wrap:wrap">{''.join(f'<span class="vtag" data-vertical="{k}"><span class="marker"></span>{n}</span>' for k,n in VN)}</div>
<div class="toast ok">{ic('check',18)} Guardado en tus errores.</div><div style="height:8px"></div><div class="toast bad">{ic('x',18)} Sin conexión. Lo reintentamos.</div><div style="height:8px"></div><div class="toast warn">{ic('flag',18)} Quedan 5 minutos.</div></div></div>
<p class="eyebrow" style="margin-top:26px">Tipografía</p><div style="display:flex;gap:36px;align-items:baseline;flex-wrap:wrap"><span class="serif" style="font-size:48px">Display 48</span><span class="serif" style="font-size:34px">H1 34</span><span class="serif" style="font-size:26px">H2 26</span><span style="font:600 19px var(--font-sans)">H3 19 Plex</span><span>Body 16 Plex</span><span class="mono" style="font-size:14px">D = 68 − 21 ÷ 3</span></div>
<p class="eyebrow" style="margin-top:22px">Iconos · 24 px · trazo 1,5</p><div style="display:flex;gap:18px;flex-wrap:wrap">{''.join(ic(k,24) for k in json.load(open('icons/_list.json')))}</div></div>''',w=1280,h=900,theme=theme)
open('ui/ui-kit.html','w').write(kit('light'));open('ui/ui-kit-dark.html','w').write(kit('dark'))
# logo sheet
L=json.load(open('logo/_list.json'))
mis=''.join(f'<figure style="margin:0" class="card"><img src="../logo/aula-umbrella-horizontal.svg" style="height:40px;{s}"><figcaption class="subtle" style="font-size:12px;margin-top:8px">✕ {t}</figcaption></figure>' for s,t in [('transform:scaleX(1.4);transform-origin:left','No deformar'),('filter:hue-rotate(160deg) saturate(3)','No cambiar colores'),('transform:rotate(-10deg)','No girar'),('background:repeating-linear-gradient(45deg,#D9A21B 0 6px,#fff 6px 12px)','No sobre fondos ruidosos'),('opacity:.35','No bajar opacidad'),('filter:drop-shadow(3px 3px 0 #000)','No añadir sombras')])
cell=lambda n,dk=False,h=48:f'<figure style="margin:0;padding:18px;border-radius:12px;background:{"#142A3D" if dk else "#fff"};border:1px solid var(--line)"><img src="../logo/{n}.svg" style="height:{h}px;max-width:100%"><figcaption class="mono" style="font-size:10px;color:{"#B9BCC8" if dk else "#66697F"};margin-top:6px">{n}</figcaption></figure>'
open('ui/logo-sheet.html','w').write(page(f'''<div style="padding:36px 48px"><p class="eyebrow">Logotipo · «Aula.» — el punto significa «resuelto»</p>
<div style="display:grid;grid-template-columns:2fr 1fr 1fr 1fr;gap:14px;margin:14px 0">{cell('aula-umbrella-horizontal',h=64)}{cell('aula-stacked-light',h=110)}{cell('aula-mark-light',h=80)}{cell('aula-stacked-dark',True,110)}</div>
<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:14px">{''.join(cell(f'aula-{k}-horizontal',h=40) for k,_ in VN)}{''.join(cell(f'aula-{k}-on-dark',True,40) for k,_ in VN)}</div>
<div style="display:grid;grid-template-columns:1.3fr 2fr;gap:14px;margin-top:14px">{cell('aula-clearspace',h=150)}<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:10px">{mis}</div></div></div>''',w=1280,h=800))
# competitor check
comp=C['competitors'];alt=C['navy_alternative']
rows=''.join(f'<tr><td><span style="display:inline-block;width:18px;height:18px;border-radius:4px;background:{c["hex"]};vertical-align:middle"></span> {c["ours"]} <span class="mono">{c["hex"]}</span></td><td><span style="display:inline-block;width:18px;height:18px;border-radius:4px;background:{c["refhex"]};vertical-align:middle"></span> {c["ref"]} <span class="mono">{c["refhex"]}</span></td><td class="mono"><b>{c["dE2000"]}</b> {"✓" if c["dE2000"]>=10 else "⚠ &lt;10"}</td></tr>' for c in comp)
open('ui/competitor-check.html','w').write(page(f'''<div style="padding:32px 40px"><p class="eyebrow">Distancia de color vs competencia · ΔE2000 (objetivo ≥ 10)</p>
<table style="width:100%;border-collapse:collapse;font-size:14px;margin-top:10px">{rows}</table>
<p class="toast ok" style="margin-top:14px">Navy #142A3D (tinta petróleo): ΔE {[c for c in comp if c["ref"]=="MAD navy"][0]["dE2000"]} vs MAD #11184A y {[c for c in comp if c["ref"]=="OpositaTest navy"][0]["dE2000"]} vs OpositaTest #253B80; contraste {alt["on_paper"]}:1 sobre papel.</p></div>''',w=1080,h=520,extra='td{padding:7px 8px;border-bottom:1px solid var(--line)}'))
# templates
def tpl(body,w,h,dark=False): return page(body,w=w,h=h,theme='dark' if dark else 'light',extra=f'body{{height:{h}px}}')
open('templates/instagram-post.html','w').write(tpl(f'''<div style="padding:90px;height:1080px;display:flex;flex-direction:column;justify-content:space-between"><span class="vtag" style="font-size:26px;gap:14px"><span class="marker" style="width:20px;height:20px;border-radius:4px"></span>Museos · Pregunta del día</span>
<h1 style="font-size:84px;line-height:1.06">¿Qué ley regula el Patrimonio Histórico Español<span class="dot">?</span></h1>
<div style="display:flex;justify-content:space-between;align-items:flex-end"><p class="muted" style="font-size:30px;margin:0">Respuesta y fuente en la app.</p><img src="../logo/aula-umbrella-horizontal.svg" height="64"></div></div>''',1080,1080))
open('templates/instagram-story.html','w').write(tpl(f'''<div style="padding:120px 90px;height:1920px;display:flex;flex-direction:column;justify-content:space-between;background:#142A3D;color:#F4F1EA"><img src="../logo/aula-umbrella-on-dark.svg" height="70" style="align-self:flex-start">
<div><p class="eyebrow" style="font-size:26px;color:#B9BCC8">Estudia con método</p><h1 style="font-size:132px;line-height:1.02;color:#F4F1EA">Menos ruido<span class="dot">.</span><br>Más temario<span class="dot">.</span></h1>
<p style="font-size:38px;color:#B9BCC8;margin-top:30px">Cada respuesta, explicada con la norma.</p></div>
<div style="display:flex;gap:30px;flex-wrap:wrap">{''.join(f'<span class="vtag" data-theme="dark" data-vertical="{k}" style="font-size:30px;color:#F4F1EA;gap:14px"><span class="marker" style="width:18px;height:18px;border-radius:4px"></span>{n}</span>' for k,n in VN)}</div></div>''',1080,1920))
open('templates/og-image.html','w').write(tpl(f'''<div style="padding:72px;height:630px;display:flex;flex-direction:column;justify-content:space-between"><img src="../logo/aula-umbrella-horizontal.svg" height="56" style="align-self:flex-start"><h1 style="font-size:88px;line-height:1.02">Menos ruido<span class="dot">.</span> Más temario<span class="dot">.</span></h1><p class="muted" style="font-size:26px;margin:0">aulaoposiciones.es · Oposiciones con método</p></div>''',1200,630))
sig='<table cellpadding="0" cellspacing="0" style="font-family:\'IBM Plex Sans\',Arial,sans-serif;color:#142A3D"><tr><td style="padding-right:16px;border-right:2px solid #D9A21B"><img src="https://aulaoposiciones.es/email/aula-mark.png" width="48" height="48" alt="Aula."></td><td style="padding-left:16px"><b style="font-family:Fraunces,Georgia,serif;font-size:17px;font-weight:600">Equipo Aula</b><br><span style="font-size:13px;color:#4A5068">hola@aulaoposiciones.es · aulaoposiciones.es</span><br><span style="font-size:12px;color:#66697F">Menos ruido. Más temario.</span></td></tr></table>'
open('templates/email-signature.html','w').write(sig)
open('templates/email-signature-preview.html','w').write(page('<div style="padding:24px">'+sig.replace('https://aulaoposiciones.es/email/aula-mark.png','../logo/png/aula-mark-light.png')+'</div>',w=520,h=140))
AS=[('Menos ruido.<br>Más temario.','home'),('Cada respuesta,<br>explicada con la norma.','explanation'),('Simulacros con<br>el formato real.','simulacro'),('Tu nota,<br>calculada como en el examen.','result')]
for i,(t,s) in enumerate(AS,1):
  open(f'templates/appstore-6.7-{i}.html','w').write(tpl(f'''<div style="padding:56px 30px 0;height:932px;text-align:center;{'background:#142A3D;color:#F4F1EA' if i%2==0 else ''}"><h1 style="font-size:34px;line-height:1.12;{'color:#F4F1EA' if i%2==0 else ''}">{t}</h1><img src="../screens/{s}.png" style="width:330px;border-radius:40px;margin-top:28px;border:8px solid {'#213848' if i%2==0 else '#fff'};box-shadow:0 20px 50px rgba(20,42,61,.18)"></div>''',430,932))
print('ok')
