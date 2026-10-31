import json,pathlib,re
from gen4 import ic,page
T=json.load(open('tokens/_t.json'));C=json.load(open('tokens/contrast.json'))
# ---------- web header/hero/footer
def site(mobile):
  W=390 if mobile else 1280
  nav='' if mobile else '<nav style="display:flex;gap:28px;font-weight:800">'+''.join(f'<a>{x}</a>' for x in ['Oposiciones','Cómo funciona','Simulacros','Preguntas'])+'</nav>'
  verts=''.join(f'<span class="badge" style="background:{T["vertical"][k]["light"]};color:#fff;font-size:14px;padding:6px 12px">{n}</span>' for k,n in [('museos','Museos'),('justicia','Justicia'),('policia','Policía'),('educacion','Educación')])
  hero_img='' if mobile else '<img src="../screens/home.png" style="width:300px;border-radius:36px;border:8px solid #0B1530;box-shadow:0 30px 60px rgba(0,0,0,.35);transform:rotate(3deg)">'
  pad='20px' if mobile else '64px'
  return page(f'''<header style="display:flex;justify-content:space-between;align-items:center;padding:18px {pad};background:var(--bg)"><img src="../logo/aula-umbrella-horizontal.svg" height="{34 if mobile else 40}" alt="aula!">{nav}<a class="btn btn-primary" style="padding:{'10px 16px;font-size:15px' if mobile else '12px 20px'}">{'Empieza' if mobile else 'Empieza gratis'}</a></header>
<section class="navy" style="padding:{'36px 20px 40px' if mobile else '72px 64px'};display:flex;gap:48px;align-items:center;justify-content:space-between">
<div style="max-width:600px"><span class="streak" style="margin-bottom:18px">{ic('flame',18)} Un poco cada día</span>
<h1 style="font-size:{40 if mobile else 64}px;color:#fff;margin:16px 0 12px">Estudia como<br>se <span style="color:var(--gold)">examina</span><span style="color:#FF7A85">!</span></h1>
<p style="font-size:{17 if mobile else 20}px;color:#C9D2E8;font-weight:600;margin:0 0 20px"><b style="color:#fff">Nuestra misión:</b> que prepares tu oposición con constancia y sin agobios, con lecciones cortas, simulacros con el formato real y explicaciones que citan su fuente.</p>
<div style="display:flex;gap:12px;flex-wrap:wrap"><a class="btn btn-primary big" style="{'width:100%' if mobile else ''}">Empieza gratis</a><a class="btn btn-gold" style="{'width:100%' if mobile else ''}">Ver cómo funciona</a></div>
<div style="display:flex;gap:8px;flex-wrap:wrap;margin-top:22px">{verts}</div></div>{hero_img}</section>
<section style="padding:{'32px 20px' if mobile else '56px 64px'};display:grid;grid-template-columns:{'1fr' if mobile else 'repeat(3,1fr)'};gap:20px">
{''.join(f'<div class="card"><img src="../illustrations/{i}.svg" width="72" alt=""><h3>{t}</h3><p class="muted" style="margin:0;font-weight:600">{d}</p></div>' for i,t,d in [('racha','Lecciones de 5 minutos','Una meta diaria a tu medida y tu racha para no perder el ritmo.'),('simulacro','Simulacros reales','Mismo número de preguntas, tiempo y penalización que el examen.'),('temario','Todo el temario','Por bloques y temas, con tus errores siempre a mano.')])}</section>
<footer style="background:var(--navy-900);color:#A9B4D0;padding:{'28px 20px' if mobile else '40px 64px'};display:flex;flex-direction:{'column' if mobile else 'row'};gap:18px;justify-content:space-between;align-items:{'flex-start' if mobile else 'center'}">
<img src="../logo/aula-umbrella-on-dark.svg" height="36" alt="aula!"><span style="font-weight:700;font-size:14px"><a style="color:#F3F5FB">Aviso legal</a> · <a style="color:#F3F5FB">Privacidad</a> · <a style="color:#F3F5FB">Cookies</a><br>Aula es una herramienta independiente, no afiliada a ningún ministerio ni organismo público.</span><span style="font-size:13px">© 2026 Aula</span></footer>''',w=W,h=800)
pathlib.Path('web').mkdir(exist_ok=True)
open('web/site-desktop.html','w').write(site(False));open('web/site-mobile.html','w').write(site(True))
# ---------- templates
def tpl(name,w,h,body):
  open(f'templates/{name}.html','w').write(page(body,w=w,h=h).replace('body{width','body{margin:0;width'))
tpl('instagram-post',1080,1080,f'''<div class="navy" style="width:1080px;height:1080px;padding:90px;display:flex;flex-direction:column;justify-content:space-between">
<img src="../logo/aula-umbrella-on-dark.svg" height="70" style="align-self:flex-start"><div><span class="streak" style="font-size:34px;padding:12px 26px">{ic('flame',38)} 30 días</span>
<h1 style="font-size:104px;color:#fff;margin:36px 0 0;line-height:1.02">Un mes seguido<br>estudiando.<br><span style="color:var(--gold)">Eso es método.</span></h1></div>
<p style="font-size:34px;color:#C9D2E8;font-weight:700;margin:0">Estudia como se examina · aulaoposiciones.es</p></div>''')
tpl('instagram-story',1080,1920,f'''<div style="width:1080px;height:1920px;background:var(--bg);padding:110px 90px;display:flex;flex-direction:column;gap:50px">
<img src="../logo/aula-umbrella-horizontal.svg" height="80" style="align-self:flex-start"><h1 style="font-size:110px;line-height:1.02;margin:40px 0 0">¿Te atreves con<br>un <span style="color:var(--coral-700)">simulacro</span><br>de verdad?</h1>
<p style="font-size:42px;font-weight:700;color:var(--muted);margin:0">100 + 10 preguntas · 100 minutos<br>Puntuación: +1 / 0 / −1/3</p>
<img src="../screens/result.png" style="width:640px;align-self:center;border-radius:60px;border:14px solid #0B1530;box-shadow:0 40px 80px rgba(0,0,0,.25)">
<a class="btn btn-primary big" style="font-size:44px;padding:36px;margin-top:auto">Empieza gratis</a></div>''')
tpl('og-image',1200,630,f'''<div class="navy" style="width:1200px;height:630px;padding:70px;display:flex;justify-content:space-between;align-items:center">
<div><img src="../logo/aula-umbrella-on-dark.svg" height="64"><h1 style="font-size:84px;color:#fff;margin:40px 0 16px;line-height:1.02">Estudia como<br>se <span style="color:var(--gold)">examina</span><span style="color:#FF7A85">!</span></h1><p style="font-size:28px;color:#C9D2E8;font-weight:700;margin:0">Oposiciones · lecciones diarias · simulacros reales</p><p style="font-size:24px;color:var(--gold);font-weight:800;margin:10px 0 0">aulaoposiciones.es</p></div>
<img src="../illustrations/racha.svg" width="300"></div>''')
frames=[('Un poco cada día.<br>Tu racha te espera.','home'),('Explicaciones al instante,<br>con su fuente.','explanation'),('Simulacros con el<br>formato real.','simulacro'),('Tu nota 0–30,<br>sin cajas negras.','result')]
for i,(t,s) in enumerate(frames,1):
  bg='navy' if i%2 else ''
  tpl(f'appstore-6.7-{i}',430,932,f'''<div class="{bg}" style="width:430px;height:932px;{'' if bg else 'background:var(--bg);'}padding:48px 28px 0;text-align:center;overflow:hidden">
<h1 style="font-size:31px;line-height:1.12;{'color:#fff' if bg else ''}">{t}</h1><img src="../screens/{s}.png" style="width:330px;margin-top:26px;border-radius:44px;border:10px solid #0B1530;box-shadow:0 30px 60px rgba(0,0,0,.3)"></div>''')
open('templates/email-signature.html','w').write('''<!-- Firma de email aula! · pegar en el cliente de correo (tablas + estilos inline).
     Nota: el dominio aulaoposiciones.es aún no está activo; la imagen debe alojarse allí antes de usar la firma. -->
<table cellpadding="0" cellspacing="0" role="presentation" style="font-family:Nunito,Arial,sans-serif;color:#1B2140;font-size:14px;line-height:1.4">
<tr><td style="padding-right:14px;border-right:3px solid #FF4250"><img src="https://aulaoposiciones.es/brand/favicon-96.png" width="48" height="48" alt="aula!" style="border-radius:13px;display:block"></td>
<td style="padding-left:14px"><b style="font-size:16px">Equipo Aula</b><br>
<a href="mailto:hola@aulaoposiciones.es" style="color:#2449D8;text-decoration:none;font-weight:700">hola@aulaoposiciones.es</a> · <a href="https://aulaoposiciones.es" style="color:#2449D8;text-decoration:none;font-weight:700">aulaoposiciones.es</a><br>
<span style="color:#C8162B;font-weight:800">Estudia como se examina.</span></td></tr></table>''')
open('templates/email-signature-preview.html','w').write(page('<div style="padding:24px 30px;background:#fff;height:120px">'+open('templates/email-signature.html').read()+'</div>',w=520,h=120).replace('https://aulaoposiciones.es/brand/favicon-96.png','../favicon/favicon-96.png'))
# ---------- UI kit
V=T['vertical']
kit=f'''<div style="padding:40px;display:grid;grid-template-columns:1fr 1fr;gap:28px">
<div class="card"><h3>Botones</h3><div style="display:flex;gap:10px;flex-wrap:wrap"><a class="btn btn-primary big">Empezar</a><a class="btn btn-primary">Comprobar</a><a class="btn btn-blue">Continuar</a><a class="btn btn-ghost">Saltar</a><a class="btn btn-navy">Entregar</a><a class="btn btn-gold">Ver racha</a><button class="btn" disabled>Desactivado</button></div></div>
<div class="card"><h3>Campos</h3><label class="label">Correo electrónico</label><input class="input" value="lucia@correo.es"><div style="height:10px"></div><input class="input" placeholder="Busca un tema"><div style="height:10px"></div><input class="input err" value="lucia@"><small style="color:var(--error);font-weight:800">Revisa el correo: falta el dominio.</small></div>
<div class="card"><h3>Opciones de respuesta</h3><button class="opt"><span class="k">A</span>Por defecto</button><button class="opt sel"><span class="k">B</span>Seleccionada</button><button class="opt ok"><span class="k">C</span>Correcta<span class="tag">Correcta</span></button><button class="opt bad"><span class="k">D</span>Incorrecta<span class="tag">Tu respuesta</span></button></div>
<div class="card"><h3>Progreso, racha, XP</h3><div class="progress"><i style="width:40%"></i></div><div style="height:10px"></div><div class="progress gold"><i style="width:75%"></i></div><div style="display:flex;gap:10px;margin-top:16px;flex-wrap:wrap"><span class="streak">{ic('flame',18)} 12</span><span class="xp">{ic('star',16)} +10 XP</span><span class="xp">{ic('star',16)} 340 XP</span><span class="chip on">Regular · 50 XP</span><span class="chip">Ligera · 30</span><span class="chip">Intensa · 80</span></div>
<div style="margin-top:16px"><img src="../illustrations/racha.svg" width="56" style="vertical-align:middle"> <b>Día de descanso automático:</b> <span class="muted">uno por semana, sin perder la racha.</span></div></div>
<div class="card"><h3>Etiqueta IA y fuente</h3><span class="badge ai">{ic('sparkle',13)} Contenido generado por IA</span><div class="src" style="margin:8px 0 16px">{ic('source',14)} Fuente: <a>Ley 16/1985, art. 59.3</a></div><span class="badge ai">{ic('sparkle',13)} Contenido generado por IA</span> <span class="badge nosrc">Sin fuente</span><p class="muted" style="font-size:13px;margin:8px 0 0">Sin fuente: aviso ámbar, nunca se oculta.</p></div>
<div class="card"><h3>Badges de vertical y tarjetas</h3><div style="display:flex;gap:8px;flex-wrap:wrap">{''.join(f'<span class="badge" style="background:{V[k]["light"]};color:#fff">{ic(i,13)} {n}</span>' for k,n,i in [('museos','Museos','museum'),('justicia','Justicia','scale'),('policia','Policía','shield'),('educacion','Educación','school')])}</div>
<div class="card" style="border-left:6px solid {V["justicia"]["light"]};margin-top:14px;padding:14px"><b>Tarjeta con línea de vertical</b><br><span class="muted">Línea izquierda 6px = color de la vertical.</span></div></div>
<div class="card"><h3>Toasts</h3><div class="toast ok" style="margin-bottom:8px">{ic('check',20)} ¡Correcta! +10 XP</div><div class="toast bad" style="margin-bottom:8px">{ic('x',20)} Casi. Mira la explicación.</div><div class="toast info">{ic('flame',20)} ¡Racha de 12 días! Sigue así.</div></div>
<div class="card" style="padding:0;overflow:hidden"><h3 style="padding:20px 20px 0">Barra de pestañas</h3><nav class="tabbar">{''.join(f'<span class="tab{" on" if k=="Hoy" else ""}">{ic(i,24)}{k}</span>' for k,i in [('Hoy','home'),('Temario','book'),('Simulacro','timer'),('Errores','refresh'),('Perfil','user')])}</nav></div>
</div>'''
pathlib.Path('ui').mkdir(exist_ok=True)
open('ui/ui-kit.html','w').write(page(kit,w=1280,h=900))
open('ui/ui-kit-dark.html','w').write(page(kit,w=1280,h=900,theme='dark'))
# ---------- coral vs reference
cv=C['coral_vs_reference']
sw=f'''<div style="padding:40px;width:1000px"><h2 style="font-size:28px">Coral final vs. referencia competidor</h2><div style="display:flex;gap:24px;margin:20px 0">
<div style="flex:1"><div style="height:220px;border-radius:24px;background:#FF4250"></div><h3 style="margin-top:12px">aula! coral · #FF4250</h3><p class="muted" style="font-weight:700;margin:0">Tono {cv["hue_final"]}° · texto: #C8162B</p></div>
<div style="flex:1"><div style="height:220px;border-radius:24px;background:#EF7746"></div><h3 style="margin-top:12px">Referencia competidor · #EF7746</h3><p class="muted" style="font-weight:700;margin:0">Tono {cv["hue_ref"]}°</p></div></div>
<div class="card"><b>Diferencia de tono: {cv["hue_diff"]}° · ΔE2000 = {cv["dE2000"]}</b> <span class="muted">(el coral anterior #FF6B3D estaba a ΔE {cv["dE2000_old_FF6B3D"]}, casi idéntico). ΔE &gt; 10 = claramente distinto a simple vista.</span></div></div>'''
open('ui/coral-vs-reference.html','w').write(page(sw,w=1080,h=520))
# ---------- logo sheet
L=json.load(open('logo/_list.json'))
ls='<div style="padding:30px;display:grid;grid-template-columns:repeat(3,1fr);gap:16px;width:1280px">'+''.join(f'<div class="card" style="padding:14px;{"background:#0B1530" if "dark" in n else ""}"><img src="../logo/{n}.svg" style="max-width:100%;height:56px"><br><small class="muted">{n}</small></div>' for n in L if 'symbol' not in n)+'</div><div style="padding:0 30px 30px;display:flex;gap:12px;flex-wrap:wrap">'+''.join(f'<img src="../logo/{n}.svg" height="64">' for n in L if 'symbol' in n)+'</div>'
open('ui/logo-sheet.html','w').write(page(ls,w=1280,h=800))
print('ok')
