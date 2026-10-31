# Aula Justicia · manual de vertical v2 (bajo Atrio). Reuses umbrella helpers (../brandbook/build.py lines before "write logo assets").
import os, re, json, html
HERE = os.path.dirname(os.path.abspath(__file__)); UMB = os.path.join(HERE, "..", "brandbook")
src = open(os.path.join(UMB, "build.py")).read(); exec(src[:src.index("# ---------- write logo assets")])
OUT = HERE
NAME, SLUG, SECTOR = "Justicia", "justicia", "Gestión · Tramitación · Auxilio"
INK, ACC, REV, BG = "#14304D", "#B07A2A", "#D9A24E", "#EEF2F7"
S = scale(INK, ACC, BG)
J = dict(surface="#FFFFFF", paper2="#E3E9F1", line="#DCE4EE", text="#16202B", muted="#4A5868", subtle="#5F6B7B", **{k.replace('-','_'):v for k,v in S.items()}, acc_dark=REV)
ACC_TEXT = "#8A5F1F"  # v2: token de texto ámbar de la vertical (AA sobre fondo, superficie, ámbar 100, gris expediente)
CUERPOS = [("Gestión Procesal y Administrativa","Gestión Procesal","A2"),("Tramitación Procesal y Administrativa","Tramitación Procesal","C1"),("Auxilio Judicial","Auxilio Judicial","C2")]

assets = []
def save(name, content, folder="logos"):
    open(os.path.join(OUT, folder, name), "w").write(content); assets.append(f"{folder}/{name}")
save("aula-justicia-primary.svg", horiz(NAME, INK, ACC, INK)[0])
save("aula-justicia-primary-reverse.svg", horiz(NAME, P['paper'], REV, P['paper'], bg=INK, pad=24)[0])
save("aula-justicia-primary-mono-black.svg", horiz(NAME, P['ink'], P['ink'], P['ink'])[0])
save("aula-justicia-primary-mono-white.svg", horiz(NAME, "#FFFFFF", "#FFFFFF", "#FFFFFF")[0])
save("aula-justicia-stacked.svg", stacked(NAME, INK, ACC, S['acc-600'], SECTOR)[0])
save("aula-justicia-stacked-reverse.svg", stacked(NAME, P['paper'], REV, REV, SECTOR, bg=INK, pad=24)[0])
save("aula-justicia-symbol.svg", symbol_svg(INK, ACC))
save("aula-justicia-symbol-reverse.svg", symbol_svg(P['paper'], REV, INK, 8))
for full, short, grp in CUERPOS:
    sl = short.split()[0].lower().replace('ó','o')
    save(f"aula-justicia-{sl}-stacked.svg", stacked(NAME, INK, ACC, S['acc-600'], f"{short} · {grp}")[0])
d_tag, w_tag = text_path("Estudia como se examina.", "serif", 20, 0, 0)
hz, (hw, hh) = horiz(NAME, INK, ACC, INK)
save("aula-justicia-tagline.svg", svg(max(hw, w_tag), hh+40, hz.replace('<svg', '<svg x="0" y="0"', 1) + f'<path transform="translate(1,{hh+32})" d="{d_tag}" fill="{J["muted"]}"/>', "Aula Justicia · Estudia como se examina."))
save("icon-justicia-1024.svg", app_icon_full(INK, P['paper'], REV), "icons")
save("icon-justicia-light-1024.svg", app_icon_full(BG, INK, ACC), "icons")
save("favicon-justicia.svg", app_icon(INK, P['paper'], REV, 32), "icons")
# social card 1200x630
hzr = horiz(NAME, P['paper'], REV, P['paper'])[0].replace('<svg', '<svg x="80" y="90" width="620" height="126"', 1)
d1, _ = text_path("Estudia como se examina.", "serif", 54, 0, 0)
d2, _ = text_path("Gestión · Tramitación · Auxilio Judicial", "sans", 26, 0, 0)
og = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 630" width="1200" height="630"><rect width="1200" height="630" fill="{INK}"/>'
      f'<g transform="translate(860,250) scale(9)" opacity=".10">{arch(P["paper"], REV)}</g><rect x="80" y="540" width="120" height="6" fill="{REV}"/>{hzr}'
      f'<path transform="translate(80,380)" d="{d1}" fill="{P["paper"]}"/><path transform="translate(80,440)" d="{d2}" fill="{REV}"/></svg>')
save("aula-justicia-og-1200x630.svg", og, "icons")

# tokens
tokens = {"vertical": "justicia", "status": "Bloqueado (tinta + acento)", "inherits": "../brandbook/aula-tokens.css",
          "colors": {**S, "acc-dark": REV, "acc-text": ACC_TEXT, "surface": J['surface'], "paper-2": J['paper2'], "line": J['line'], "text": J['text'], "muted": J['muted'], "subtle": J['subtle']}, "version": "2.0", "text_tokens_v2": {"acc-text": ACC_TEXT, "subtle": J['subtle'], "rule": "texto ámbar siempre --v-acc-text; metadatos --subtle sobre fondo/superficie, --muted sobre paper-2"},
          "status_colors": {k: P[k] for k in ["ok","ok100","err","err100","warn","warn100","ai","ai100"]},
          "exam_scoring": {"type": "parámetro de convocatoria", "source": "bases de la convocatoria vigente (BOE)", "current_convocatoria": {"correct": 1, "blank": 0, "wrong": -0.25, "wrong_label": "−1/4"}, "example_per_question": {"correct": "+0,60", "wrong": "−0,15", "blank": "0"}, "note": "No heredar el −1/3 de Museos/ejemplo paraguas."}}
json.dump(tokens, open(os.path.join(OUT, "aula-justicia-tokens.json"), "w"), ensure_ascii=False, indent=2); assets.append("aula-justicia-tokens.json")
TCSS = '/* Aula Justicia · tokens de vertical v2 · cargar después de aula-tokens.css */\n[data-vertical="justicia"]{\n' + \
  ''.join(f"  --v-{k}:{v};\n" for k,v in S.items()) + f"  --v-acc-dark:{REV};\n  /* v2: texto ámbar AA (eyebrow, pill, cifras) */\n  --v-acc-text:{ACC_TEXT};\n" + \
  f"  /* neutros fríos de la vertical (sustituyen a los cálidos de plataforma dentro de la app) */\n  --surface:{J['surface']};\n  --paper:{BG};\n  --paper-2:{J['paper2']};\n  --line:{J['line']};\n  --text:{J['text']};\n  --muted:{J['muted']};\n  --subtle:{J['subtle']}; /* v2: #6B7787 → #5F6B7B (AA) */\n" + \
  "  /* estados: heredados de plataforma, no cambiar */\n}\n"
open(os.path.join(OUT, "aula-justicia-tokens.css"), "w").write(TCSS); assets.append("aula-justicia-tokens.css")

# ---------- HTML ----------
def rd(p): return open(os.path.join(OUT, p)).read()
E = html.escape
def swatch(hexv, name, role, token, on=None):
    on = on or J['bg']; fg = "#FFFFFF" if lum(hexv) < .35 else J['text']
    return (f'<div class="sw"><div class="chipc" style="background:{hexv};color:{fg}"><span>{cr(hexv,"#FFFFFF"):.1f}:1 ⬜ · {cr(hexv,on):.1f}:1 fondo</span></div>'
            f'<b>{name}</b><code>{hexv}</code><code class="t">--{token}</code><small>{role}</small></div>')
SEC = []
def section(num, sid, kicker, title, body):
    SEC.append((num, sid, kicker)); return f'<section id="{sid}"><p class="kicker">{num} · {kicker}</p><h2>{title}</h2>{body}</section>'
UMB_URL = "https://muratpod.github.io/polina-design/aula-umbrella/brandbook/"

# 01 marca
s1 = f'''<p class="lead">Aula Justicia usa el sistema Atrio sin modificaciones: arco + «Aula» en Source Serif 4 + «Justicia» en Inter Medium. La vertical solo aporta su par de colores: <b>azul toga</b> en arco y textos, <b>ámbar</b> en el basamento. Construcción, área de respeto y tamaños mínimos: ver <a href="{UMB_URL}#logo">manual paraguas · 01</a>.</p>
<div class="g2"><figure class="panel big">{rd("logos/aula-justicia-primary.svg")}<figcaption>Principal · <a href="logos/aula-justicia-primary.svg">SVG</a></figcaption></figure>
<figure class="panel big dark">{rd("logos/aula-justicia-primary-reverse.svg")}<figcaption>Inverso sobre azul toga · <a href="logos/aula-justicia-primary-reverse.svg">SVG</a></figcaption></figure></div>
<div class="g4"><figure class="panel st">{rd("logos/aula-justicia-stacked.svg")}<figcaption>Apilado · <a href="logos/aula-justicia-stacked.svg">SVG</a></figcaption></figure>
<figure class="panel st dark">{rd("logos/aula-justicia-stacked-reverse.svg")}<figcaption>Apilado inverso · <a href="logos/aula-justicia-stacked-reverse.svg">SVG</a></figcaption></figure>
<figure class="panel">{rd("logos/aula-justicia-primary-mono-black.svg")}<figcaption>Monocromo negro (fax, sellos, B/N) · <a href="logos/aula-justicia-primary-mono-black.svg">SVG</a></figcaption></figure>
<figure class="panel" style="background:#5B6B7D">{rd("logos/aula-justicia-primary-mono-white.svg")}<figcaption style="color:#fff">Monocromo blanco · <a style="color:#fff" href="logos/aula-justicia-primary-mono-white.svg">SVG</a></figcaption></figure></div>
<h3>Sublockups por cuerpo</h3><p class="note" style="margin-top:0">Para materiales específicos de un cuerpo (temarios, campañas, simulacros oficiales por convocatoria). El nombre del cuerpo es descriptivo: nunca sustituye a «Justicia» ni entra en el icono.</p>
<div class="g3">{''.join(f'<figure class="panel st">{rd(f"logos/aula-justicia-{c[1].split()[0].lower().replace('ó','o')}-stacked.svg")}<figcaption><b>{c[0]}</b> · subgrupo {c[2]} · <a href="logos/aula-justicia-{c[1].split()[0].lower().replace('ó','o')}-stacked.svg">SVG</a></figcaption></figure>' for c in CUERPOS)}</div>
<h3>Sí / No específicos de Justicia</h3>
<div class="g4 dd"><figure class="panel ok">{horiz(NAME, INK, ACC, INK)[0]}<figcaption>✓ Azul toga + basamento ámbar</figcaption></figure>
<figure class="panel no">{horiz(NAME, INK, "#9A3B28", INK)[0]}<figcaption>✗ Basamento rojo (se confunde con «error»)</figcaption></figure>
<figure class="panel no">{horiz(NAME, ACC, INK, ACC)[0]}<figcaption>✗ Invertir: texto ámbar, basamento azul</figcaption></figure>
<figure class="panel no"><div style="display:flex;align-items:center;gap:8px"><span style="font:700 13px var(--sans);color:#9A3B28;border:1.5px dashed #9A3B28;border-radius:8px;padding:6px 8px;white-space:nowrap">+ balanza</span>{horiz(NAME, INK, ACC, INK)[0].replace('width="','data-w="',1)}</div><figcaption>✗ Añadir balanza, mazo o toga al logotipo</figcaption></figure></div>'''

# 02 color
core = ''.join([swatch(S['ink-800'],"Azul toga","logotipo, botón primario, cabecera","v-ink-800"), swatch(S['ink-900'],"Azul toga 900","texto de enunciado, hover","v-ink-900"),
  swatch(S['ink-700'],"Azul 700","enlaces, iconos activos","v-ink-700"), swatch(S['ink-600'],"Azul 600","iconos secundarios","v-ink-600"),
  swatch(S['ink-100'],"Azul 100","chips de tema, pista de progreso","v-ink-100"), swatch(S['ink-50'],"Azul 50","opción seleccionada","v-ink-50"),
  swatch(S['acc-500'],"Ámbar","basamento, progreso, racha (no texto pequeño)","v-acc-500"), swatch(S['acc-600'],"Ámbar 600","bordes y trazos de acento (no texto)","v-acc-600"), swatch(ACC_TEXT,"Ámbar texto","eyebrow, pill, cifras ámbar · v2","v-acc-text"),
  swatch(S['acc-100'],"Ámbar 100","fondo de aviso de plazo, sello","v-acc-100"), swatch(REV,"Ámbar claro","basamento sobre azul, icono","v-acc-dark")])
neu = ''.join([swatch(BG,"Fondo Justicia","fondo de app","paper"), swatch(J['surface'],"Superficie","tarjetas, opciones","surface"), swatch(J['paper2'],"Gris expediente","bandas, inputs","paper-2"),
  swatch(J['line'],"Línea","bordes, separadores","line"), swatch(J['text'],"Texto","cuerpo","text"), swatch(J['muted'],"Texto suave","metadatos, texto sobre gris expediente","muted"), swatch(J['subtle'],"Subtle Justicia","metadatos, en blanco, pestañas inactivas · v2","subtle")])
st = ''.join([swatch(P['ok'],"Acierto","+1","ok"), swatch(P['err'],"Error","−1/4 (convocatoria actual)","err"), swatch(J['subtle'],"En blanco","0","subtle"), swatch(P['warn'],"Aviso","sin fuente, plazo","warn"), swatch(P['ai'],"Violeta IA","Contenido IA","ai")])
s2 = f'''<p class="lead">Azul toga y ámbar están <b>bloqueados</b> (heredados del manual paraguas). Este manual añade la escala completa y unos neutros fríos propios de la vertical; los colores de estado son de plataforma y no cambian.</p>
<div class="ratio"><span style="flex:58;background:{BG};color:{J['muted']}">Fondo 58 %</span><span style="flex:18;background:#fff;color:{J['muted']}">Superficie 18 %</span><span style="flex:16;background:{INK}">Azul toga 16 %</span><span style="flex:5;background:{ACC}">Ámbar 5 %</span><span style="flex:3;background:{P['ai']}">IA</span></div>
<p class="note">Proporción orientativa en pantalla. El ámbar es escaso a propósito: marca progreso y lo que importa (plazos, racha), nunca bloques grandes.</p>
<h3>Azul toga y ámbar</h3><div class="sws s5 s11">{core}</div>
<h3>Neutros de la vertical</h3><div class="sws s5">{neu}</div>
<h3>Estados (plataforma)</h3><div class="sws s5">{st}</div>
<p class="note"><b>v2 · tokens de texto:</b> todo texto ámbar usa <code>--v-acc-text</code> {ACC_TEXT} ({cr(ACC_TEXT,BG):.2f}:1 sobre fondo, {cr(ACC_TEXT,S["acc-100"]):.2f}:1 sobre ámbar 100); <code>--subtle</code> de Justicia pasa de #6B7787 a {J["subtle"]} ({cr(J["subtle"],BG):.2f}:1 sobre fondo). Ámbar 500/600 quedan para elementos no textuales. Los tokens paraguas no cambian. Detalle en <a href="#contraste">12 · Contraste</a>. Botón primario: texto blanco sobre azul toga ({cr("#FFFFFF",INK):.1f}:1).</p>'''

# 03 tipo
s3 = f'''<p class="lead">Mismo par que la plataforma: <b>Source Serif 4</b> para enunciados y titulares, <b>Inter</b> para interfaz y cifras (escala completa en el <a href="{UMB_URL}#tipo">manual paraguas · 03</a>). En Justicia añadimos reglas de <b>citación normativa</b>, porque el contenido es casi todo norma.</p>
<div class="g2"><div class="panel"><h4>Cómo se cita</h4><table class="t"><tr><th>Caso</th><th>Forma</th></tr>
<tr><td>Primera mención</td><td><span class="cite">Ley Orgánica 6/1985, de 1 de julio, del Poder Judicial (LOPJ)</span></td></tr>
<tr><td>Siguientes</td><td><span class="cite">art. 453.1 LOPJ</span></td></tr>
<tr><td>Constitución</td><td><span class="cite">art. 117.1 CE</span></td></tr>
<tr><td>Leyes procesales</td><td><span class="cite">art. 458.1 LEC</span> · <span class="cite">art. 14 LECrim</span></td></tr>
<tr><td>Fuente</td><td><span class="cite">BOE-A-1985-12666</span> (identificador BOE, enlazado)</td></tr>
<tr><td>Cita literal</td><td>Serif cursiva, comillas latinas, filete ámbar</td></tr></table></div>
<div class="panel"><h4>Muestra</h4><p style="font:500 20px/1.35 var(--serif);color:var(--v-ink-900);margin:0 0 10px">¿A quién corresponde, con exclusividad y plenitud, el ejercicio de la fe pública judicial?</p>
<blockquote class="lit">«Corresponde a los Letrados de la Administración de Justicia, con exclusividad y plenitud, el ejercicio de la fe pública judicial.»</blockquote><p class="note" style="margin-top:6px">art. 453.1 LOPJ · BOE-A-1985-12666</p>
<p class="note"><b>Reglas:</b> abreviaturas oficiales sin punto (LOPJ, LEC, LECrim, LJCA, LRJS, CE); «art.» en minúscula; números de artículo nunca partidos de su ley (usar espacio duro); denominaciones actuales: «Letrado/a de la Administración de Justicia» (no «Secretario judicial»).</p></div></div>'''

# 04 voz
VO = [("Bienvenida","«Buenas tardes, Lucía. Hoy: Tema 8, Tribunales de Instancia. Unos 10 minutos.»","«¡Vamos, futura jueza!» con emoji de balanza y fuego."),
 ("Acierto","«Correcto. El plazo para interponer apelación es de veinte días (art. 458.1 LEC).»","«¡Caso cerrado! ¡Sentencia a tu favor!»"),
 ("Error","«No es el Juez. La fe pública judicial corresponde al Letrado de la Administración de Justicia (art. 453.1 LOPJ).»","«¡Culpable! Has fallado.»"),
 ("Plazos","«Ojo al cómputo: en los plazos por días se excluyen los inhábiles.»","«Plazos = pesadilla 😱»"),
 ("Examen","«Nota orientativa: 37,80 / 60 (mínimo 30). Cada error resta 0,15 (−1/4).»","«Con esta nota apruebas seguro.»"),
 ("Contenido IA","«Explicación generada con IA · Fuente: BOE-A-2000-323, art. 458.»","Presentar la IA como criterio de un tribunal o doctrina oficial."),
 ("Sin fuente","«No tengo una fuente suficiente para explicarlo. Revisa el artículo en el BOE.»","Improvisar jurisprudencia o «lo normal es…».")]
vt = ''.join(f'<tr><td><b>{a}</b></td><td class="yes">{b}</td><td class="nop">{c}</td></tr>' for a,b,c in VO)
s4 = f'''<p class="lead">Aula Justicia habla como <b>un buen preparador de cuerpos de Justicia</b>: procedimental, preciso y tranquilo. Cada respuesta se apoya en un artículo; cada plazo se dice con su cómputo. Tuteo respetuoso; nada de teatro de juicio.</p>
<div class="taghero"><p class="tagline">«Estudia como se examina.»</p><p class="note">Lema común de Aula. Variantes de campaña para Justicia: «Cada artículo, en su sitio.» · «Del temario al expediente.» · «Plazos, órganos y procedimientos, pregunta a pregunta.»</p></div>
<div class="g4 pr"><div class="panel"><b>1 · Procedimental</b><p>Orden de la norma: órgano → competencia → plazo → recurso.</p></div><div class="panel"><b>2 · Citada</b><p>Toda afirmación lleva artículo y ley. Sin cita, no hay afirmación.</p></div><div class="panel"><b>3 · Actualizada</b><p>Denominaciones y redacciones vigentes; si una norma cambió, se indica la fecha.</p></div><div class="panel"><b>4 · Sobria</b><p>Sin metáforas de tribunal (mazos, veredictos, «culpable»), sin dramatizar.</p></div></div>
<table class="t voice"><tr><th>Situación</th><th>Sí</th><th>No</th></tr>{vt}</table>
<div class="g2"><div class="panel"><h4>Vocabulario propio</h4><p>cuerpo · subgrupo (A2 / C1 / C2) · convocatoria y bases · temario oficial · órgano judicial · competencia · plazo y cómputo · días hábiles · diligencia · notificación · recurso · supuesto práctico · Letrado/a de la Administración de Justicia (LAJ).</p></div>
<div class="panel"><h4>Evitar</h4><p>«Secretario judicial» (denominación anterior a 2015) · anglicismos de series («objeción», mazo) · confundir Gestión / Tramitación / Auxilio · prometer plaza · usar logotipos o escudos del Ministerio de Justicia o del CGPJ · insinuar relación oficial con la Administración.</p></div></div>'''

# 05 iconografía
def ico(body, c=INK, a=ACC):
    return f'<svg viewBox="0 0 24 24" width="44" height="44" fill="none" stroke="{c}" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">{body.replace("ACC", a)}</svg>'
ICONS = [("Expediente",'<path d="M3 7a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><path d="M7 13h10" stroke="ACC"/>'),
 ("Plazo",'<rect x="3.5" y="5" width="17" height="15" rx="2"/><path d="M8 3v4M16 3v4M3.5 10h17"/><path d="M12 13v3l2 1" stroke="ACC"/>'),
 ("Artículo",'<path d="M15 5.5c-1-1.2-2.6-1.6-4-1-1.6.7-1.7 2.8 0 3.8l2.4 1.4c1.8 1 1.6 3.3-.2 4"/><path d="M9 18.5c1 1.2 2.6 1.6 4 1 1.6-.7 1.7-2.8 0-3.8l-2.4-1.4c-1.8-1-1.6-3.3.2-4" stroke="ACC"/>'),
 ("Órgano",'<rect x="9" y="3" width="6" height="4" rx="1"/><rect x="3" y="16" width="6" height="4" rx="1"/><rect x="15" y="16" width="6" height="4" rx="1"/><path d="M12 7v4M6 16v-2.5h12V16" stroke="ACC"/>'),
 ("Notificación",'<rect x="3" y="5.5" width="18" height="13" rx="2"/><path d="m3.5 7 8.5 6 8.5-6" stroke="ACC"/>'),
 ("Recurso",'<path d="M4 12a8 8 0 1 1 2.3 5.6"/><path d="M4 18v-4h4" stroke="ACC"/>'),
 ("Código / ley",'<path d="M5 4.5A1.5 1.5 0 0 1 6.5 3H19v16H6.5A1.5 1.5 0 0 0 5 20.5z"/><path d="M5 20.5A1.5 1.5 0 0 0 6.5 22H19M9 7h6" stroke="ACC"/>'),
 ("Supuesto práctico",'<path d="M7 3h7l4 4v14H7z"/><path d="M14 3v4h4"/><path d="m9.5 14 2 2 3.5-4" stroke="ACC"/>')]
ig = ''.join(f'<div class="ic">{ico(b)}<small>{n}</small></div>' for n,b in ICONS)
s5 = f'''<p class="lead">Iconos lineales de 24 px, trazo 1,8 px, terminales redondeados; el detalle significativo en ámbar. Representan <b>objetos del procedimiento</b> (expedientes, plazos, notificaciones), no símbolos de tribunal.</p>
<div class="panel"><div class="icg">{ig}</div></div>
<div class="g2" style="margin-top:16px"><div class="panel"><h4>Sí</h4><ul><li>Documentos, calendarios, esquemas de órganos, flechas de recurso.</li><li>Fotografía (si la hay): mesa de estudio, temario anotado, luz natural; sin personas togadas.</li></ul></div>
<div class="panel"><h4>No</h4><ul><li>Mazo (no se usa en tribunales españoles), balanza, estatua de la Justicia, toga y puñetas como decoración.</li><li>Escudos oficiales, banderas, edificios reales de juzgados identificables.</li></ul></div></div>'''

# 06 icono app + redes
sizes = ''.join(f'<div class="sz">{app_icon(INK,P["paper"],REV,px)}<small>{px}px</small></div>' for px in (120,60,40,29,20))
s6 = f'''<div class="g3"><figure class="panel big icn">{app_icon(INK,P["paper"],REV,150)}<figcaption>Icono principal · <a href="icons/icon-justicia-1024.svg">SVG 1024</a> · <a href="icons/icon-justicia-1024.png">PNG</a></figcaption></figure>
<figure class="panel big icn">{app_icon(BG,INK,ACC,150)}<figcaption>Variante clara (web, prensa; no para tiendas) · <a href="icons/icon-justicia-light-1024.svg">SVG</a> · <a href="icons/icon-justicia-light-1024.png">PNG</a></figcaption></figure>
<div class="panel"><div class="szs">{sizes}</div><p class="note">Mismo dibujo que toda la línea Aula; Justicia = azul toga + basamento ámbar claro. Retícula y máscaras: <a href="{UMB_URL}#iconos">paraguas · 06</a>. Favicon: <a href="icons/favicon-justicia.svg">SVG</a>.</p></div></div>
<h3>Tarjeta para redes / Open Graph</h3><figure class="panel og">{rd("icons/aula-justicia-og-1200x630.svg").replace('width="1200" height="630"','width="100%"',1)}<figcaption>1200 × 630 · <a href="icons/aula-justicia-og-1200x630.svg">SVG</a> · <a href="icons/aula-justicia-og-1200x630.png">PNG</a></figcaption></figure>'''

# 07 UI
def btn(l,k): return f'<button class="b {k}">{l}</button>'
s7 = f'''<p class="lead">Componentes de plataforma con tokens de Justicia: <code>&lt;html data-vertical="justicia"&gt;</code> + <a href="aula-justicia-tokens.css">aula-justicia-tokens.css</a> (después de <a href="{UMB_URL}aula-tokens.css">aula-tokens.css</a>). Nada de hex en componentes.</p>
<div class="g2"><div class="panel"><h4>Botones</h4><div class="row">{btn("Continuar","pri")}{btn("Revisar","sec")}{btn("Abrir en BOE","ghost")}{btn("Entregar","pri dis")}</div>
<h4>Chips</h4><div class="row"><span class="chip cu">Tramitación · C1</span><span class="chip tema">Tema 8 · LOPJ</span><span class="chip mode">Prueba</span><span class="chip mode ex">Examen</span><span class="chip ai">✦ Contenido IA</span><span class="chip src">Fuente oficial · BOE</span><span class="chip plazo">⏱ Plazo: 20 días</span><span class="chip warn">Sin fuente suficiente</span></div>
<div class="prog"><span style="width:58%"></span></div><small class="pl">Temario Tramitación · 18 de 37 temas · racha 9 días</small></div>
<div class="panel"><h4>Selector de cuerpo</h4>{''.join(f'<div class="opt{" sel" if i==1 else ""}"><i>{g}</i><span><b>{f}</b><br><small style="color:var(--muted)">{["Subgrupo A2","Subgrupo C1","Subgrupo C2"][i]}</small></span></div>' for i,(f,s,g) in enumerate(CUERPOS))}<p class="note">El cuerpo elegido filtra temario, simulacros y penalización según las bases de la convocatoria vigente.</p></div></div>
<h3>Estados de examen</h3><div class="g3 states"><div class="state ok"><b>+1</b><span>Acierto</span><small>verde plataforma · solo al entregar en examen</small></div><div class="state bl"><b>0</b><span>En blanco</span><small>discontinuo · nunca penaliza</small></div><div class="state er"><b>−1/4</b><span>Error</span><small>teja · con explicación y artículo · −1/4 en la convocatoria actual</small></div></div>
<p class="note">La puntuación es un <b>parámetro de convocatoria</b>: se lee de las bases, no del manual. <b>Convocatoria actual de Justicia: cada error resta 1/4 del valor de un acierto (−1/4).</b> Ejemplo: si un acierto vale +0,60, un error resta −0,15 y una respuesta en blanco vale 0. La UI muestra siempre la fórmula aplicada; si una convocatoria futura fija otra fracción, el chip y el resultado la muestran tal cual. (El −1/3 del manual paraguas es el ejemplo de Museos/genérico, no aplica a Justicia.)</p>
<h3>Opciones y Contenido IA</h3><div class="g2"><div><div class="opt"><i>A</i>Por defecto</div><div class="opt sel"><i>B</i>Seleccionada</div><div class="opt okk"><i>✓</i>Correcta (revisión)</div><div class="opt err"><i>✗</i>Elegida y errónea</div></div>
<div><div class="aibox"><small class="ov">✦ RESPUESTA AULA · CONTENIDO IA · CON FUENTE</small><p>El recurso de apelación se interpone ante el tribunal que dictó la resolución, en veinte días desde el siguiente a la notificación.</p><a>BOE-A-2000-323 · LEC, art. 458.1</a><small class="lv">Nivel de fuente: Legislación</small></div>
<div class="aibox abst" style="margin-top:10px"><small class="ov">✦ RESPUESTA AULA · CONTENIDO IA · SIN FUENTE</small><p>No tengo una fuente suficiente para explicarlo. Revisa el artículo en el BOE.</p><small class="lv"><code>abstain = true</code> → se muestra <code>message_es</code></small></div></div></div>
<details><summary>Ver aula-justicia-tokens.css</summary><pre>{E(TCSS)}</pre></details>'''

# 08 screens
brand = '<span class="pbrand"><span class="ps">Aula</span> <span class="pv">Justicia</span></span>'
def scr(inner, cls=""): return f'<div class="phone" data-vertical="justicia"><div class="scr {cls}">{inner}</div></div>'
home = scr(f'''<div class="ph-top">{brand}<span class="chip cu">Tramitación · C1</span></div>
<p class="hi">Buenas tardes, Lucía.</p><p class="note" style="margin:0 0 12px">Racha: 9 días · 18 de 37 temas vistos</p>
<div class="card2"><small class="ovj">HOY · 10 MIN</small><p class="ct">Tema 8 · Tribunales de Instancia (LOPJ)</p><div class="prog"><span style="width:40%"></span></div><button class="b pri" style="width:100%;margin-top:12px">Continuar en el aula</button></div>
<div class="g2m"><div class="card2"><small class="ovj">PRUEBA</small><p>Práctica con corrección inmediata</p></div><div class="card2"><small class="ovj">EXAMEN</small><p>Simulacro 100 preguntas · +1 · 0 · −1/4</p></div></div>
<div class="card2 pz"><span class="chip plazo">⏱ Repaso</span><p>Plazos LEC (temas 16–28): 12 tarjetas pendientes</p></div>''')
qopts = ["La provincia","El partido judicial","La comunidad autónoma","El municipio"]
def opts(sel, review):
    o=""
    for i,t in enumerate(qopts):
        c = (" okk" if i==1 else (" err" if i==sel else "")) if review else (" sel" if i==sel else "")
        m = ("✓" if i==1 else ("✗" if i==sel else "ABCD"[i])) if review else "ABCD"[i]
        o += f'<div class="opt{c}"><i>{m}</i>{t}</div>'
    return o
exam = scr(f'''<div class="ph-top">{brand}<span class="chip mode ex">Examen · 47/100</span></div><div class="prog"><span style="width:47%"></span></div>
<div class="ph-meta"><span>⏱ 52:10 restantes</span><span>en blanco 4</span></div><p class="ph-q">Según la LOPJ, ¿qué ámbito territorial tiene el Tribunal de Instancia?</p>{opts(0,False)}
<p class="fm" style="text-align:left">Sin corrección hasta entregar · +0,60 · 0 · −0,15 (−1/4)</p><div class="ph-b"><button class="b sec">Dejar en blanco</button><button class="b pri">Siguiente</button></div>''')
res = scr(f'''<div class="ph-top">{brand}<span class="chip mode ex">Simulacro entregado</span></div><p class="ov2">NOTA ORIENTATIVA</p><p class="big">37,80<small> / 60</small></p><p class="ten">6,30 sobre 10</p>
<div class="rgrid"><div class="state ok"><b>68</b><span>+40,80 aciertos</span></div><div class="state bl"><b>12</b><span>0 en blanco</span></div><div class="state er"><b>20</b><span>−3,00 errores</span></div></div>
<p class="fm">Neta = 68 × 0,60 − 20 × 0,15 = 37,80 / 60 (−1/4, convocatoria actual; mínimo 30). No es una calificación oficial.</p>
<div class="card2"><small class="ovj">DÓNDE FALLAS</small><p>Tema 5 · Unión Europea · 7 errores<br>Tema 7 · Órganos judiciales (LOPJ) · 5 errores</p></div>
<div class="ph-b"><button class="b sec">Revisar errores</button><button class="b pri">Repasar tema 5</button></div>''', "res")
rev = scr(f'''<div class="ph-top">{brand}<span class="chip mode">Revisión · 47/100</span></div><div class="prog"><span style="width:47%"></span></div>
<div class="ph-meta"><span>Tu respuesta: A · <b class="r">−1/4</b></span><span>Tema 8 · LOPJ</span></div><p class="ph-q">Según la LOPJ, ¿qué ámbito territorial tiene el Tribunal de Instancia?</p>{opts(0,True)}
<div class="aibox sm"><small class="ov">✦ RESPUESTA AULA · CONTENIDO IA · CON FUENTE</small><p>Habrá un Tribunal de Instancia en cada partido judicial, con sede en su capital; la provincia es la demarcación de la Audiencia Provincial.</p><a>BOE-A-1985-12666 · LOPJ, art. 84.1</a></div>
<div class="ph-b"><button class="b sec">Anterior</button><button class="b pri">Siguiente error</button></div>''')
s8 = f'''<p class="lead">Cuatro pantallas clave en azul toga + ámbar: inicio, examen en curso (sin feedback), resultado con nota neta y revisión con explicación IA citada.</p><div class="phones">{home}{exam}{res}{rev}</div>'''


# ================= v2 · componentes app v0.2, microcopia, prohibiciones, contraste =================
T = dict(paper=BG, surface=J['surface'], paper2=J['paper2'], line=J['line'], text=J['text'], muted=J['muted'], subtle=J['subtle'])
# 09 componentes v0.2
grid = ''.join(f'<i class="{c}">{n}</i>' for n,c in [(i, 'a' if i<17 and i not in (5,9,12) else ('m' if i in (9,) else ('c' if i==17 else ('b' if i in (5,12) else '')))) for i in range(1,31)])
TAB = [("Inicio",'<path d="M4 20V11a8 8 0 0 1 16 0v9"/><path d="M8.5 20v-8a3.5 3.5 0 0 1 7 0v8"/><path class="acc" d="M2.5 21h19"/>',True),
       ("Temario",'<path d="M5 4h10a3 3 0 0 1 3 3v13H8a3 3 0 0 1-3-3z"/><path class="acc" d="M9 9h6M9 12.5h4"/>',False),
       ("Simulacro",'<circle cx="12" cy="13" r="8"/><path class="acc" d="M12 9v4l2.5 2"/><path d="M9.5 2.5h5"/>',False),
       ("Leyes",'<path d="M6 3h9l4 4v14H6z"/><path d="M15 3v4h4"/><path class="acc" d="M9 12h7M9 15.5h7M9 8.5h3"/>',False)]
tabs = ''.join(f'<a class="{"on" if on else ""}"><svg viewBox="0 0 24 24">{d}</svg>{l}</a>' for l,d,on in TAB)
s9v = f"""<p class="lead">Componentes añadidos en las maquetas <b>v0.2</b> de la app (onboarding, camino de temas, prueba, simulacro, resultado, banco de leyes). Todos usan tokens; ningún hex en componentes. Referencia: <code>/workspace/aula-justicia/mockups/assets/app.css</code> (Aula Justicia Design).</p>
<div class="g2"><div class="panel"><h4>Chips de baremo</h4><div class="row"><span class="k-chip ok">+0,60 acierto</span><span class="k-chip bl">0 en blanco</span><span class="k-chip er">−0,15 error (−1/4)</span></div>
<p class="note">Siempre los tres, en este orden, con <b>valor por pregunta</b> y fracción. Aparecen en: reglas previas al simulacro, cabecera del simulacro y resultado. Valores = parámetro de convocatoria (<code>exam_scoring</code>), nunca fijados en el componente.</p></div>
<div class="panel"><h4>Cita de artículo</h4><blockquote class="k-quote">«Habrá un Tribunal de Instancia en cada partido judicial, con sede en su capital, de la que tomará su nombre.»</blockquote>
<div class="k-src">art. 84.1 LOPJ <a>BOE-A-1985-12666 ↗</a></div><p class="note">Serif cursiva, comillas latinas, <b>filete ámbar 3 px</b> (<code>--v-acc-500</code>, elemento no textual) sobre <code>--paper</code>. Debajo, la cita corta + identificador BOE como enlace al texto consolidado. Obligatoria en toda explicación de prueba.</p></div></div>
<div class="g2"><div class="panel"><h4>Badge Contenido IA</h4><div class="k-ai"><div class="k-ai-h"><b>✦ Respuesta Aula · Contenido IA</b><span>con fuente</span></div><p>Pista: la provincia es la demarcación de la Audiencia Provincial; el partido judicial, la del Tribunal de Instancia.</p><small>[1] LOPJ, art. 84.1 · Nivel de fuente: Legislación</small></div>
<div class="k-ai abst"><div class="k-ai-h"><b>✦ Respuesta Aula · Contenido IA</b><span>sin fuente</span></div><p>No tengo una fuente suficiente para explicarlo. Revisa el artículo en el BOE.</p></div>
<p class="note">Texto del badge fijo: <b>«✦ Respuesta Aula · Contenido IA»</b> (igual que web v0.1). Violeta IA solo para este bloque. Nunca sustituye a la cita literal ni se presenta como criterio de tribunal.</p></div>
<div class="panel"><h4>Hoja de respuestas y temporizador</h4><div class="row" style="justify-content:space-between;align-items:center"><span class="k-timer">⏱ 52:10</span><small style="color:var(--muted)">Simulacro · 17/100</small></div>
<div class="k-grid">{grid}</div><div class="k-leg"><span class="a">respondida</span><span class="m">marcada</span><span class="c">actual</span><span class="b">en blanco</span><span>pendiente</span></div>
<p class="note">Respondida = azul 700; marcada = ámbar 100 + borde ámbar; actual = contorno ámbar 2 px; en blanco = borde discontinuo. La hoja <b>no revela aciertos</b> hasta entregar. Marcador en directo: solo rango posible de neta (p. ej. 40 respondidas → entre −6,00 y +24,00).</p></div></div>
<div class="g2"><div class="panel"><h4>Tarjeta de ley</h4><div class="k-law"><div class="k-law-h"><b>LOPJ</b><span class="k-pill">En tu temario</span></div><p>Ley Orgánica 6/1985, de 1 de julio, del Poder Judicial</p><small>A2 · C1 · C2 · Temas 7–8</small><div class="k-law-f"><span><b>5</b> preguntas · 5 arts. citados</span><a>BOE-A-1985-12666 ↗</a></div></div>
<p class="note">Sigla en serif + nombre oficial completo en primera mención + cuerpos + temas + identificador BOE. Estado «por confirmar» en gris cuando el mapeo al temario no está validado. Filtro por defecto: <b>Mi temario</b>.</p></div>
<div class="panel"><h4>Tab bar · camino · racha</h4><nav class="k-tabs">{tabs}</nav>
<div class="row" style="margin-top:14px;align-items:center;gap:14px"><span class="k-dot done">✓</span><span class="k-dot now">4</span><span class="k-dot">5</span><span class="k-dot lock">7</span><span class="k-stat"><b>9</b> días de racha</span><span class="k-stat"><b>1.240</b> XP</span></div>
<p class="note">Cuatro pestañas: Inicio · Temario · Simulacro · Leyes; activa en azul toga con detalle ámbar. Nodos: hecho (azul), actual (ámbar + halo ámbar 100), siguiente (blanco), bloqueado (gris expediente). Racha y XP discretos: cifras en serif, sin confeti ni llamas grandes.</p></div></div>
<div class="panel" style="margin-top:16px"><h4>Descargo (obligatorio)</h4><p class="k-foot">Aula Justicia · Material de estudio no oficial, sin relación con el Ministerio de Justicia ni el CGPJ. Verifique siempre en el BOE.</p>
<p class="note">Al pie de inicio, resultado, banco de leyes y en el onboarding. Nota de examen: siempre «Nota orientativa» + «No es una calificación oficial». Fechas no publicadas: chip «fecha de ejemplo» o «aún no hay fecha».</p></div>"""

# 10 microcopia
MC = [("Onboarding","«¿A qué cuerpo te presentas? El cuerpo elegido filtra el temario, los simulacros y la penalización.»","«¡Elige tu destino, futuro funcionario!»"),
 ("Fecha de examen","«Fecha prevista · la ajustas cuando se publique en el BOE.» / «Aún no hay fecha · avísame cuando salga.»","Inventar o insinuar una fecha oficial."),
 ("Objetivo diario","«Te faltan 8 minutos para mantener la racha.»","«¡No pierdas tu racha o lo pagarás! 🔥»"),
 ("Racha perdida","«Racha reiniciada. Retoma hoy con 10 minutos del Tema 4.»","«Has fallado a tu racha.»"),
 ("Antes del simulacro","«Cada error o respuesta múltiple resta 1/4 del valor de un acierto. Las preguntas en blanco no puntúan.»","«Cuidado, que te penalizan mucho.»"),
 ("Duda en examen","«Si dudas entre dos, piensa si te compensa arriesgar.»","«Arriesga siempre» / «Nunca contestes si dudas.»"),
 ("Tiempo","«Quedan 5 minutos. Al llegar a 0 se entrega solo.»","«¡Se acaba el tiempo! 😱»"),
 ("Bajo el mínimo","«29,40 / 60: por debajo del mínimo de 30. Donde más restas: Tema 5 · Unión Europea.»","«Suspendido.»"),
 ("Sobre el mínimo","«37,80 / 60: supera el mínimo de 30 del primer ejercicio. No es una calificación oficial.»","«¡Aprobado! Ya tienes la plaza.»"),
 ("Tema vacío","«Sin preguntas para este tema todavía · pronto.»","«Próximamente, ¡estate atento!» con fecha inventada."),
 ("Ley no mapeada","«Pendiente de mapear con el anexo VI.»","Atribuir una ley a un tema sin validarlo.")]
mt = ''.join(f'<tr><td><b>{a}</b></td><td class="yes">{b}</td><td class="nop">{c}</td></tr>' for a,b,c in MC)
s10v = f"""<p class="lead">Microcopia de las pantallas v0.2 bajo la voz de la vertical: <b>procedimental, citada, actualizada, sobria</b>. Tuteo; cifras con coma decimal y punto de miles (1.240 XP; 37,80); el signo menos es «−» (U+2212).</p>
<table class="t voice"><tr><th>Situación</th><th>Sí</th><th>No</th></tr>{mt}</table>"""

# 11 prohibiciones
s11v = """<div class="g2"><div class="panel no-list"><h4>Nunca en Aula Justicia</h4><ul>
<li>Mazo, balanza, estatua de la Justicia, toga o puñetas como decoración, en logo, iconos, ilustración o emoji (tampoco el emoji de balanza).</li>
<li>Escudos, emblemas o logotipos del Ministerio de Justicia, CGPJ, Casa Real, BOE o comunidades autónomas; banderas; fotos de sedes judiciales identificables.</li>
<li>Basamento rojo o teja; invertir azul/ámbar; mezclar colores de otra vertical (terracota de Museos).</li>
<li>Presentarse como recurso oficial, «homologado» o vinculado a la Administración; prometer plaza o aprobado.</li>
<li>Penalización fija en el diseño (−1/3 u otra): siempre parámetro de convocatoria.</li>
<li>Contenido IA sin badge, sin fuente o como doctrina/criterio de tribunal; jurisprudencia improvisada.</li>
<li>Fechas, plazas o notas de corte no publicadas presentadas como reales.</li>
<li>«Secretario judicial» (usar Letrado/a de la Administración de Justicia).</li></ul></div>
<div class="panel"><h4>Siempre</h4><ul><li>Artículo + ley + identificador BOE en cada explicación.</li><li>Fórmula de puntuación visible antes, durante y después del simulacro.</li><li>«Nota orientativa» y descargo de no oficialidad.</li><li>Ejemplos marcados como «ejemplo» cuando no sean datos de convocatoria publicados.</li><li>Ámbar escaso: progreso, racha, plazos, nodo actual.</li></ul></div></div>"""

# 12 contraste
PAIRS = [("Texto","text",J['text'],"Fondo","paper",BG,"text"),("Texto","text",J['text'],"Superficie","surface",J['surface'],"text"),
 ("Texto suave","muted",J['muted'],"Fondo","paper",BG,"text"),("Texto suave","muted",J['muted'],"Superficie","surface",J['surface'],"text"),("Texto suave","muted",J['muted'],"Gris expediente","paper-2",J['paper2'],"text"),
 ("Subtle Justicia","subtle",J['subtle'],"Fondo","paper",BG,"text"),("Subtle Justicia","subtle",J['subtle'],"Superficie","surface",J['surface'],"text"),
 ("Azul toga","v-ink-800",S['ink-800'],"Fondo","paper",BG,"text"),("Blanco","#FFF","#FFFFFF","Azul toga (botón)","v-ink-800",S['ink-800'],"text"),
 ("Azul 700 (enlace)","v-ink-700",S['ink-700'],"Superficie","surface",J['surface'],"text"),("Azul 900","v-ink-900",S['ink-900'],"Azul 50 (seleccionada)","v-ink-50",S['ink-50'],"text"),
 ("Azul 800 (pill tema)","v-ink-800",S['ink-800'],"Azul 50","v-ink-50",S['ink-50'],"text"),
 ("Ámbar texto (eyebrow)","v-acc-text",ACC_TEXT,"Fondo","paper",BG,"text"),("Ámbar texto","v-acc-text",ACC_TEXT,"Superficie","surface",J['surface'],"text"),
 ("Ámbar texto (pill)","v-acc-text",ACC_TEXT,"Ámbar 100","v-acc-100",S['acc-100'],"text"),("Ámbar texto","v-acc-text",ACC_TEXT,"Gris expediente","paper-2",J['paper2'],"text"),
 ("Blanco (nodo actual, 19 px bold)","#FFF","#FFFFFF","Ámbar 500","v-acc-500",S['acc-500'],"large"),
 ("Ámbar 500","v-acc-500",S['acc-500'],"Fondo","paper",BG,"ui"),("Ámbar 500","v-acc-500",S['acc-500'],"Superficie","surface",J['surface'],"ui"),
 ("Ámbar 600 (borde)","v-acc-600",S['acc-600'],"Fondo","paper",BG,"ui"),
 ("Ámbar claro","v-acc-dark",REV,"Azul toga","v-ink-800",S['ink-800'],"ui"),("Azul 100 (pista)","v-ink-100",S['ink-100'],"Fondo","paper",BG,"ui"),
 ("Línea","line",J['line'],"Superficie","surface",J['surface'],"ui"),
 ("Acierto","ok",P['ok'],"Acierto 100","ok100",P['ok100'],"text"),("Error","err",P['err'],"Error 100","err100",P['err100'],"text"),
 ("Violeta IA","ai",P['ai'],"IA 100","ai100",P['ai100'],"text"),("Aviso","warn",P['warn'],"Aviso 100","warn100",P['warn100'],"text"),
 ("Blanco","#FFF","#FFFFFF","Acierto","ok",P['ok'],"text"),("Blanco","#FFF","#FFFFFF","Error","err",P['err'],"text")]
def verdict(r, kind):
    if kind=="ui": return ("✓ ≥ 3:1 no textual" if r>=3 else "✗ < 3:1 · solo decorativo"), r>=3
    if kind=="large": return ("AA texto grande (≥ 18,66 px bold)" if r>=3 else "✗ no apto"), r>=3
    if r>=7: return "AAA", True
    if r>=4.5: return "AA", True
    if r>=3: return "AA grande (≥ 18,66 px bold / 24 px)", False
    return "✗ no apto para texto", False
rows=''
TXT_FAIL=[(fn,bn) for fn,ft,fh,bn,bt,bh,k in PAIRS if k=='text' and cr(fh,bh)<4.5]
assert not TXT_FAIL, TXT_FAIL
for fn,ft,fh,bn,bt,bh,k in PAIRS:
    r=cr(fh,bh); v,okk=verdict(r,k)
    rows+=f'<tr><td><span class="k-sw" style="background:{bh};color:{fh}">Aa</span></td><td><b>{fn}</b> <code>{ft if ft.startswith("#") else "--"+ft}</code><br>sobre {bn} <code>{"--"+bt if not bt.startswith("#") else bt}</code></td><td class="num">{r:.2f}:1</td><td>{ {"text":"texto","large":"texto grande","ui":"no textual"}[k] }</td><td class="{"yes" if okk else "nop"}">{v}</td></tr>'
s12v = f"""<p class="lead">Contraste WCAG 2.2 (fórmula de luminancia relativa) calculado desde los tokens al generar el manual. Texto normal ≥ 4,5:1 (AA), texto grande ≥ 3:1, elementos no textuales (bordes, barras, filetes, iconos) ≥ 3:1 (1.4.11).</p>
<table class="t k-cr"><tr><th></th><th>Par</th><th>Ratio</th><th>Uso</th><th>Resultado</th></tr>{rows}</table>
<p class="note"><b>Resultado v2:</b> todos los pares de <b>texto</b> pasan AA (≥ 4,5:1); la generación falla si alguno no lo cumple. <b>Reglas:</b> texto ámbar siempre en <code>--v-acc-text</code> (nunca <code>--v-acc-500</code>/<code>--v-acc-600</code>); metadatos y «en blanco» en <code>--subtle</code> sobre fondo y superficie, en <code>--muted</code> sobre gris expediente (<code>--subtle</code> sobre <code>--paper-2</code> da {cr(J['subtle'],J['paper2']):.2f}:1); blanco sobre ámbar 500 solo como texto grande (número del nodo actual a 19 px bold). Ámbar 500/600 solo para basamento, barra, filete, borde y nodo. <code>--line</code> y <code>--v-ink-100</code> no alcanzan 3:1: los controles no dependen solo del borde (la opción seleccionada y la casilla respondida cambian también de fondo). Foco: anillo oro Atrio 3 px.</p>
<div class="panel" style="margin-top:12px"><h4>Tokens de texto de la vertical · v2</h4><div class="row" style="gap:16px;align-items:center"><span class="k-sw" style="background:{BG};color:{ACC_TEXT};width:auto;padding:0 10px">--v-acc-text {ACC_TEXT} · {cr(ACC_TEXT,BG):.2f}:1</span><span class="k-sw" style="background:{S['acc-100']};color:{ACC_TEXT};width:auto;padding:0 10px">pill · {cr(ACC_TEXT,S['acc-100']):.2f}:1</span><span class="k-sw" style="background:{BG};color:{J['subtle']};width:auto;padding:0 10px">--subtle {J['subtle']} · {cr(J['subtle'],BG):.2f}:1</span></div>
<p class="note">Definidos en <a href="aula-justicia-tokens.css">aula-justicia-tokens.css</a> (vertical). Los tokens del manual paraguas (<code>aula-tokens.css</code>) no cambian. Antes (v1): texto ámbar en <code>--v-acc-600</code> {S['acc-600']} ({cr(S['acc-600'],BG):.2f}:1 sobre fondo) y <code>--subtle</code> #6B7787 ({cr("#6B7787",BG):.2f}:1).</p></div>"""

# 09 relación
s9 = f'''<div class="g2"><div class="panel"><h4>Hereda del manual paraguas (no redefinir)</h4><ul><li>Símbolo, construcción, área de respeto, tamaños mínimos.</li><li>Tipografías y escala; radios 10/16/22/pill; foco oro Atrio.</li><li>Estados (acierto · en blanco · error), violeta IA, contrato <code>/v0/explain</code> (abstain → <code>message_es</code>).</li><li><b>No se hereda:</b> la penalización. Es parámetro de convocatoria; Justicia, convocatoria actual: −1/4 (el −1/3 del paraguas es el ejemplo de Museos).</li><li>Voz común: exacta, serena, cercana, transparente.</li></ul><p class="note"><a href="{UMB_URL}">Manual paraguas Aula · Atrio v1 →</a></p></div>
<div class="panel"><h4>Propio de Justicia</h4><ul><li>Azul toga #14304D + ámbar #B07A2A (bloqueados) y su escala; neutros fríos.</li><li>Sublockups por cuerpo (Gestión A2 · Tramitación C1 · Auxilio C2) y selector de cuerpo.</li><li>Reglas de citación normativa y vocabulario procesal; chip «Plazo».</li><li>Iconografía de procedimiento; prohibidos mazo, balanza y escudos oficiales.</li></ul></div></div>
<div class="panel" style="margin-top:16px"><h4>Para Aula Justicia Design (reutilizar)</h4><p class="note" style="margin-top:0">Partir de la app web v0.1 de Museos (<a href="https://muratpod.github.io/polina-design/app/">/app/</a>): cambiar <code>data-vertical</code> a <code>justicia</code>, cargar <code>aula-justicia-tokens.css</code>, sustituir logotipo por <code>logos/aula-justicia-primary.svg</code> y contenidos por los del temario de Justicia. Los patrones prueba/examen, racha/XP discretos y Contenido IA se mantienen idénticos en toda la línea. <b>Puntuación:</b> la app de Museos usa −1/3; en Justicia configurar la penalización como parámetro de convocatoria con el valor actual <b>−1/4</b> (p. ej. +0,60 / −0,15), ver <code>exam_scoring</code> en <a href="aula-justicia-tokens.json">aula-justicia-tokens.json</a>.</p></div>
<p class="note">Los ejemplos de preguntas son ilustrativos y deben validarse con el temario y la convocatoria vigentes. Sin dominios ni registro de marca.</p>'''

secs = [section("01","marca","Marca","Aula Justicia",s1), section("02","color","Color","Azul toga y ámbar",s2), section("03","tipo","Tipografía y citas","Escribir la norma",s3),
        section("04","voz","Voz y tono","Cómo habla Aula Justicia",s4), section("05","iconos","Iconografía","Objetos del procedimiento",s5),
        section("06","app","Icono y redes","Icono de app y tarjetas",s6), section("07","ui","UI","Tokens y componentes",s7),
        section("08","pantallas","Pantallas","Inicio, examen, resultado, revisión",s8), section("09","app02","Componentes v0.2","Componentes de la app v0.2",s9v),
        section("10","micro","Microcopia","Microcopia por pantalla",s10v), section("11","prohibido","Prohibiciones","Lo que nunca hace Aula Justicia",s11v),
        section("12","contraste","Contraste","Contraste WCAG de la paleta",s12v), section("13","relacion","Relación","Paraguas y reutilización",s9)]
nav = ''.join(f'<a href="#{sid}">{n} {k}</a>' for n,sid,k in SEC)
files = ''.join(f'<li><a href="{a}">{a}</a></li>' for a in assets + ["icons/icon-justicia-1024.png","icons/icon-justicia-light-1024.png","icons/aula-justicia-og-1200x630.png"])
BASE = re.search(r'<style>(.*?)</style>', open(os.path.join(UMB, "index.html")).read(), re.S).group(1)
CSS = BASE + TCSS.replace('[data-vertical="justicia"]', ':root,[data-vertical="justicia"]') + f'''
:root{{--ink:{INK}}}.panel.dark{{background:{INK}}}.kicker{{color:{ACC_TEXT}}}.cover{{background:{INK}}}.top{{background:{INK}f2}}a{{color:{S['ink-700']}}}
.sws.s5{{grid-template-columns:repeat(5,1fr)}}.ratio{{display:flex;height:54px;border-radius:14px;overflow:hidden;border:1px solid var(--line);margin:8px 0}}.ratio span{{display:flex;align-items:center;padding:0 10px;font-size:12px;color:#fff;font-weight:600;white-space:nowrap;overflow:hidden}}
.cite{{font-family:var(--serif);color:var(--v-ink-900)}}blockquote.lit{{margin:0;padding:4px 0 4px 12px;border-left:3px solid var(--v-acc-500);font:italic 500 16px/1.45 var(--serif);color:var(--muted)}}
.icg{{display:grid;grid-template-columns:repeat(8,1fr);gap:10px}}.ic{{display:flex;flex-direction:column;align-items:center;gap:6px;font-size:12px;color:var(--muted);text-align:center}}
.chip.cu{{background:var(--v-acc-100);color:var(--v-acc-text)}}.chip.plazo{{background:var(--v-acc-100);color:var(--v-acc-text)}}.res .ten{{color:var(--v-acc-text)}}.sws.s11{{grid-template-columns:repeat(6,1fr)}}
figure.st{{align-items:center}}figure.st svg{{max-height:170px;width:auto}}figure.dark figcaption,figure.dark figcaption a{{color:#E5EBF2}}
figure.icn{{align-items:center}}figure.icn svg{{filter:drop-shadow(0 8px 16px #14304D40)}}figure.og svg{{border-radius:12px}}
.phones{{gap:14px;flex-wrap:nowrap}}.phone{{width:25%;max-width:300px;padding:9px;border-radius:38px}}.scr{{min-height:600px;padding:18px 12px 14px;border-radius:30px}}.phone{{display:flex}}.scr{{flex:1}}.scr .pbrand .ps{{font-size:16px}}.scr .pbrand .pv{{font-size:13.5px}}.scr .ph-top{{gap:6px}}.scr .ph-top .chip{{font-size:10.5px;padding:4px 8px;white-space:nowrap}}.scr .ph-q{{font-size:17px}}.scr .opt{{font-size:13px;padding:9px 10px}}.res .big{{font-size:46px}}.hi{{font:600 24px var(--serif);color:var(--v-ink-800);margin:4px 0 2px}}
.card2{{background:var(--surface);border:1px solid var(--line);border-radius:var(--r-md);padding:12px 14px;margin-bottom:10px}}.card2 p{{margin:4px 0 0;font-size:13.5px}}.card2 .ct{{font:600 17px var(--serif);color:var(--v-ink-900);margin:4px 0 10px}}
.ovj{{font-size:10.5px;letter-spacing:1.3px;font-weight:700;color:var(--v-acc-text)}}.g2m{{display:grid;grid-template-columns:1fr 1fr;gap:10px}}.pz p{{margin-top:8px}}
.opt span small{{font-weight:400}}
:root{{--ok-100:var(--ok100);--err-100:var(--err100);--ai-100:var(--ai100);--warn-100:var(--warn100);--gold-100:var(--gold100)}} /* v2: alias de estados (antes indefinidos) */
.k-chip{{display:inline-flex;align-items:center;border:1.5px solid var(--line);border-radius:99px;padding:5px 11px;font:600 12.5px var(--sans)}}.k-chip.ok{{color:var(--ok);background:var(--ok-100);border-color:var(--ok-100)}}.k-chip.er{{color:var(--err);background:var(--err-100);border-color:var(--err-100)}}.k-chip.bl{{color:var(--subtle);border-style:dashed;background:var(--surface)}}
.k-quote{{margin:0 0 10px;padding:10px 12px;border-left:3px solid var(--v-acc-500);background:var(--paper);border-radius:0 8px 8px 0;font:italic 500 15px/1.45 var(--serif);color:var(--text)}}
.k-src{{display:flex;gap:8px;align-items:center;font-size:12.5px;color:var(--subtle)}}.k-src a,.k-law-f a{{font-weight:600;border:1px solid var(--line);border-radius:8px;padding:4px 8px;background:var(--surface);color:var(--v-ink-700);text-decoration:none;font-size:12px}}
.k-ai{{background:var(--ai-100);border-radius:12px;padding:12px 14px;margin-bottom:10px;font-size:14px}}.k-ai p{{margin:0 0 6px}}.k-ai small{{color:var(--ai);font-weight:600;font-size:12px}}.k-ai-h{{display:flex;justify-content:space-between;align-items:center;margin-bottom:6px}}.k-ai-h b{{color:var(--ai);font-size:13px}}.k-ai-h span{{font-size:11px;background:var(--surface);color:var(--ai);border-radius:99px;padding:2px 8px}}.k-ai.abst{{background:var(--warn-100)}}.k-ai.abst .k-ai-h span{{color:var(--warn)}}
.k-timer{{font:700 15px var(--sans);font-variant-numeric:tabular-nums;color:var(--v-ink-900);border:1.5px solid var(--line);background:var(--surface);border-radius:99px;padding:5px 12px}}
.k-grid{{display:grid;grid-template-columns:repeat(10,1fr);gap:4px;margin:12px 0 6px;max-width:340px}}.k-grid i{{aspect-ratio:1;border-radius:5px;background:var(--surface);border:1px solid var(--line);font:normal 9px var(--sans);display:grid;place-items:center;color:var(--subtle)}}.k-grid i.a{{background:var(--v-ink-700);border-color:var(--v-ink-700);color:#fff}}.k-grid i.m{{background:var(--v-acc-100);border-color:var(--v-acc-500)}}.k-grid i.c{{outline:2px solid var(--v-acc-500);outline-offset:1px;color:var(--v-ink-900);font-weight:700}}.k-grid i.b{{border:1.5px dashed var(--subtle)}}
.k-leg{{display:flex;gap:12px;flex-wrap:wrap;font-size:11.5px;color:var(--subtle)}}.k-leg span::before{{content:"";display:inline-block;width:10px;height:10px;border-radius:3px;margin-right:5px;vertical-align:-1px;background:var(--surface);border:1px solid var(--line)}}.k-leg .a::before{{background:var(--v-ink-700)}}.k-leg .m::before{{background:var(--v-acc-100);border-color:var(--v-acc-500)}}.k-leg .c::before{{border:2px solid var(--v-acc-500)}}.k-leg .b::before{{border:1.5px dashed var(--subtle)}}
.k-law{{background:var(--surface);border:1px solid var(--line);border-radius:16px;padding:14px;max-width:360px}}.k-law-h{{display:flex;gap:8px;align-items:center}}.k-law-h b{{font:600 19px var(--serif);color:var(--v-ink-900)}}.k-pill{{font-size:11px;font-weight:600;background:var(--v-ink-50);color:var(--v-ink-800);border-radius:99px;padding:3px 9px}}.k-law p{{margin:4px 0 6px;font-size:13.5px;color:var(--muted)}}.k-law small{{color:var(--subtle);font-size:12px}}.k-law-f{{display:flex;justify-content:space-between;align-items:center;margin-top:8px;font-size:12.5px;color:var(--subtle)}}.k-law-f b{{color:var(--v-ink-900)}}
.k-tabs{{display:grid;grid-template-columns:repeat(4,1fr);background:var(--surface);border:1px solid var(--line);border-radius:14px;padding:8px 6px;max-width:360px}}.k-tabs a{{display:grid;justify-items:center;gap:3px;font:600 11px var(--sans);color:var(--subtle);text-decoration:none}}.k-tabs svg{{width:24px;height:24px;stroke:currentColor;fill:none;stroke-width:1.8;stroke-linecap:round;stroke-linejoin:round}}.k-tabs a.on{{color:var(--v-ink-800)}}.k-tabs a.on .acc{{stroke:var(--v-acc-500)}}
.k-dot{{width:40px;height:40px;border-radius:50%;display:grid;place-items:center;font-weight:700;font-size:13px;background:var(--surface);border:2px solid var(--v-ink-100);color:var(--v-ink-600)}}.k-dot.done{{background:var(--v-ink-800);border-color:var(--v-ink-800);color:#fff}}.k-dot.now{{background:var(--v-acc-500);border-color:var(--v-acc-600);color:#fff;font-size:19px;box-shadow:0 0 0 5px var(--v-acc-100)}}.k-dot.lock{{background:var(--paper-2);border-color:var(--line);color:var(--muted)}}.k-stat{{font-size:12px;color:var(--subtle)}}.k-stat b{{font:600 18px var(--serif);color:var(--v-ink-800)}}
.k-foot{{font-size:12px;color:var(--subtle);text-align:center;border-top:1px solid var(--line);padding-top:10px}}
.k-sw{{display:inline-grid;place-items:center;width:44px;height:30px;border-radius:8px;font:700 15px var(--sans);border:1px solid #0000001a}}.k-cr td.num{{font-variant-numeric:tabular-nums;font-weight:700}}.k-cr td{{vertical-align:middle}}.no-list li{{margin-bottom:4px}}
@media screen and (max-width:900px){{.sws.s5{{grid-template-columns:1fr 1fr}}.icg{{grid-template-columns:repeat(4,1fr)}}}}
'''
cover = horiz(NAME, P['paper'], REV, P['paper'])[0]
HTML = f'''<!doctype html><html lang="es" data-vertical="justicia"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Aula Justicia · Manual de vertical · Atrio v2</title><link rel="icon" href="icons/favicon-justicia.svg"><meta property="og:image" content="icons/aula-justicia-og-1200x630.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,500;0,8..60,600;0,8..60,700;1,8..60,500&display=swap" rel="stylesheet">
<style>{CSS}</style></head><body>
<nav class="top"><span class="lg">{cover}</span>{nav}<a href="{UMB_URL}">↑ Paraguas Aula</a><a href="#archivos">Archivos</a></nav>
<div class="wrap"><header class="cover"><div class="cl">{cover}</div><svg class="bigarch" viewBox="0 0 38 40">{arch(P['paper'],REV)}</svg>
<h1>Manual de marca de la vertical</h1><p class="tg" style="color:{REV}">«Estudia como se examina.»</p>
<p>Aula Justicia prepara las oposiciones a los cuerpos generales de la Administración de Justicia: <b>Gestión Procesal y Administrativa</b>, <b>Tramitación Procesal y Administrativa</b> y <b>Auxilio Judicial</b>. Este anexo aplica el sistema Atrio a la vertical; lo común está en el <a style="color:{REV}" href="{UMB_URL}">manual paraguas</a>.</p>
<div class="vlist"><span><i style="background:{INK};border:2px solid {REV}"></i>Azul toga {INK}</span><span><i style="background:{ACC}"></i>Ámbar {ACC}</span><span>Bloqueados · v2.0 · 31 oct 2026</span></div>
<p class="meta" style="margin-top:28px">Vertical de la línea Aula · Dirección Atrio · Uso interno</p></header>
{''.join(secs)}
<section id="archivos"><p class="kicker">Anexo · Archivos</p><h2>Descargas</h2><p class="lead">Logotipos con texto en trazados. PDF: <a href="aula-justicia-brandbook-v2.pdf">aula-justicia-brandbook-v2.pdf</a> · ZIP: <a href="aula-justicia-brandbook-v2.zip">aula-justicia-brandbook-v2.zip</a> · Paraguas: <a href="{UMB_URL}">Aula · Atrio v1</a>.</p><ul class="files">{files}</ul></section>
<p class="foot">Aula Justicia · Manual de vertical v2.0 · bajo Aula · Atrio v1 · Aula no está vinculada al Ministerio de Justicia ni al CGPJ.</p></div></body></html>'''
open(os.path.join(OUT, "index.html"), "w").write(HTML); print("html", len(HTML), "assets", len(assets))
