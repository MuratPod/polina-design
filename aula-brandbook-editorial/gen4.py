import re,pathlib
def ic(n,s=20,c='currentColor'):
  t=open(f'icons/{n}.svg').read();return re.sub(r'width="24" height="24"',f'width="{s}" height="{s}" class="ic" style="color:{c}"',t)
def page(body,w=390,h=844,theme='light',vert='museos',extra='',up='../'):
  return f'''<!doctype html><html lang="es" data-theme="{theme}" data-vertical="{vert}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><link rel="stylesheet" href="{up}ui/aula-ui.css"><style>body{{width:{w}px;min-height:{h}px;position:relative;overflow:hidden}}{extra}</style></head><body>{body}</body></html>'''
LOGO=lambda dark=False,h=30:f'<img src="../logo/aula-museos-{"on-dark" if dark else "horizontal"}.svg" height="{h}" alt="Aula. Museos">'
TAB=lambda on: '<nav class="tabbar" style="position:absolute;left:0;right:0;bottom:0">'+''.join(f'<span class="tab{" on" if k==on else ""}">{ic(i,22)}{k}</span>' for k,i in [('Hoy','home'),('Temario','book'),('Simulacro','timer'),('Errores','refresh'),('Perfil','user')])+'</nav>'
S={}
def home(d):
  return f'''<div style="padding:18px 20px 6px;display:flex;justify-content:space-between;align-items:center">{LOGO(d)}<span class="streak">{ic('flame',16)} 12 días</span></div>
<main style="padding:14px 20px">
<p class="eyebrow" style="margin:0 0 6px">Sábado, 31 de octubre</p>
<h1 style="font-size:32px">Buenos días, Lucía<span class="dot">.</span></h1>
<p class="muted" style="margin:0 0 18px">Hoy toca el tema 18. Diez preguntas, unos seis minutos.</p>
<div class="card" style="margin-bottom:14px"><span class="vtag"><span class="marker"></span>Museos · Tema 18</span>
<h2 style="font-size:23px;margin:10px 0 4px">Funciones del museo</h2><p class="muted" style="font-size:14px;margin:0 0 14px">10 preguntas · ~6 min · 3 errores pendientes</p>
<a class="btn btn-primary big full">Empezar lección {ic('arrow-right',18)}</a></div>
<div class="card" style="margin-bottom:14px"><div style="display:flex;justify-content:space-between;align-items:baseline"><b style="font-weight:600">Meta diaria</b><span class="mono subtle" style="font-size:13px">32 / 50 XP</span></div>
<div class="progress gold" style="margin:10px 0 12px"><i style="width:64%"></i></div>
<div style="display:flex;justify-content:space-between">{''.join(f'<span style="display:flex;flex-direction:column;align-items:center;gap:6px;font:500 12px var(--font-sans);color:var(--subtle)"><i style="width:8px;height:8px;border-radius:50%;{"background:var(--gold)" if i<5 else "border:1.5px solid var(--line)"}"></i>{x}</span>' for i,x in enumerate('LMXJVSD'))}</div></div>
<div class="card" style="display:flex;gap:14px;align-items:center">{ic('timer',26)}<div style="flex:1"><h3 style="font-size:17px;margin:0">Simulacro completo</h3><p class="subtle mono" style="margin:2px 0 0;font-size:12px">100 + 10 preguntas · 100 min · +1 / 0 / −1/3</p></div>{ic('arrow-right',20)}</div>
</main>{TAB('Hoy')}'''
S['home']=page(home(False));S['home-dark']=page(home(True),theme='dark')
OPTS=[('A','Ley 39/2015'),('B','Ley 16/1985'),('C','Real Decreto 1495/2011'),('D','Ley 10/2015')]
def qhead(n): return f'''<div style="padding:16px 20px 0"><div style="display:flex;align-items:center;gap:14px">{ic('x',22)}<div class="progress" style="flex:1"><i style="width:{n*10}%"></i></div><span class="mono subtle" style="font-size:13px">{n}/10</span></div>
<p style="margin:22px 0 8px" class="vtag"><span class="marker"></span>Museos · Tema 7 · Patrimonio</p>
<h1 style="font-size:26px;margin-bottom:18px">¿Qué ley regula el Patrimonio Histórico Español?</h1></div>'''
def opts(state):
  o=''
  for k,t in OPTS:
    cls={'sel':{'B':'sel'},'ans':{'A':'bad','B':'ok'}}[state].get(k,'');tag={'ok':'Correcta','bad':'Tu respuesta'}.get(cls,'')
    o+=f'<button class="opt {cls}"><span class="k">{k}</span>{t}<span class="tag">{tag}</span></button>'
  return o
S['question']=page(qhead(4)+f'<main style="padding:0 20px">{opts("sel")}</main><div style="position:absolute;left:20px;right:20px;bottom:30px"><a class="btn btn-primary big full">Comprobar</a></div>')
S['explanation']=page(qhead(4)+f'''<main style="padding:0 20px">{opts("ans")}
<div class="explain"><div style="display:flex;justify-content:space-between;align-items:center;gap:8px;margin-bottom:8px;flex-wrap:wrap"><b class="serif" style="font-size:18px">Era la B<span class="dot">.</span></b><span class="badge ai">{ic('sparkle',12)} Contenido generado por IA</span></div>
<p style="font-size:15px">La Ley 16/1985 es la norma básica del Patrimonio Histórico Español. La 39/2015 regula el procedimiento administrativo común.</p>
<div class="src">{ic('source',14)}<span>Fuente: <a>Ley 16/1985, de 25 de junio, del Patrimonio Histórico Español (BOE-A-1985-12534)</a></span></div></div>
</main><div style="position:absolute;left:20px;right:20px;bottom:30px;display:flex;gap:10px"><a class="btn btn-ghost">{ic('bookmark',20)}</a><a class="btn btn-primary big" style="flex:1">Siguiente</a></div>''')
S['result']=page(f'''<div style="padding:18px 20px 0">{LOGO()}</div><main style="padding:18px 20px">
<p class="vtag" style="margin:0 0 8px"><span class="marker"></span>Simulacro completo · Museos</p>
<div style="display:flex;align-items:baseline;gap:10px"><span class="serif" style="font-size:72px;line-height:1">21,64</span><span class="muted">sobre 30</span></div>
<div style="position:relative;height:6px;background:var(--line);border-radius:6px;margin:20px 0 8px"><i style="position:absolute;left:0;top:0;bottom:0;width:72.1%;background:var(--ink);border-radius:6px"></i><span style="position:absolute;left:50%;top:-6px;width:2px;height:18px;background:var(--gold)"></span></div>
<div style="display:flex;justify-content:space-between;font:500 12px var(--font-sans);color:var(--subtle);margin-bottom:18px"><span>0</span><span>15 · nota de corte orientativa</span><span>30</span></div>
<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:8px;margin-bottom:14px">
{''.join(f'<div class="card" style="padding:12px"><b class="mono" style="font-size:22px;font-weight:500;color:var({c})">{n}</b><br><small class="subtle">{t}</small></div>' for n,t,c in [(68,'aciertos','--success'),(21,'errores','--error'),(11,'en blanco','--muted')])}</div>
<div class="card" style="margin-bottom:14px"><h3 style="font-size:15px">Cómo se calcula</h3>
<p class="code" style="font-size:12px;margin:0;line-height:1.75">D = 68 − 21 ÷ 3 = 61,00<br>C = 30 (corte)<br>D ≥ C → 15 + (61 − 30) ÷ (100 − 30) × 15<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;= <b>21,64</b></p></div>
<div class="toast ok" style="margin-bottom:14px">{ic('check',18)} Por encima del corte orientativo. Repasa tus 21 errores.</div>
<a class="btn btn-primary big full">Repasar errores</a></main>''')
cells=''
for i in range(1,101):
  st='ans' if i<64 else ('cur' if i==64 else 'blank')
  if i in(12,37,58,71):st='mark'
  sty={'ans':'background:var(--ink);color:var(--bg);border-color:var(--ink)','cur':'background:var(--surface);border-color:var(--ink);box-shadow:0 0 0 2px var(--gold)','mark':'background:var(--gold-100);border-color:var(--gold);color:var(--gold-text)','blank':'background:var(--surface)'}[st]
  cells+=f'<span style="display:grid;place-items:center;height:28px;border-radius:5px;border:1px solid var(--line);font:500 11px var(--font-mono);{sty}">{i}</span>'
S['simulacro']=page(f'''<div style="padding:16px 20px;display:flex;justify-content:space-between;align-items:center;border-bottom:1px solid var(--line)"><span class="vtag" style="color:var(--ink);font-size:15px"><span class="marker"></span>Simulacro · Museos</span><span class="mono" style="border:1px solid var(--line);padding:6px 10px;border-radius:99px;font-size:14px">{ic('timer',15)} 63:12</span></div>
<main style="padding:16px 20px"><div style="display:flex;justify-content:space-between;font-size:14px;margin-bottom:12px"><b style="font-weight:600">63 respondidas · 4 marcadas</b><span class="subtle">37 sin responder</span></div>
<div style="display:grid;grid-template-columns:repeat(10,1fr);gap:4px">{cells}</div>
<div style="display:flex;gap:14px;flex-wrap:wrap;font-size:12px;margin:14px 0 6px" class="subtle"><span>■ respondida</span><span><span style="color:var(--gold)">■</span> marcada</span><span>□ sin responder</span></div>
<p class="subtle" style="font-size:12px;margin:0 0 14px">Bloques: Legislación 30 · Museología 30 · Patrimonio 40<br>+ 10 preguntas de reserva · sin pausa · +1 / 0 / −1/3</p>
<div style="display:flex;gap:10px"><a class="btn btn-ghost" style="flex:1">Volver a la 64</a><a class="btn btn-primary" style="flex:1">Entregar</a></div></main>''')
if __name__=='__main__':
  for k,v in S.items(): open(f'screens/{k}.html','w').write(v)
  print(list(S))
