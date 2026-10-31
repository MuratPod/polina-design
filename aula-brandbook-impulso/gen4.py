import re,pathlib
def ic(n,s=20,c='currentColor'):
  t=open(f'icons/{n}.svg').read();return re.sub(r'width="24" height="24"',f'width="{s}" height="{s}" class="ic" style="color:{c}"',t)
def page(body,w=390,h=844,theme='light',vert='museos',extra='',up='../'):
  return f'''<!doctype html><html lang="es" data-theme="{theme}" data-vertical="{vert}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><link rel="stylesheet" href="{up}ui/aula-ui.css"><style>body{{width:{w}px;min-height:{h}px;position:relative;overflow:hidden}}{extra}</style></head><body>{body}</body></html>'''
LOGO=lambda dark=False:f'<img src="../logo/aula-museos-{"on-dark" if dark else "horizontal"}.svg" height="34" alt="aula! museos">'
TAB=lambda on: '<nav class="tabbar" style="position:absolute;left:0;right:0;bottom:0">'+''.join(f'<span class="tab{" on" if k==on else ""}">{ic(i,24)}{k}</span>' for k,i in [('Hoy','home'),('Temario','book'),('Simulacro','timer'),('Errores','refresh'),('Perfil','user')])+'</nav>'
S={}
def home(theme):
  d=theme=='dark'
  return f'''<div class="navy" style="padding:18px 20px 24px;border-radius:0 0 28px 28px">
<div style="display:flex;justify-content:space-between;align-items:center">{LOGO(True)}<span class="streak">{ic('flame',18)} 12</span></div>
<h1 style="font-size:28px;margin:20px 0 4px;color:#fff">¡Hola, Lucía!</h1><p style="margin:0 0 16px;color:#A9B4D0;font-weight:700">Llevas 12 días seguidos. Hoy toca el tema 18.</p>
<div style="background:rgba(255,255,255,.07);border-radius:18px;padding:14px;border:1px solid rgba(255,255,255,.12)">
<div style="display:flex;justify-content:space-between;font-weight:800"><span>Meta diaria · Regular</span><span class="mono" style="color:var(--gold)">32 / 50 XP</span></div>
<div class="progress gold" style="margin:10px 0;background:rgba(255,255,255,.14)"><i style="width:64%"></i></div>
<div style="display:flex;gap:6px">{''.join(f'<span style="flex:1;text-align:center;font:900 12px var(--font-sans);padding:6px 0;border-radius:10px;{"background:var(--gold);color:var(--navy-900)" if i<4 else "background:rgba(255,255,255,.08);color:#A9B4D0"}">{x}</span>' for i,x in enumerate('LMXJVSD'))}</div></div></div>
<main style="padding:18px 20px">
<div class="card v" style="margin-bottom:14px"><span class="badge badge-v">{ic('museum',14)} Museos</span>
<h2 style="font-size:21px;margin:10px 0 2px">Lección de hoy</h2><p class="muted" style="margin:0 0 14px;font-weight:700">Tema 18 · Funciones del museo · 10 preguntas · ~6 min</p>
<a class="btn btn-primary big full">{ic('arrow-right',20)} Empezar lección</a></div>
<div class="card" style="display:flex;gap:14px;align-items:center"><img src="../illustrations/simulacro.svg" width="64" alt="">
<div style="flex:1"><h3 style="font-size:18px;margin:0">Simulacro completo</h3><p class="muted mono" style="margin:2px 0 0;font-size:13px;font-weight:600">100 + 10 · 100 min · +1 / 0 / −1/3</p></div>{ic('arrow-right',22)}</div>
<div style="display:flex;gap:8px;margin-top:14px"><span class="xp">{ic('star',16)} 340 XP esta semana</span><span class="chip">{ic('refresh',16)}&nbsp;8 errores por repasar</span></div>
</main>{TAB('Hoy')}'''
S['home']=page(home('light'));S['home-dark']=page(home('dark'),theme='dark')
OPTS=[('A','Ley 39/2015'),('B','Ley 16/1985'),('C','Real Decreto 1495/2011'),('D','Ley 10/2015')]
def qhead(n): return f'''<div style="padding:16px 20px 0"><div style="display:flex;align-items:center;gap:12px">{ic('x',24)}<div class="progress" style="flex:1"><i style="width:{n*10}%"></i></div><span class="streak" style="padding:4px 10px">{ic('flame',16)} 12</span></div>
<p class="muted" style="font-weight:800;margin:14px 0 6px;font-size:14px">Pregunta {n} de 10 · Tema 7 · <span style="color:var(--v-museos)">Museos</span></p>
<h1 style="font-size:24px">¿Qué ley regula el Patrimonio Histórico Español?</h1></div>'''
def opts(state):
  out=''
  for k,t in OPTS:
    cls={'sel':{'B':'sel'},'ans':{'A':'bad','B':'ok'}}[state].get(k,'');tag={'ok':'Correcta','bad':'Tu respuesta'}.get(cls,'')
    out+=f'<button class="opt {cls}"><span class="k">{k}</span>{t}<span class="tag">{tag}</span></button>'
  return out
S['question']=page(qhead(4)+f'<main style="padding:10px 20px">{opts("sel")}</main><div style="position:absolute;left:20px;right:20px;bottom:30px"><a class="btn btn-primary big full">Comprobar</a></div>')
S['explanation']=page(qhead(4)+f'''<main style="padding:10px 20px">{opts("ans")}
<div class="explain bad"><div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:6px"><b style="color:var(--error)">¡Casi! Era la B.</b><span class="badge ai">{ic('sparkle',13)} Contenido generado por IA</span></div>
<p style="margin:0 0 8px;font-weight:600">La Ley 16/1985 es la norma básica del Patrimonio Histórico Español. La Ley 39/2015 regula el procedimiento administrativo común: buena pista para descartarla.</p>
<div class="src">{ic('source',14)} Fuente: <a>Ley 16/1985, de 25 de junio, del Patrimonio Histórico Español (BOE-A-1985-12534)</a></div></div>
</main><div style="position:absolute;left:20px;right:20px;bottom:30px;display:flex;gap:10px"><a class="btn btn-ghost" style="flex:none">{ic('bookmark',20)}</a><a class="btn btn-primary big" style="flex:1">Siguiente</a></div>''')
S['result']=page(f'''<div class="navy" style="padding:22px 20px 26px;text-align:center;border-radius:0 0 28px 28px">
<p style="margin:0;color:#A9B4D0;font-weight:800">Simulacro completo · Museos</p>
<div class="mono" style="font-size:64px;font-weight:800;color:var(--gold);line-height:1.1;margin:8px 0 0">21,64</div><p style="margin:0;color:#F3F5FB;font-weight:800">sobre 30</p>
<div style="position:relative;height:12px;background:rgba(255,255,255,.14);border-radius:99px;margin:18px 0 6px"><i style="position:absolute;left:0;top:0;bottom:0;width:72.1%;background:var(--gold);border-radius:99px"></i><span style="position:absolute;left:50%;top:-6px;width:3px;height:24px;background:#fff;border-radius:2px"></span></div>
<div style="display:flex;justify-content:space-between;font:700 12px var(--font-sans);color:#A9B4D0"><span>0</span><span>15 · nota de corte orientativa</span><span>30</span></div></div>
<main style="padding:18px 20px">
<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:8px;margin-bottom:14px;text-align:center">
<div class="card" style="padding:12px"><b class="mono" style="font-size:24px;color:var(--success)">68</b><br><small class="muted" style="font-weight:800">aciertos</small></div>
<div class="card" style="padding:12px"><b class="mono" style="font-size:24px;color:var(--error)">21</b><br><small class="muted" style="font-weight:800">errores</small></div>
<div class="card" style="padding:12px"><b class="mono" style="font-size:24px;color:var(--muted)">11</b><br><small class="muted" style="font-weight:800">en blanco</small></div></div>
<div class="card" style="margin-bottom:14px"><h3 style="font-size:16px">Cómo se calcula</h3>
<p class="code" style="font-size:13px;margin:0;line-height:1.7">D = 68 − 21 ÷ 3 = 61,00<br>C = 30 (corte)<br>D ≥ C → 15 + (61 − 30) ÷ (100 − 30) × 15 = <b>21,64</b></p></div>
<div class="toast info" style="margin-bottom:14px">{ic('trophy',20)} ¡Por encima del corte orientativo! Repasa tus 21 errores para subir más.</div>
<a class="btn btn-primary big full">Repasar errores</a></main>''')
cells=''
import random;random.seed(4)
for i in range(1,101):
  st='ans' if i<64 else ('cur' if i==64 else ('mark' if i in (12,37,58,71) else 'blank'))
  if i in(12,37,58):st='mark'
  sty={'ans':'background:var(--blue);color:#fff;border-color:var(--blue)','cur':'background:#fff;border-color:var(--ink);box-shadow:0 0 0 3px var(--gold)','mark':'background:var(--coral-100);border-color:var(--coral-700);color:var(--coral-700)','blank':'background:#fff'}[st]
  cells+=f'<span style="display:grid;place-items:center;height:30px;border-radius:8px;border:2px solid var(--line);font:800 11px var(--font-mono);{sty}">{i}</span>'
S['simulacro']=page(f'''<div class="navy" style="padding:16px 20px;display:flex;justify-content:space-between;align-items:center"><b style="font-size:17px">Simulacro · Museos</b><span class="mono" style="background:rgba(255,255,255,.1);padding:6px 12px;border-radius:99px;color:var(--gold);font-weight:800">{ic('timer',16)} 63:12</span></div>
<main style="padding:14px 20px"><div style="display:flex;justify-content:space-between;font-weight:800;font-size:14px;margin-bottom:8px"><span>63 respondidas · 3 marcadas</span><span class="muted">37 sin responder</span></div>
<div style="display:flex;gap:4px;margin-bottom:10px">{''.join(f'<span style="flex:{f};height:6px;border-radius:9px;background:{c}"></span>' for f,c in [(30,'#1B2140'),(30,'#5A5F78'),(40,'#A69C8A')])}</div>
<div style="display:grid;grid-template-columns:repeat(10,1fr);gap:4px">{cells}</div>
<div style="display:flex;gap:12px;flex-wrap:wrap;font-size:12px;font-weight:800;margin:12px 0" class="muted"><span>■ <span style="color:var(--blue)">respondida</span></span><span><span style="color:var(--coral-700)">■</span> marcada</span><span>□ sin responder</span><span>Bloques: Legislación 30 · Museología 30 · Patrimonio 40</span></div>
<p class="muted" style="font-size:13px;font-weight:700;margin:0 0 12px">+ 10 preguntas de reserva · sin pausa · +1 / 0 / −1/3</p>
<div style="display:flex;gap:10px"><a class="btn btn-ghost" style="flex:1">Volver a la 64</a><a class="btn btn-navy" style="flex:1">Entregar</a></div></main>''')
pathlib.Path('screens').mkdir(exist_ok=True)
for k,v in S.items(): open(f'screens/{k}.html','w').write(v)
print(list(S))
