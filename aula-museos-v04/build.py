# Genera las pantallas y tableros de Aula Museos v0.4 (prototipo de diseño estático).
import pathlib
H = pathlib.Path(__file__).parent
SYMS = (H/'icons-symbols.txt').read_text() + (
 '<symbol id="i-skip" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 5l8 7-8 7M15 5v14"/></symbol>'
 '<symbol id="i-grid" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="4" y="4" width="6" height="6" rx="1.5"/><rect x="14" y="4" width="6" height="6" rx="1.5"/><rect x="4" y="14" width="6" height="6" rx="1.5"/><rect x="14" y="14" width="6" height="6" rx="1.5"/></symbol>'
 '<symbol id="i-flagf" viewBox="0 0 24 24" fill="currentColor" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><path d="M5 21V4" fill="none"/><path d="M5 4h11l-2 4 2 4H5z"/></symbol>'
 '<symbol id="i-rest" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M20 14.5A8 8 0 1 1 9.5 4a6.5 6.5 0 0 0 10.5 10.5z"/></symbol>'
 '<symbol id="i-repeat" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M4 12a8 8 0 0 1 14-5.3L20 9M20 4v5h-5M20 12a8 8 0 0 1-14 5.3L4 15M4 20v-5h5"/></symbol>')
def ic(n, cls='i'): return f'<svg class="{cls}"><use href="#{n}"/></svg>'
LOGO = '<svg viewBox="0 0 38 40" aria-hidden="true"><g transform="translate(1,1)" fill="none" stroke-linecap="round"><path d="M4 34V16a14 14 0 0 1 28 0v18" stroke="currentColor" stroke-width="3.2"/><path d="M11 34V18a7 7 0 0 1 14 0v16" stroke="currentColor" stroke-width="2.2"/><path d="M1 36.5h34" stroke="#C0643F" stroke-width="3"/></g></svg>'
LOGO_W = LOGO.replace('currentColor', '#F6F1E8')
STATUS = '<div class="status"><span>9:41</span><i>●●● ▮</i></div>'
DEMO = '<span class="chip demo">Pregunta de ejemplo</span>'

S = {}
# ---------- 1 · Simulacro: reglas ----------
S[1] = ('Simulacro · reglas', 'Formato real (BOE-A-2025-26893): 100 + 10 de reserva repartidas 3/3/4, 100 min, bloques 30/30/40, +1 · 0 · −1/3, escala 0–30 con 15 como nota de corte orientativa. Cuenta día de racha, no da XP.', f'''
<div class="topbar"><span class="iconbtn">{ic('i-back')}</span><h2>Simulacro</h2><span class="iconbtn">{ic('i-info')}</span></div>
<div class="hero"><span class="label">Formato del examen real</span><h1 style="margin-top:6px">Simulacro completo</h1>
<p class="lead">100 preguntas + 10 de reserva · 100 minutos · sin correcciones hasta entregar.</p></div>

<div class="card tight" style="margin-top:12px"><div class="label" style="margin-bottom:8px">Puntuación</div>
 <div class="scoring"><div class="sc ok"><b>+1</b>acierto</div><div class="sc bl"><b>0</b>en blanco</div><div class="sc er"><b>−1/3</b>error</div></div>
 <div class="formula" style="margin-top:8px">Nota = (aciertos − errores ÷ 3) × 30 ÷ 100<br><span class="small muted">15 / 30 · nota de corte orientativa (la real la fija el tribunal)</span></div>
</div>
<div class="card tight" style="margin-top:10px"><div class="row between" style="margin-bottom:8px"><span class="label">Bloques · 79 temas</span><span class="xs muted">BOE-A-2025-26893 · turno libre</span></div>
 <div class="blocks">
  <div class="blk"><span class="n">I</span><span class="t">Legislación<small>Temas 1–16 · P. 1–30 · reserva 101–103</small></span><span class="c">30+3</span></div>
  <div class="blk"><span class="n">II</span><span class="t">Museología<small>Temas 17–35 · P. 31–60 · reserva 104–106</small></span><span class="c">30+3</span></div>
  <div class="blk"><span class="n">III</span><span class="t">Patrimonio artístico, arqueológico y antropológico<small>Temas 36–79 · P. 61–100 · reserva 107–110</small></span><span class="c">40+4</span></div>
 </div></div>
<div class="foot"><div class="infoline">{ic('i-flame')}Cuenta como día de racha · el simulacro no suma XP</div><span class="btn btn-primary">{ic('i-play')} Empezar simulacro</span>
<p class="disc">Nota orientativa, no oficial. El cronómetro no se pausa. La reserva (101–110) solo cuenta si se anula alguna.</p></div>''')

# ---------- 2 · Pregunta en curso ----------
S[2] = ('Pregunta en curso', 'Cronómetro, número, marcar y saltar siempre visibles. Sin feedback hasta entregar.', f'''
<div class="exambar"><span class="iconbtn">{ic('i-x')}</span><span class="timer">{ic('i-clock')}58:24</span><span class="spacer"></span>
<span class="chip ex">Bloque I</span><span class="iconbtn">{ic('i-grid')}</span></div>
<div class="row"><div class="progress"><i style="width:23%"></i></div><span class="xs muted tab">23/100</span></div>
<div class="qmeta"><span class="qnum">Pregunta 23</span><span>Respondidas 19 · en blanco 3 · marcadas 2</span></div>
<div class="row" style="margin-top:8px">{DEMO}</div>
<p class="q">Según la Ley 16/1985, del Patrimonio Histórico Español, ¿cómo se declaran de forma individualizada los Bienes de Interés Cultural?</p>
<div class="opts">
 <div class="opt"><span class="k">a</span>Por orden del Ministerio de Cultura</div>
 <div class="opt sel"><span class="k">b</span>Mediante real decreto</div>
 <div class="opt"><span class="k">c</span>Por resolución de la comunidad autónoma</div>
 <div class="opt"><span class="k">d</span>Mediante ley orgánica</div>
</div>
<p class="note">Puedes cambiar la respuesta hasta entregar · acierto +1 · blanco 0 · error −1/3</p>
<div class="foot"><div class="btns"><span class="btn btn-ghost">{ic('i-flag')} Marcar</span><span class="btn btn-ghost">{ic('i-skip')} Saltar</span></div>
<div class="btns"><span class="btn btn-ghost" style="flex:.45">{ic('i-back')}</span><span class="btn btn-primary">Siguiente</span></div></div>''')

# ---------- 3 · Rejilla + confirmación ----------
def grid():
    blanks = {7,12,23-0}; blanks = {12,27,33,41,58,66,72,88,95}
    flags = {14,23,47,81}
    out=[]
    def cell(n, extra=''):
        c=[]
        if n in blanks: c.append('b')
        if n in flags: c.append('f')
        if n==23: c.append('cur')
        return f'<span class="{" ".join(c)}{extra}">{n}</span>'
    secs=[('I · Legislación','temas 1–16 · 1–30',range(1,31)),('II · Museología','temas 17–35 · 31–60',range(31,61)),('III · Patrimonio','temas 36–79 · 61–100',range(61,101))]
    for nm,rg,r in secs:
        out.append(f'<div class="gsep"><b>{nm}</b><span>{rg}</span></div><div class="qgrid">'+''.join(cell(n) for n in r)+'</div>')
    res=''.join(f'<span class="r{" a" if n<=104 else ""}">{n}</span>' for n in range(101,111))
    out.append(f'<div class="gsep"><b>Reserva</b><span>I 101–103 · II 104–106 · III 107–110</span></div><div class="qgrid">{res}</div>')
    return ''.join(out)
S[3] = ('Rejilla de navegación + entregar', 'Saltar a cualquier número; reserva 101–110 siempre visible. Entrega anticipada: una sola confirmación con resumen, sin pausa.', f'''
<div class="exambar"><span class="iconbtn">{ic('i-x')}</span><span class="timer">{ic('i-clock')}41:12</span><span class="spacer"></span><span class="serif" style="font-size:17px;color:var(--ink-900)">Preguntas</span></div>
<div class="legend"><span><i></i>Respondida 87</span><span><i class="b"></i>En blanco 9</span><span><i class="f"></i>Marcada 4</span><span><i class="r"></i>Reserva</span></div>
{grid()}
<div class="scrim"></div>
<div class="sheet"><div class="grab"></div>
<h3>¿Entregar ahora?</h3>
<p class="small muted" style="margin-top:4px">Quedan 41:12 y el cronómetro sigue corriendo. Tras entregar no podrás cambiar respuestas.</p>
<div class="sumrow three"><div><b>87</b>respondidas</div><div class="bl"><b>9</b>en blanco · 0 pts</div><div class="fl"><b>4</b>marcadas</div></div>
<div class="warnbox">Marcadas: 14, 23, 47 y 81.</div>
<div class="btns" style="margin-top:12px"><span class="btn btn-ghost">Seguir</span><span class="btn btn-primary">Entregar</span></div>
</div>''')

# ---------- 4 · Resultado ----------
# ejemplo: 68 aciertos, 21 errores, 11 en blanco → neta 61,00 → 18,30/30
S[4] = ('Resultado', 'Nota 0–30 frente a 15 (nota de corte orientativa), fórmula visible, desglose por los 3 bloques. Racha +1, sin XP.', f'''
<div class="topbar"><span class="iconbtn">{ic('i-x')}</span><h2>Resultado</h2><span class="chip demo">Datos de ejemplo</span></div>
<div class="card"><div class="scorebox">
 <div class="ring" style="background:conic-gradient(var(--ink-800) 0 61%, var(--ink-100) 61% 100%)"><div><div><b>18,30</b><small>de 30</small></div></div></div>
 <div><span class="chip ok">{ic('i-check')} Por encima de 15</span><p class="cut" style="margin-top:6px">15 = nota de corte orientativa</p><p class="xs muted" style="margin-top:4px">La nota de corte real la fija el tribunal. Tiempo: 86:40 de 100:00.</p></div>
</div>
<div class="thr"><i style="width:61%"></i><em style="left:50%"></em></div><div class="thrlbl"><span>0</span><span>30</span></div>
</div>
<div class="res3" style="margin-top:10px">
 <div class="ok"><b>68</b><span>aciertos</span><small>+68,00</small></div>
 <div class="er"><b>21</b><span>errores</span><small>−7,00</small></div>
 <div class="bl"><b>11</b><span>en blanco</span><small>0,00</small></div>
</div>
<div class="formula" style="margin-top:8px">68 − 21 ÷ 3 = 61,00 → 61,00 × 30 ÷ 100 = <b>18,30</b></div>
<div class="card tight" style="margin-top:8px"><div class="label" style="margin-bottom:4px">Por bloques · neta</div>
 <div class="bk"><div class="row"><span class="nm">I · Legislación</span><span class="pts">20,00 / 30</span></div><div class="split"><i class="o" style="width:73.3%"></i><i class="e" style="width:20%"></i><i class="z" style="width:6.7%"></i></div><small>22 aciertos · 6 errores · 2 en blanco</small></div>
 <div class="bk"><div class="row"><span class="nm">II · Museología</span><span class="pts">16,67 / 30</span><span class="chip err" style="font-size:10.5px;padding:2px 8px">Más resta</span></div><div class="split"><i class="o" style="width:63.3%"></i><i class="e" style="width:23.3%"></i><i class="z" style="width:13.3%"></i></div><small>19 aciertos · 7 errores · 4 en blanco</small></div>
 <div class="bk"><div class="row"><span class="nm">III · Patrimonio art., arq. y antrop.</span><span class="pts">24,33 / 40</span></div><div class="split"><i class="o" style="width:67.5%"></i><i class="e" style="width:20%"></i><i class="z" style="width:12.5%"></i></div><small>27 aciertos · 8 errores · 5 en blanco</small></div>
</div>
<div class="foot"><div class="infoline">{ic('i-flame')}Cuenta como día de racha · el simulacro no suma XP</div><div class="btns"><span class="btn btn-ghost">Nuevo simulacro</span><span class="btn btn-primary">Revisar errores</span></div></div>''')

# ---------- 5 · Revisión ----------
S[5] = ('Revisión por bloque y tema', 'Filtros por bloque, temas que más restan, explicación del error con fuente y «Practicar errores».', f'''
<div class="topbar"><span class="iconbtn">{ic('i-back')}</span><h2>Revisión</h2><span class="chip err">21 errores</span></div>
<div class="tabs"><span class="chip">Legislación 6</span><span class="chip on">Museología 7</span><span class="chip">Patrimonio 8</span><span class="chip blank">Blanco 11</span></div>
<div class="topic" style="margin-top:10px"><span class="t"><b>Museos de titularidad estatal</b><small>Museología · temas 17–35 · el que más resta</small></span><span class="e">4 err.</span></div>
<div class="card tight" style="margin-top:8px">
 <div class="row between"><span class="qnum">Pregunta 38</span><div class="row" style="gap:6px">{DEMO}<span class="chip err">−1/3</span></div></div>
 <p class="q" style="font-size:16px;margin:6px 0 8px">Según el art. 59.3 de la Ley 16/1985, ¿qué función <u>no</u> figura en la definición de museo?</p>
 <div class="opts" style="gap:6px">
  <div class="opt wrong" style="padding:9px 12px;font-size:13.5px"><span class="k">b</span>Investigan<span class="tag">Tu respuesta</span></div>
  <div class="opt right" style="padding:9px 12px;font-size:13.5px"><span class="k">c</span>Comercializan<span class="tag">Correcta</span></div>
 </div>
 <div class="aibox" style="margin-top:10px"><span class="badge-ai">{ic('i-ai')}Contenido generado por IA</span>
 <p>El art. 59.3 define el museo como institución que adquiere, conserva, investiga, comunica y exhibe colecciones. «Comercializar» no figura.</p>
 <div class="cite">{ic('i-doc')}<span><b>Ley 16/1985, de 25 de junio · art. 59.3</b><small>BOE-A-1985-12534 · boe.es</small></span></div></div>
</div>
<div class="nosrc" style="margin-top:8px"><span class="badge-nosrc">Sin fuente</span> <span style="margin-left:4px">P. 52: sin fuente suficiente para explicarla. Revísala en el temario oficial.</span></div>
<div class="foot"><div class="btns"><span class="btn btn-ghost" style="flex:.6">Siguiente</span><span class="btn btn-terra">{ic('i-repeat')} Practicar errores</span></div></div>''')

# ---------- 6 · Inicio ----------
WEEK = ''.join(f'<div class="{c}"><i>{ic("i-flame") if c=="d" else (ic("i-rest") if c=="rest" else "")}</i>{d}</div>' for d,c in zip('LMXJVSD',['d','d','rest','d','d','t','']))
S[6] = ('Inicio · racha y XP', 'Racha de días con 1 descanso semanal automático (sin vidas ni ligas), XP diario frente a la meta elegida y un único siguiente paso.', f'''
<div class="topbar"><span class="logo">{LOGO}<b>Aula Museos</b></span><div class="row" style="gap:6px"><span class="chip streak">{ic('i-flame')}12</span><span class="chip xp">{ic('i-star')}30 XP</span></div></div>
<h1 style="font-size:25px">Buenas tardes, Lucía</h1><p class="lead" style="margin-top:4px">Hoy toca repasar el Bloque II: unos 8 minutos.</p>
<div class="card" style="margin-top:14px"><div class="streakcard"><span class="flame">{ic('i-flame')}</span>
<div><div class="serif" style="font-size:22px">12 días seguidos</div><p class="small muted">Haz la lección o un simulacro para llegar a 13.</p></div></div>
<div class="week">{WEEK}</div>
<div class="restnote">{ic('i-rest')}<span>Descanso semanal automático: usado el miércoles. Tu racha se mantuvo.</span></div></div>
<div class="card tight" style="margin-top:10px"><div class="row between"><span class="label">XP de hoy · meta Regular</span><span class="small tab"><b>30</b> / 50 XP</span></div>
<div class="xpbar" style="margin-top:8px"><div class="progress gold"><i style="width:60%"></i></div><span class="xs muted">Meta diaria</span></div></div>
<div class="lesson" style="margin-top:12px"><span class="label">Lección del día</span><h3>Museos de titularidad estatal</h3>
<div class="meta"><span>{ic('i-clock')}8 min</span><span>{ic('i-book')}6 preguntas</span><span>{ic('i-star')}+20 XP</span></div>
<span class="btn">{ic('i-play')} Empezar lección</span></div>
<div class="mini" style="margin-top:10px"><span class="ic">{ic('i-repeat')}</span><span class="t"><b>Repaso pendiente</b><small>5 preguntas falladas ayer · Bloque II</small></span>{ic('i-back','i" style="transform:rotate(180deg);color:var(--subtle)')}</div>
<div class="spacer"></div>''', True)

# ---------- 7 · Pregunta de lección ----------
S[7] = ('Lección · pregunta', 'Lección corta con barra de progreso; explicación inmediata tras responder, con insignia IA y fuente.', f'''
<div class="exambar"><span class="iconbtn">{ic('i-x')}</span><div class="progress"><i style="width:50%"></i></div><span class="xs muted tab">3/6</span></div>
<div class="row" style="margin-top:4px"><span class="chip">Tema de ejemplo · Museos estatales</span>{DEMO}</div>
<p class="q">¿Qué norma aprueba el Reglamento de Museos de Titularidad Estatal y del Sistema Español de Museos?</p>
<div class="opts">
 <div class="opt right"><span class="k">a</span>Real Decreto 620/1987, de 10 de abril<span class="tag">{ic('i-check')}</span></div>
 <div class="opt dim"><span class="k">b</span>Ley 16/1985, de 25 de junio</div>
 <div class="opt dim"><span class="k">c</span>Ley 10/2007, de 22 de junio</div>
</div>
<div class="fb ok"><div class="row between"><h3>Correcto</h3><span class="chip xp">{ic('i-star')}+3 XP</span></div>
<div class="aibox" style="margin-top:10px"><span class="badge-ai">{ic('i-ai')}Contenido generado por IA</span>
<p>El Real Decreto 620/1987 aprueba ese reglamento. La Ley 16/1985 es la norma general del Patrimonio Histórico Español y la Ley 10/2007 regula la lectura, el libro y las bibliotecas.</p>
<div class="cite">{ic('i-doc')}<span><b>Real Decreto 620/1987, de 10 de abril</b><small>Reglamento de Museos de Titularidad Estatal · boe.es</small></span></div></div></div>
<div class="foot"><span class="btn btn-primary">Continuar</span></div>''')

# ---------- 8 · Lección completada ----------
S[8] = ('Lección completada', 'XP ganado, racha +1 y próximo repaso espaciado. Tono sereno, sin confeti ni mascotas.', f'''
<div class="topbar"><span class="iconbtn">{ic('i-x')}</span><span></span><span class="chip streak">{ic('i-flame')}13</span></div>
<div class="done-hero"><div class="seal">{LOGO_W}</div><h1 style="font-size:26px">Lección completada</h1>
<p class="lead">5 de 6 correctas · Museos de titularidad estatal</p></div>
<div class="gain" style="margin-top:12px"><div class="x"><b>+20 XP</b><span>Meta diaria 50/50</span></div><div class="s"><b>13 días</b><span>Racha +1</span></div></div>
<div class="card tight" style="margin-top:12px"><div class="label" style="margin-bottom:4px">Próximos repasos · repetición espaciada</div>
<div class="rep"><span class="when">Mañana</span><span class="t"><b>1 pregunta fallada</b><small>Funciones de los museos (art. 59.3 Ley 16/1985)</small></span></div>
<div class="rep"><span class="when">En 3 días</span><span class="t"><b>2 preguntas dudosas</b><small>Respondidas tras más de 30 s</small></span></div>
<div class="rep"><span class="when">En 7 días</span><span class="t"><b>3 preguntas acertadas</b><small>Repaso de consolidación</small></span></div>
</div>
<p class="small muted" style="margin-top:10px;text-align:center">Descanso semanal ya usado esta semana · se renueva el lunes</p>
<div class="foot"><span class="btn btn-primary">Volver al inicio</span><span class="btn-text" style="text-align:center">Repasar el error ahora</span></div>''')

# ---------- 9 · Onboarding: meta diaria ----------
S[9] = ('Onboarding · meta diaria', 'Tres niveles de meta de XP; se puede cambiar en Ajustes. Pie con aviso legal, privacidad y no afiliación.', f'''
<div class="exambar"><span class="iconbtn">{ic('i-back')}</span><div class="progress"><i style="width:75%"></i></div><span class="xs muted tab">3/4</span></div>
<span class="label" style="margin-top:6px">Tu ritmo</span>
<h1 style="margin-top:6px;font-size:26px">¿Cuánto quieres estudiar cada día?</h1>
<p class="lead">Elige una meta diaria de XP. Puedes cambiarla cuando quieras en Ajustes.</p>
<div class="stack-s" style="margin-top:16px">
 <div class="goal"><span class="rad"></span><span class="t"><b>Ligera</b><small>Unos 5 minutos · 1 lección corta</small></span><span class="xpv">30 XP</span></div>
 <div class="goal sel"><span class="rad"></span><span class="t"><b>Regular</b><small>Unos 10 minutos · lección + repaso</small></span><span class="xpv">50 XP</span></div>
 <div class="goal"><span class="rad"></span><span class="t"><b>Intensa</b><small>Unos 20 minutos · varias lecciones</small></span><span class="xpv">80 XP</span></div>
</div>
<div class="card tight" style="margin-top:14px"><div class="row" style="align-items:flex-start">{ic('i-rest')}<p class="small"><b>Racha de días.</b> Cuenta cualquier día con lección o simulacro. Tienes 1 día de descanso por semana, automático. El simulacro no suma XP.</p></div></div>
<div class="foot"><span class="btn btn-primary">Continuar</span><p class="legal"><a>Aviso legal</a> · <a>Privacidad</a><br>Aula Museos es una herramienta no afiliada al Ministerio de Cultura.</p></div>''')

def phone(n):
    t, cap, body, *tab = S[n]
    tb = ''
    if tab:
        tb = ('<div class="tabbar">' + ''.join(f'<div class="{"on" if i==0 else ""}"><span class="ico">{ic(x)}</span>{l}</div>' for i,(x,l) in enumerate([('i-home','Inicio'),('i-book','Estudiar'),('i-clock','Simulacro'),('i-chart','Progreso')])) + '</div>')
    return f'<div class="phone" data-vertical="museos">{STATUS}<div class="scr">{body}</div>{tb}</div>'

HEAD = '''<!DOCTYPE html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{t}</title><link rel="stylesheet" href="styles.css"></head>'''
SPR = f'<svg width="0" height="0" style="position:absolute">{SYMS}</svg>'
for n in S:
    (H/f'screen-{n:02d}.html').write_text(HEAD.format(t=f'Aula Museos v0.4 · {n:02d} {S[n][0]}') + f'<body style="background:var(--paper)">{SPR}{phone(n)}</body></html>')

def board(fname, title, sub, nums):
    frames = ''.join(f'<div class="frame"><div class="cap"><b>{n:02d} · {S[n][0]}</b>{S[n][1]}</div>{phone(n)}</div>' for n in nums)
    (H/fname).write_text(HEAD.format(t=title) + f'''<body class="boardbody">{SPR}
<div class="bhead"><div><span class="label">Aula Museos · v0.4 · prototipo de diseño</span><h1 style="margin-top:6px">{title}</h1><p>{sub}</p></div>
<div class="meta">Estilo Atrio · data-vertical="museos"<br>Source Serif 4 + Inter · móvil 390 px<br>Contenido de ejemplo · no es código de producción</div></div>
<div class="board">{frames}</div>
<div class="bfoot">Preguntas, temas mostrados y puntuaciones son de ejemplo; bloques según BOE-A-2025-26893 (turno libre, 79 temas: 1–16, 17–35, 36–79). Explicaciones de IA siempre con la etiqueta «Contenido generado por IA» y fuente; «Sin fuente» cuando no la hay. Normas citadas: Ley 16/1985, de 25 de junio, del Patrimonio Histórico Español (BOE-A-1985-12534); Real Decreto 620/1987, de 10 de abril. Escritorio: ver desktop-simulacro.html (pregunta + rejilla fija). Aviso legal · Privacidad · Aula Museos no está afiliada al Ministerio de Cultura.</div>
</body></html>''')
board('board-simulacro.html','Simulacro · formato real','100 preguntas + 10 de reserva · 100 minutos · bloques 30/30/40 · acierto +1, blanco 0, error −1/3 · nota 0–30 con 15 como nota de corte orientativa · navegación por números, marcar y saltar · revisión por bloques y temas.',[1,2,3,4,5])
board('board-leccion.html','Lección diaria con racha','Racha de días y XP diario frente a la meta (oro solo para XP; teja para la racha, como en el concepto v0.3) · lección corta con explicación inmediata · cierre con XP, racha +1 y repaso espaciado. Sin vidas, sin ligas, sin mascotas.',[9,6,7,8])

def dgrid():
    blanks={12,27,33,41,58,66,72,88,95}; flags={14,23,47,81}
    def cell(n):
        c=(['b'] if n in blanks else [])+(['f'] if n in flags else [])+(['cur'] if n==23 else [])
        return f'<span class="{" ".join(c)}">{n}</span>'
    o=''
    for nm,rg,r in [('I · Legislación','temas 1–16',range(1,31)),('II · Museología','temas 17–35',range(31,61)),('III · Patrimonio','temas 36–79',range(61,101))]:
        o+=f'<div class="gsep"><b>{nm}</b><span>{rg}</span></div><div class="qgrid">'+''.join(cell(n) for n in r)+'</div>'
    o+='<div class="gsep"><b>Reserva</b><span>I 101–103 · II 104–106 · III 107–110</span></div><div class="qgrid">'+''.join(f'<span class="r{" a" if n<=104 else ""}">{n}</span>' for n in range(101,111))+'</div>'
    return o
DESK = f"""<div class="desk" data-vertical="museos">
<div class="dhead"><span class="logo">{LOGO}<b>Aula Museos</b></span><span class="chip ex" style="margin-left:12px">Simulacro · formato real</span><span class="spacer"></span>
<span class="small muted">Respondidas 19 · en blanco 3 · marcadas 2</span><span class="timer">{ic('i-clock')}58:24</span><span class="btn btn-ghost" style="width:auto;padding:9px 16px;font-size:14px">Entregar</span></div>
<div class="dmain">
 <div class="dq">
  <div class="row between"><div class="row"><span class="qnum" style="font-size:19px">Pregunta 23</span><span class="chip">Bloque I · Legislación</span>{DEMO}</div>
  <div class="row"><span class="btn btn-ghost" style="width:auto;padding:9px 14px;font-size:14px">{ic('i-flag')} Marcar <kbd>M</kbd></span><span class="btn btn-ghost" style="width:auto;padding:9px 14px;font-size:14px">{ic('i-skip')} Saltar <kbd>S</kbd></span></div></div>
  <div class="row" style="margin-top:14px"><div class="progress"><i style="width:23%"></i></div><span class="xs muted tab">23/100</span></div>
  <p class="q">Según la Ley 16/1985, del Patrimonio Histórico Español, ¿cómo se declaran de forma individualizada los Bienes de Interés Cultural?</p>
  <div class="opts">
   <div class="opt"><span class="k">a</span>Por orden del Ministerio de Cultura</div>
   <div class="opt sel"><span class="k">b</span>Mediante real decreto</div>
   <div class="opt"><span class="k">c</span>Por resolución de la comunidad autónoma</div>
   <div class="opt"><span class="k">d</span>Mediante ley orgánica</div>
  </div>
  <div class="spacer"></div>
  <div class="row between" style="max-width:780px;width:100%"><span class="xs muted">Teclado: <kbd>A</kbd>–<kbd>D</kbd> responder · <kbd>←</kbd> <kbd>→</kbd> navegar · sin corrección hasta entregar · +1 · 0 · −1/3</span>
  <div class="row"><span class="btn btn-ghost" style="width:auto;padding:12px 18px">{ic('i-back')} Anterior</span><span class="btn btn-primary" style="width:auto;padding:12px 26px">Siguiente</span></div></div>
 </div>
 <aside class="dside">
  <div class="row between"><span class="serif" style="font-size:19px">Preguntas</span><span class="xs muted">Clic para saltar</span></div>
  <div class="legend" style="margin-top:8px"><span><i></i>Respondida</span><span><i class="b"></i>En blanco</span><span><i class="f"></i>Marcada</span><span><i class="r"></i>Reserva</span></div>
  {dgrid()}
  <div class="spacer"></div>
  <div class="infoline" style="margin-top:12px">{ic('i-flame')}Cuenta como día de racha · no suma XP · el cronómetro no se pausa</div>
 </aside>
</div>
<div class="dfoot"><a>Aviso legal</a><a>Privacidad</a><span>Aula Museos no está afiliada al Ministerio de Cultura · herramienta de estudio no oficial · preguntas de ejemplo</span></div>
</div>"""
(H/'desktop-simulacro.html').write_text(HEAD.format(t='Aula Museos v0.4 · escritorio · simulacro') + f'<body>{SPR}{DESK}</body></html>')

idx = ''.join(f'<li><a href="screen-{n:02d}.html">{n:02d} · {S[n][0]}</a></li>' for n in S)
(H/'index.html').write_text(HEAD.format(t='Aula Museos v0.4') + f'<body class="boardbody"><h1>Aula Museos · v0.4</h1><p class="lead">Prototipo de diseño: simulacro + lección diaria (estilo Atrio).</p><ul style="margin:16px 0 0 20px;line-height:1.9"><li><a href="board-simulacro.html">Tablero · Simulacro</a></li><li><a href="board-leccion.html">Tablero · Lección diaria</a></li><li><a href="desktop-simulacro.html">Escritorio · simulacro</a></li>{idx}</ul></body></html>')
print('built', len(S))
