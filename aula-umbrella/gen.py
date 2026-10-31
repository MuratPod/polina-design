# Generator: Aula umbrella — conceptos de dirección v1
VERT = [  # name, sector line, dir-specific colours handled per direction
 ("Museos","Ayudantes de Museos del Estado"),
 ("Justicia","Tramitación · Auxilio · Gestión"),
 ("Policía","Escala Básica · Policía Nacional"),
 ("Administración","Cuerpos generales AGE · C1/C2"),
]
SERIF="'Source Serif 4',Georgia,serif"; SANS="Inter,Arial,sans-serif"; PUB="'Public Sans',Inter,Arial,sans-serif"

# ---------------- A · CÁTEDRA ----------------
A = dict(ink="#231C17", paper="#F5EFE3", vellum="#EAE0CC", accent="#6B2234", gold="#A9843A", line="#DCCFB6",
  vc={"Museos":("#15393F","#A84B2A"),"Justicia":("#14304D","#B07A2A"),"Policía":("#1F3550","#5B7FA8"),"Administración":("#2C4A3B","#8C7A3A")})
def a_seal(c="#231C17", ring=None, s=1.0, bg="none"):
    ring = ring or c
    return f'''<g transform="scale({s})"><circle cx="32" cy="32" r="30" fill="{bg}" stroke="{ring}" stroke-width="2.4"/><circle cx="32" cy="32" r="25.5" fill="none" stroke="{ring}" stroke-width=".9"/>
<text x="32" y="44" text-anchor="middle" style="font-family:{SERIF};font-weight:600;font-size:33px" fill="{c}">A</text><path d="M18 49.5h28" stroke="{ring}" stroke-width="1.1"/></g>'''
def a_h(v=None, fg="#231C17", sub="#6B2234", ring=None, w=480):
    suf = f'<text x="226" y="47" style="font-family:{SERIF};font-style:italic;font-weight:500;font-size:34px" fill="{sub}">{v}</text><path d="M212 22v32" stroke="{fg}" stroke-width="1" opacity=".35"/>' if v else ''
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} 76" width="100%" role="img" aria-label="Aula {v or ''}"><g transform="translate(4,6)">{a_seal(fg, ring or sub)}</g>
<text x="84" y="48" style="font-family:{SERIF};font-weight:600;font-size:31px;letter-spacing:7px" fill="{fg}">AULA</text>{suf}</svg>'''
def a_stack(v, fg, sub, bg="none"):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 220 200" width="100%" role="img" aria-label="Aula {v}"><rect width="220" height="200" fill="{bg}"/><g transform="translate(78,14)">{a_seal(fg, sub)}</g>
<text x="110" y="122" text-anchor="middle" style="font-family:{SERIF};font-weight:600;font-size:26px;letter-spacing:6px" fill="{fg}">AULA</text><path d="M80 134h60" stroke="{sub}" stroke-width="1.2"/>
<text x="110" y="166" text-anchor="middle" style="font-family:{SERIF};font-style:italic;font-weight:500;font-size:28px" fill="{sub}">{v}</text></svg>'''

# ---------------- B · BOLETÍN ----------------
B = dict(ink="#0B2545", paper="#FFFFFF", grey="#F2F4F7", line="#D0D5DD", accent="#B3261E", text="#101828", muted="#475467",
  vc={"Museos":("#15393F","#C0643F"),"Justicia":("#0B2545","#B07A2A"),"Policía":("#13315C","#4F86C6"),"Administración":("#24443A","#9AA33C")})
def b_mark(bg="#0B2545", stripe="#B3261E", fg="#FFFFFF"):
    return f'''<rect x="0" y="0" width="56" height="56" rx="4" fill="{bg}"/><rect x="0" y="46" width="56" height="10" fill="{stripe}"/><rect x="0" y="44" width="56" height="2" fill="{bg}"/>
<path d="M14 40 L28 10 L42 40 M19.5 30h17" fill="none" stroke="{fg}" stroke-width="5" stroke-linejoin="miter" stroke-linecap="square"/>'''
def b_h(v=None, bg="#0B2545", stripe="#B3261E", tc="#0B2545", sc="#475467", w=440):
    suf = f'<path d="M150 14v40" stroke="{sc}" stroke-width="2"/><text x="164" y="46" style="font-family:{PUB};font-weight:500;font-size:30px" fill="{sc}">{v}</text>' if v else ''
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} 68" width="100%" role="img" aria-label="Aula {v or ''}"><g transform="translate(2,6)">{b_mark(bg, stripe)}</g>
<text x="72" y="46" style="font-family:{PUB};font-weight:800;font-size:32px;letter-spacing:-.5px" fill="{tc}">Aula</text>{suf}</svg>'''
def b_tile(v, bg, stripe):
    code = {"Museos":"MUS","Justicia":"JUS","Policía":"POL","Administración":"AGE"}[v]
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 220 200" width="100%" role="img" aria-label="Aula {v}"><rect width="220" height="200" rx="10" fill="{bg}"/><rect y="176" width="220" height="24" fill="{stripe}"/>
<g transform="translate(20,20) scale(.8)">{b_mark("#FFFFFF", stripe, bg)}</g><text x="20" y="118" style="font-family:{PUB};font-weight:800;font-size:30px" fill="#fff">Aula</text>
<text x="20" y="152" style="font-family:{PUB};font-weight:500;font-size:24px" fill="#fff" opacity=".85">{v}</text><text x="200" y="44" text-anchor="end" style="font-family:{PUB};font-weight:700;font-size:13px;letter-spacing:2px" fill="#fff" opacity=".7">{code}</text></svg>'''

# ---------------- C · ATRIO ----------------
C = dict(ink="#17242B", paper="#F6F1E8", surface="#FFFDF8", gold="#C49A45", line="#E3D9C8", muted="#56615F",
  vc={"Museos":("#15393F","#C0643F"),"Justicia":("#14304D","#B07A2A"),"Policía":("#1F2F45","#3F6FB0"),"Administración":("#24473B","#7E9A3A")})
def c_arch(c="#17242B", base="#C49A45", s=1.0):
    return f'''<g transform="scale({s})" fill="none" stroke-linecap="round"><path d="M4 34V16a14 14 0 0 1 28 0v18" stroke="{c}" stroke-width="3.2"/><path d="M11 34V18a7 7 0 0 1 14 0v16" stroke="{c}" stroke-width="2.2"/><path d="M1 36.5h34" stroke="{base}" stroke-width="3.2"/></g>'''
def c_h(v=None, c="#17242B", base="#C49A45", sc=None, w=440):
    sc = sc or c
    suf = f'<text x="158" y="50" style="font-family:{SANS};font-weight:500;font-size:30px;letter-spacing:-.3px" fill="{sc}">{v}</text>' if v else ''
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} 72" width="100%" role="img" aria-label="Aula {v or ''}"><g transform="translate(6,10) scale(1.35)">{c_arch(c, base)}</g>
<text x="66" y="50" style="font-family:{SERIF};font-weight:600;font-size:38px;letter-spacing:-.3px" fill="{c}">Aula</text>{suf}</svg>'''
def c_app(v, ink, acc, bg):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 220 200" width="100%" role="img" aria-label="Aula {v}"><rect width="220" height="200" fill="{bg}"/><g transform="translate(83,22) scale(1.5)">{c_arch(ink, acc)}</g>
<text x="110" y="126" text-anchor="middle" style="font-family:{SERIF};font-weight:600;font-size:32px" fill="{ink}">Aula</text><text x="110" y="160" text-anchor="middle" style="font-family:{SANS};font-weight:500;font-size:22px" fill="{acc}">{v}</text>
<text x="110" y="184" text-anchor="middle" style="font-family:{SANS};font-weight:600;font-size:8px;letter-spacing:1.6px" fill="{ink}" opacity=".6">{dict(VERT)[v].upper()}</text></svg>'''

def sw(hexv, name, role, dark=True):
    return f'<div class="sw"><div class="chip" style="background:{hexv}"></div><b>{name}</b><code>{hexv}</code><small>{role}</small></div>'
def icon(svgbody, bg, size=64, vb="0 0 64 64"):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" width="{size}" height="{size}"><rect width="64" height="64" rx="14" fill="{bg}"/>{svgbody}</svg>'

def section(key, num, title, sub, tagline, alttag, lead, pal, typo, voice, dos, donts, umbrella_html, vert_rows, system_html, pros, cons, ui_html, css_vars):
    return f'''<section id="{key}" class="dir" style="{css_vars}">
<header class="dir-h"><span class="num">{num}</span><div><h2>{title}</h2><p class="sub">{sub}</p></div></header>
<p class="lead">{lead}</p>
<div class="grid2">
 <div class="card hero">{umbrella_html}<p class="tag">«{tagline}»</p><p class="alt">Alternativa: «{alttag}»</p></div>
 <div class="card"><h3>1 · Nombre y logotipo</h3>{system_html}</div>
</div>
<div class="grid3">
 <div class="card"><h3>2 · Paleta</h3><div class="sws">{pal}</div></div>
 <div class="card"><h3>3 · Tipografía</h3>{typo}</div>
 <div class="card"><h3>4 · Voz</h3><p class="voice">{voice}</p><div class="dd"><div><h4>Sí</h4><ul>{''.join(f'<li>{d}</li>' for d in dos)}</ul></div><div><h4>No</h4><ul>{''.join(f'<li>{d}</li>' for d in donts)}</ul></div></div></div>
</div>
<div class="card"><h3>5 · Sistema de verticales</h3><div class="verts">{vert_rows}</div></div>
<div class="grid2">
 <div class="card"><h3>6 · En producto (prueba / examen)</h3>{ui_html}</div>
 <div class="card pc"><h3>7 · Pros y contras</h3><div class="dd"><div><h4>A favor</h4><ul>{''.join(f'<li>{p}</li>' for p in pros)}</ul></div><div><h4>En contra</h4><ul>{''.join(f'<li>{p}</li>' for p in cons)}</ul></div></div></div>
</div>
</section>'''

def ui(font_h, font_b, ink, acc, bg, surface, line, radius, ok="#2D6B4C", err="#9A3B28", ai="#4B3F8F", brand=""):
    return f'''<div class="ui" style="background:{bg};border-color:{line};font-family:{font_b}">
 <div class="ui-top" style="border-color:{line}">{brand}<span class="pill" style="border-color:{line};color:{ink}">Examen · 40 preguntas</span></div>
 <p class="ui-q" style="font-family:{font_h};color:{ink}">¿Qué norma regula el Patrimonio Histórico Español?</p>
 <div class="ui-opt" style="border-color:{ok};background:{surface};border-radius:{radius}"><b style="color:{ok}">✓</b> Ley 16/1985, de 25 de junio</div>
 <div class="ui-opt" style="border-color:{line};background:{surface};border-radius:{radius}">Real Decreto 620/1987</div>
 <div class="ui-score"><span style="color:{ok}">+1 acierto</span><span style="color:#6E7775">0 en blanco</span><span style="color:{err}">−1/3 error</span></div>
 <div class="ui-ai" style="border-color:{ai}33;background:{ai}0d;border-radius:{radius}"><small style="color:{ai}">CONTENIDO IA · con fuente</small><span>La Ley 16/1985 es la norma básica del Patrimonio Histórico Español.</span><a style="color:{ai}">BOE-A-1985-12666 · art. 1</a></div>
 <button style="background:{ink};border-radius:{radius};font-family:{font_b}">Siguiente pregunta</button>
</div>'''

# ===== Build A =====
A_pal = ''.join([sw(A['ink'],"Tinta","texto, logotipo"), sw(A['paper'],"Pergamino","fondo"), sw(A['vellum'],"Vitela","superficies"), sw(A['accent'],"Burdeos cátedra","acento paraguas"), sw(A['gold'],"Oro viejo","filetes, sello"), sw(A['line'],"Filete","bordes")])
A_typo = f'''<p class="tsample" style="font-family:{SERIF};font-weight:600;letter-spacing:5px;font-size:26px">AULA</p><p class="tsample" style="font-family:{SERIF};font-size:22px">Tema 7 · <i>La Ley 16/1985</i></p><p style="font-family:{SANS};font-size:14px;color:#555">Interfaz en Inter 14–16 px.</p>
<ul class="small"><li><b>Source Serif 4</b>: logotipo en versalitas espaciadas, titulares y enunciados</li><li><b>Inter</b>: UI, botones, números</li><li>Cursiva serif para el nombre de la vertical</li></ul>'''
A_rows = ''.join(f'<div class="vrow"><div class="lk">{a_h(v, A["ink"], A["vc"][v][1], A["vc"][v][1])}</div><div class="vk"><span style="background:{A["vc"][v][0]}"></span><span style="background:{A["vc"][v][1]}"></span><small>{s}</small></div></div>' for v,s in VERT)
A_sys = f'''<div class="lkbig">{a_h(None, A["ink"], A["accent"], A["accent"])}</div>
<div class="row3"><div class="mini" style="background:{A['paper']}">{a_stack("Museos", A['ink'], A['vc']['Museos'][1])}</div><div class="mini" style="background:{A['vc']['Justicia'][0]}">{a_stack("Justicia", "#F5EFE3", "#D9B56B")}</div>
<div class="mini icons">{icon(f'<g transform="translate(6,6) scale(.81)">{a_seal("#F5EFE3","#D9B56B")}</g>', A['accent'])}{icon(f'<g transform="translate(6,6) scale(.81)">{a_seal("#F5EFE3","#E6B39E")}</g>', A['vc']['Museos'][0])}{icon(f'<g transform="translate(6,6) scale(.81)">{a_seal("#F5EFE3","#D9B56B")}</g>', A['vc']['Justicia'][0])}<small>Iconos de app: el sello no cambia; cambia el campo de color.</small></div></div>
<p class="note"><b>Herencia:</b> sello «A» común a toda la línea; «AULA» en versalitas; la vertical va en cursiva serif con su color propio. El arco de Museos pasa a ser ilustración de su vertical, no su logotipo.</p>'''
A_html = section("catedra","A","Cátedra","Académico · serif · humanidades",
 "Rigor de cátedra para tu oposición.","Se aprueba estudiando como se enseña.",
 "Aula como institución académica: un sello tipográfico, versalitas y burdeos de universidad clásica. Hereda el calor de Museos (pergamino, oro) y lo eleva a «escuela» de toda la línea.",
 A_pal, A_typo,
 "Un catedrático que prepara: preciso, culto, sereno; siempre cita la norma.",
 ["Citar ley, artículo y BOE en cada explicación","Frases completas, registro formal, tuteo respetuoso","Nombrar el temario oficial por su número"],
 ["Emojis, exclamaciones, jerga de app","Prometer la plaza («¡apruebas seguro!»)","Ornamento: laureles, escudos, latinajos"],
 f'<div class="lkhero">{a_h(None, A["ink"], A["accent"], A["accent"])}</div>', A_rows, A_sys,
 ["Máxima credibilidad académica; diferencia frente a academias «low cost»","Continuidad natural con el brandbook de Museos (pergamino, serif)","Sello funciona muy bien en certificados, PDF, redes"],
 ["Puede sentirse antiguo para Policía o C2 administrativo","Versalitas espaciadas pierden legibilidad < 24 px","Museos debe cambiar su logotipo (arco → sello)"],
 ui(SERIF, SANS, A['ink'], A['accent'], A['paper'], "#FFFCF5", A['line'], "6px", brand=f'<span style="font-family:{SERIF};letter-spacing:3px;font-weight:600;color:{A["ink"]}">AULA <i style="letter-spacing:0;color:{A["vc"]["Museos"][1]}">Museos</i></span>'),
 f"--bg:{A['paper']};--ink:{A['ink']};--acc:{A['accent']};--card:#FFFCF5;--line:{A['line']}")

# ===== Build B =====
B_pal = ''.join([sw(B['ink'],"Azul Estado","paraguas, botones"), sw(B['paper'],"Blanco","fondo"), sw(B['grey'],"Gris boletín","superficies"), sw(B['line'],"Línea","bordes, tablas"), sw(B['accent'],"Rojo sello","franja paraguas, alertas"), sw(B['text'],"Texto","cuerpo")])
B_typo = f'''<p class="tsample" style="font-family:{PUB};font-weight:800;font-size:28px">Aula <span style="font-weight:500;color:#475467">| Justicia</span></p><p class="tsample" style="font-family:{SERIF};font-size:18px">Artículo 117.1 CE — La justicia emana del pueblo…</p>
<ul class="small"><li><b>Public Sans</b> (tipografía de administraciones públicas): logotipo, titulares, UI</li><li><b>Source Serif 4</b> solo para texto legal citado</li><li>Cifras tabulares; jerarquía por peso, no por color</li></ul>'''
B_rows = ''.join(f'<div class="vrow"><div class="lk">{b_h(v, B["vc"][v][0], B["vc"][v][1], B["vc"][v][0], B["muted"])}</div><div class="vk"><span style="background:{B["vc"][v][0]}"></span><span style="background:{B["vc"][v][1]}"></span><small>{s}</small></div></div>' for v,s in VERT)
B_sys = f'''<div class="lkbig">{b_h(None)}</div>
<div class="row3"><div class="mini">{b_tile("Museos", *B['vc']['Museos'])}</div><div class="mini">{b_tile("Justicia", *B['vc']['Justicia'])}</div>
<div class="mini icons">{icon(f'<g transform="translate(10,10) scale(.79)">{b_mark("#0B2545","#B3261E")}</g>', "#FFFFFF")}{icon(f'<g transform="translate(10,10) scale(.79)">{b_mark(*B["vc"]["Museos"])}</g>', "#FFFFFF")}{icon(f'<g transform="translate(10,10) scale(.79)">{b_mark(*B["vc"]["Justicia"])}</g>', "#FFFFFF")}<small>Iconos: bloque + franja; la franja lleva el color de la vertical (y un código MUS / JUS / POL / AGE).</small></div></div>
<p class="note"><b>Herencia:</b> bloque «A» + franja. «Aula» siempre en negrita; la vertical tras una barra vertical, peso medio. Justicia comparte el azul Estado casi idéntico — encaje directo.</p>'''
B_html = section("boletin","B","Boletín","Institucional · sans · claridad de examen de Estado",
 "Tu plaza, con método.","Temario oficial. Examen real. Sin rodeos.",
 "Aula como servicio público de preparación: claridad tipo BOE, azul de Estado, retícula estricta, señalética. Es la dirección más fría y escalable: funciona igual para Museos que para Policía o Hacienda.",
 B_pal, B_typo,
 "Un tribunal claro: directo, neutral, exacto; dice qué cuenta y cuánto puntúa.",
 ["Frases cortas, verbo primero («Revisa el tema 4»)","Datos exactos: plazas, convocatoria, penalización −1/3","Referencias normativas en formato BOE"],
 ["Calidez forzada o tono motivacional","Ilustraciones decorativas","Imitar escudos o logotipos oficiales (riesgo de confusión con la Administración)"],
 f'<div class="lkhero">{b_h(None)}</div>', B_rows, B_sys,
 ["La más escalable a 10+ cuerpos (código + franja)","Justicia ya encaja (azul marino + ámbar)","Legibilidad máxima en móvil y en tablas de resultados"],
 ["Riesgo de parecer «la web del ministerio» — poca emoción","Museos pierde su calidez (pergamino, serif)","Hay que vigilar no imitar símbolos oficiales"],
 ui(PUB, PUB, B['ink'], B['accent'], "#FFFFFF", B['grey'], B['line'], "4px", ok="#1E6B45", err="#B3261E", brand=f'<span style="font-family:{PUB};font-weight:800;color:{B["ink"]}">Aula <span style="font-weight:500;color:#475467">| Justicia</span></span>'),
 f"--bg:#FFFFFF;--ink:{B['ink']};--acc:{B['accent']};--card:#FFFFFF;--line:{B['line']}")

# ===== Build C =====
C_pal = ''.join([sw(C['ink'],"Tinta","paraguas, texto"), sw(C['paper'],"Papel","fondo"), sw(C['surface'],"Superficie","tarjetas"), sw(C['gold'],"Oro pátina","basamento paraguas"), sw(C['line'],"Línea","bordes"), sw("#4B3F8F","Violeta IA","solo Contenido IA")])
C_typo = f'''<p class="tsample" style="font-family:{SERIF};font-weight:600;font-size:30px">Aula <span style="font-family:{SANS};font-weight:500;font-size:24px;color:#14304D">Justicia</span></p><p class="tsample" style="font-family:{SERIF};font-size:18px">Pregunta 12 de 40</p>
<ul class="small"><li><b>Source Serif 4</b>: «Aula», titulares, enunciados (= Museos hoy)</li><li><b>Inter</b>: nombre de la vertical, UI, botones, puntuación</li><li>Serif = saber · Sans = herramienta. Mismo par que la app v0.1</li></ul>'''
C_rows = ''.join(f'<div class="vrow"><div class="lk">{c_h(v, C["vc"][v][0], C["vc"][v][1], C["vc"][v][0])}</div><div class="vk"><span style="background:{C["vc"][v][0]}"></span><span style="background:{C["vc"][v][1]}"></span><small>{s}</small></div></div>' for v,s in VERT)
C_sys = f'''<div class="lkbig">{c_h(None)}</div>
<div class="row3"><div class="mini">{c_app("Museos", C['vc']['Museos'][0], C['vc']['Museos'][1], "#F6F1E8")}</div><div class="mini">{c_app("Justicia", C['vc']['Justicia'][0], C['vc']['Justicia'][1], "#EEF2F7")}</div>
<div class="mini icons">{icon(f'<g transform="translate(14,12) scale(1)">{c_arch("#F6F1E8", C["gold"])}</g>', C['ink'])}{icon(f'<g transform="translate(14,12) scale(1)">{c_arch("#F6F1E8", "#E08A63")}</g>', C['vc']['Museos'][0])}{icon(f'<g transform="translate(14,12) scale(1)">{c_arch("#F6F1E8", "#D9A24E")}</g>', C['vc']['Justicia'][0])}<small>Iconos: el arco es común; cambian el fondo (tinta de la vertical) y el basamento (acento).</small></div></div>
<p class="note"><b>Herencia:</b> el arco de Museos asciende a símbolo de toda la línea. Cada vertical = su par de colores (tinta + acento en el basamento). Museos queda casi igual; Justicia conserva su azul marino + ámbar.</p>'''
C_html = section("atrio","C","Atrio","Híbrido · calidez de aula + rigor de examen",
 "Estudia como se examina.","Del temario a la plaza, cada día.",
 "El atrio es el espacio común que da acceso a cada sala: un arco (el aula) sobre un basamento (el método). Serif para el saber, sans para la herramienta. Cada vertical aporta su color sin romper la familia.",
 C_pal, C_typo,
 "Un buen preparador: sereno, exacto, cercano sin ser informal; examen sin pánico.",
 ["Explicar el porqué con fuente («según el art. 1 de la Ley 16/1985…»)","Tuteo respetuoso, frases cortas, progreso concreto","Reconocer el esfuerzo con datos, no con euforia"],
 ["Gamificación infantil (mascotas, confeti, «¡crack!»)","Respuestas IA sin cita o con certeza inventada","Mezclar los colores de dos verticales en una misma pantalla"],
 f'<div class="lkhero">{c_h(None)}</div>', C_rows, C_sys,
 ["Coste mínimo: Museos y la app v0.1 ya cumplen el 90 %","Justicia mantiene su azul + ámbar; Policía/AGE se añaden en minutos","Equilibrio serio/humano ideal para estudio diario"],
 ["Menos impactante que A o B por separado (más «tranquilo»)","El arco recuerda a museo — hay que explicarlo como «aula/atrio»","Exige disciplina de color por vertical"],
 ui(SERIF, SANS, C['vc']['Justicia'][0], C['vc']['Justicia'][1], "#EEF2F7", "#FFFFFF", "#DCE4EE", "12px", brand=f'<span style="font-family:{SERIF};font-weight:600;color:#14304D">Aula <span style="font-family:{SANS};font-weight:500">Justicia</span></span>'),
 f"--bg:{C['paper']};--ink:{C['ink']};--acc:{C['gold']};--card:{C['surface']};--line:{C['line']}")

CMP = f'''<table class="cmp"><thead><tr><th></th><th>A · Cátedra</th><th>B · Boletín</th><th>C · Atrio ★</th></tr></thead><tbody>
<tr><td>Idea</td><td>Escuela académica</td><td>Servicio público claro</td><td>Aula común + salas por cuerpo</td></tr>
<tr><td>Símbolo</td><td>Sello «A» tipográfico</td><td>Bloque «A» + franja de color</td><td>Arco + basamento (evoluciona Museos)</td></tr>
<tr><td>Tipos</td><td>Source Serif 4 (versalitas) + Inter</td><td>Public Sans (+ Serif para normas)</td><td>Source Serif 4 + Inter</td></tr>
<tr><td>Temperatura</td><td>Cálida, clásica</td><td>Fría, neutral</td><td>Templada</td></tr>
<tr><td>Museos</td><td>Cambia logotipo</td><td>Cambia casi todo</td><td>Casi sin cambios</td></tr>
<tr><td>Justicia</td><td>Encaja (azul + oro)</td><td>Encaja perfecto</td><td>Encaja (azul + ámbar)</td></tr>
<tr><td>Escala a 10+ cuerpos</td><td>Buena</td><td>Excelente</td><td>Muy buena</td></tr>
<tr><td>Esfuerzo hoy</td><td>Medio</td><td>Alto</td><td>Bajo</td></tr></tbody></table>'''

CSS = '''*{box-sizing:border-box}body{margin:0;font-family:Inter,system-ui,sans-serif;color:#1B2427;background:#F3F1EC;line-height:1.5}
.top{position:sticky;top:0;z-index:5;background:#17242Bee;backdrop-filter:blur(6px);color:#F6F1E8;display:flex;gap:18px;align-items:center;padding:10px 28px;flex-wrap:wrap}
.top b{font-family:'Source Serif 4',serif;font-size:18px;margin-right:auto}.top a{color:#F6F1E8;text-decoration:none;font-size:14px;padding:6px 12px;border:1px solid #ffffff33;border-radius:999px}.top a:hover{background:#ffffff1a}
.wrap{max-width:1180px;margin:0 auto;padding:28px}
.intro h1{font-family:'Source Serif 4',serif;font-size:44px;margin:.2em 0;letter-spacing:-.5px}.intro p{max-width:780px;color:#46524F}
.rec{background:#17242B;color:#F6F1E8;border-radius:16px;padding:18px 22px;margin:18px 0}.rec b{color:#E2C27D}
.cmp{width:100%;border-collapse:collapse;background:#fff;border-radius:12px;overflow:hidden;font-size:14px;margin:12px 0 30px}.cmp th,.cmp td{padding:9px 12px;border-bottom:1px solid #E6E1D6;text-align:left}.cmp th{background:#EFE8DB;font-family:'Source Serif 4',serif;font-size:16px}.cmp td:first-child{color:#6E7775;font-weight:600;width:170px}
.dir{background:var(--bg);border:1px solid var(--line);border-radius:22px;padding:30px;margin:34px 0;scroll-margin-top:70px}
.dir-h{display:flex;gap:16px;align-items:center}.num{width:52px;height:52px;border-radius:50%;background:var(--ink);color:#fff;display:grid;place-items:center;font:700 22px 'Source Serif 4',serif}
.dir h2{font-family:'Source Serif 4',serif;font-size:36px;margin:0;color:var(--ink)}.sub{margin:0;color:#6E7775;font-size:14px;text-transform:uppercase;letter-spacing:1.4px}
.lead{font-size:17px;max-width:860px;color:#33403D}
.card{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:18px 20px;margin-top:16px}.card h3{margin:0 0 12px;font-size:13px;letter-spacing:1.4px;text-transform:uppercase;color:var(--acc)}
.grid2{display:grid;grid-template-columns:1fr 1fr;gap:16px}.grid3{display:grid;grid-template-columns:1fr 1fr 1fr;gap:16px}
.hero{display:flex;flex-direction:column;justify-content:center}.lkhero{max-width:480px}.tag{font-family:'Source Serif 4',serif;font-size:26px;color:var(--ink);margin:18px 0 4px}.alt{color:#6E7775;margin:0;font-size:14px}
.lkbig{max-width:300px;margin-bottom:10px}.row3{display:grid;align-items:start;grid-template-columns:1fr 1fr 1.1fr;gap:10px}.mini{border:1px solid var(--line);border-radius:12px;overflow:hidden}
.icons{display:flex;flex-wrap:wrap;gap:8px;padding:10px;align-content:flex-start}.icons small{font-size:12px;color:#6E7775}
.note{font-size:13.5px;color:#46524F;margin:12px 0 0}
.sws{display:grid;grid-template-columns:1fr 1fr;gap:10px}.sw{font-size:12px;display:flex;flex-direction:column}.sw .chip{height:44px;border-radius:8px;border:1px solid #0000001a;margin-bottom:4px}.sw code{color:#56615F}.sw small{color:#6E7775}
.tsample{margin:.2em 0;color:var(--ink)}.small{font-size:13px;padding-left:18px;color:#46524F}
.voice{font-family:'Source Serif 4',serif;font-size:17px;font-style:italic;color:var(--ink);margin-top:0}
.dd{display:grid;grid-template-columns:1fr 1fr;gap:12px}.dd h4{margin:0 0 4px;font-size:13px}.dd ul{margin:0;padding-left:18px;font-size:13px;color:#46524F}.dd li{margin-bottom:4px}
.verts{display:grid;grid-template-columns:1fr 1fr;gap:10px 26px}.vrow{display:flex;align-items:center;gap:12px;border-bottom:1px dashed var(--line);padding:6px 0}.lk{flex:1;max-width:340px}.vk{display:flex;align-items:center;gap:4px;width:180px}.vk span{width:18px;height:18px;border-radius:5px;display:inline-block}.vk small{font-size:11px;color:#6E7775;margin-left:6px;line-height:1.2}
.ui{border:1px solid;border-radius:16px;padding:14px;font-size:14px}.ui-top{display:flex;justify-content:space-between;align-items:center;border-bottom:1px solid;padding-bottom:8px;margin-bottom:10px}.pill{border:1px solid;border-radius:999px;padding:2px 10px;font-size:12px}
.ui-q{font-size:18px;margin:6px 0 10px;font-weight:600}.ui-opt{border:1.5px solid;padding:9px 12px;margin-bottom:6px}.ui-score{display:flex;gap:14px;font-size:12px;font-weight:600;margin:8px 0}
.ui-ai{border:1px solid;padding:9px 12px;display:flex;flex-direction:column;gap:2px;margin-bottom:10px}.ui-ai small{font-size:10px;font-weight:700;letter-spacing:1.2px}.ui-ai a{font-size:12px;text-decoration:underline}
.ui button{width:100%;border:0;color:#fff;padding:12px;font-size:15px;font-weight:600}
.ru{background:#fff;border:1px solid #E6E1D6;border-radius:16px;padding:18px 22px}.foot{color:#6E7775;font-size:13px;text-align:center;padding:30px}
@media(max-width:900px){.grid2,.grid3,.verts,.row3{grid-template-columns:1fr}.cmp{font-size:12px}}'''

HTML = f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Aula · Conceptos de marca paraguas · v1</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Public+Sans:wght@400;500;700;800&family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,500;0,8..60,600;0,8..60,700;1,8..60,500&display=swap" rel="stylesheet">
<style>{CSS}</style></head><body>
<nav class="top"><b>Aula · conceptos v1</b><a href="#resumen">Resumen</a><a href="#catedra">A · Cátedra</a><a href="#boletin">B · Boletín</a><a href="#atrio">C · Atrio ★</a></nav>
<div class="wrap">
<div class="intro" id="resumen"><p style="letter-spacing:1.6px;text-transform:uppercase;font-size:12px;color:#8A5A12;margin:0">Marca paraguas · línea de preparación de oposiciones · octubre 2026</p>
<h1>Aula — tres direcciones de marca</h1>
<p>«Aula» es la marca común; cada cuerpo es una vertical: <b>Aula Museos</b>, <b>Aula Justicia</b>, <b>Aula Policía</b>, <b>Aula Administración</b>… Las tres propuestas son serias y oficiales; difieren en temperatura, símbolo y en cuánto cambia lo ya construido. Elegir una — después se redacta el manual completo de Aula.</p>
<p style="font-size:13px">Patrones de producto comunes a todas: prueba / examen (+1 · 0 · −1/3), Contenido IA con cita, Source Serif 4 o Inter, idioma español, una vertical = un par de colores (tinta + acento).</p></div>
<div class="rec">Recomendación: <b>C · Atrio</b> — conserva lo que ya funciona (Museos y la app v0.1 encajan sin rehacer), acoge el azul + ámbar de Justicia y escala a nuevos cuerpos con solo elegir dos colores.</div>
{CMP}
{A_html}{B_html}{C_html}
<div class="foot">Aula · conceptos de marca paraguas v1 · borrador interno para elección de dirección · no incluye dominios ni registro de marca · Prototipos ilustrativos: colores de Policía y Administración son provisionales.</div>
</div></body></html>'''
open('/workspace/polina-design/aula-umbrella/conceptos-aula-v1.html','w').write(HTML)
print(len(HTML))
