# Aula · Manual de marca paraguas v1 · Dirección C · Atrio  — generator
# Requires static instances in /tmp/fonts (serif600.ttf = Source Serif 4 wght600 opsz36, inter500.ttf = Inter wght500 opsz28) made with fontTools.varLib.instancer from Google Fonts variable TTFs.
import os, json, html
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
OUT = os.path.dirname(os.path.abspath(__file__)); FD = "/tmp/fonts"
FONTS = {"serif": TTFont(f"{FD}/serif600.ttf"), "sans": TTFont(f"{FD}/inter500.ttf")}

def text_path(txt, font, size, x=0, y=0, anchor="start", tracking=0):
    f = FONTS[font]; gs = f.getGlyphSet(); cmap = f.getBestCmap(); upm = f['head'].unitsPerEm; sc = size/upm
    hm = f['hmtx']; names = [cmap[ord(ch)] for ch in txt]
    w = sum(hm[n][0] for n in names)*sc + tracking*(len(txt)-1)
    if anchor == "middle": x -= w/2
    pen = SVGPathPen(gs, ntos=lambda v: ("%.2f" % v).rstrip("0").rstrip(".")); cx = x
    for n in names:
        tp = TransformPen(pen, (sc, 0, 0, -sc, cx, y)); gs[n].draw(tp); cx += hm[n][0]*sc + tracking
    return pen.getCommands(), w

# ---------- colour system ----------
def hx(h): h=h.lstrip('#'); return tuple(int(h[i:i+2],16) for i in (0,2,4))
def mix(a,b,t): A,B=hx(a),hx(b); return '#%02X%02X%02X'%tuple(round(A[i]+(B[i]-A[i])*t) for i in range(3))
def lum(h):
    c=[v/255 for v in hx(h)]; c=[v/12.92 if v<=.03928 else ((v+.055)/1.055)**2.4 for v in c]; return .2126*c[0]+.7152*c[1]+.0722*c[2]
def cr(a,b): la,lb=sorted([lum(a),lum(b)],reverse=True); return (la+.05)/(lb+.05)

P = dict(ink="#17242B", ink2="#2A3A42", paper="#F6F1E8", paper2="#EFE8DB", surface="#FFFDF8", line="#E3D9C8",
         text="#1B2427", muted="#56615F", subtle="#6E7775", gold="#C49A45", gold_rev="#D8B46A", gold100="#F5EBD3",
         ok="#2D6B4C", ok100="#DFEEE4", err="#9A3B28", err100="#F6E0D8", warn="#8A5A12", warn100="#F7EBCF", ai="#4B3F8F", ai100="#E9E6F7")
# name, slug, sector line, ink, accent, accent on dark, tinted bg, status
V = [("Museos","museos","Ayudantes de Museos del Estado","#15393F","#C0643F","#E08A63","#F6F1E8","Bloqueado · hereda Aula Museos v1"),
     ("Justicia","justicia","Tramitación · Auxilio · Gestión","#14304D","#B07A2A","#D9A24E","#EEF2F7","Bloqueado · manual propio pendiente"),
     ("Policía","policia","Escala Básica · Policía Nacional","#1F2F45","#3F6FB0","#7FA6DB","#EEF1F6","Provisional"),
     ("Administración","administracion","Cuerpos generales AGE · C1/C2","#24473B","#7E9A3A","#A9C46A","#EFF3EE","Provisional")]
def scale(ink, acc, bg):
    return {"ink-900":mix(ink,"#000000",.25),"ink-800":ink,"ink-700":mix(ink,"#FFFFFF",.14),"ink-600":mix(ink,"#FFFFFF",.28),
            "ink-100":mix(ink,"#FFFFFF",.86),"ink-50":mix(ink,"#FFFFFF",.93),"acc-600":mix(acc,"#000000",.14),"acc-500":acc,"acc-100":mix(acc,"#FFFFFF",.84),"bg":bg}

# ---------- marks ----------
def arch(c, base, sw=(3.2,2.2,3.2)):
    return (f'<g fill="none" stroke-linecap="round"><path d="M4 34V16a14 14 0 0 1 28 0v18" stroke="{c}" stroke-width="{sw[0]}"/>'
            f'<path d="M11 34V18a7 7 0 0 1 14 0v16" stroke="{c}" stroke-width="{sw[1]}"/><path d="M1 36.5h34" stroke="{base}" stroke-width="{sw[2]}"/></g>')
# symbol bbox in local units: x -0.6..36.6, y 0.4..38.1  -> ~37.2 x 37.7
SYM_W, SYM_H = 37.2, 37.7

def svg(w, h, body, label, bg=None, extra=""):
    b = f'<rect width="{w:.1f}" height="{h:.1f}" fill="{bg}"/>' if bg else ''
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w:.1f} {h:.1f}" width="{w:.0f}" height="{h:.0f}" role="img" aria-label="{label}"{extra}>{b}{body}</svg>'

def symbol_svg(c, base, bg=None, pad=0):
    w, h = SYM_W+2*pad, SYM_H+2*pad
    return svg(w, h, f'<g transform="translate({pad+0.6:.2f},{pad-0.4:.2f})">{arch(c,base)}</g>', "Aula · símbolo", bg)

def horiz(vname=None, c=P['ink'], base=P['gold'], sc=None, bg=None, pad=0):
    """Primary horizontal lockup. Grid: symbol scaled 1.35; 'Aula' Source Serif 4 600 @38; vertical Inter 500 @30."""
    sc = sc or c; s = 1.35
    d, wa = text_path("Aula", "serif", 38, 0, 0)
    tx = SYM_W*s + 12  # gap = 12 u
    base_y = 49.5      # text baseline aligned to visual mid of arch legs
    body = f'<g transform="translate({pad+0.6*s:.2f},{pad+(-0.4*s)+0.5:.2f}) scale({s})">{arch(c,base)}</g>'
    body += f'<path transform="translate({pad+tx:.2f},{pad+base_y})" d="{d}" fill="{c}"/>'
    w = tx + wa
    if vname:
        dv, wv = text_path(vname, "sans", 30, 0, 0, tracking=-.3)
        vx = w + 11
        body += f'<path transform="translate({pad+vx:.2f},{pad+base_y})" d="{dv}" fill="{sc}"/>'
        w = vx + wv
    h = SYM_H*s + 1
    return svg(w+2*pad, h+2*pad, body, f"Aula {vname or ''}".strip(), bg), (w, h)

def stacked(vname=None, c=P['ink'], base=P['gold'], sc=None, sector=None, bg=None, pad=0):
    sc = sc or base; s = 1.6
    d, wa = text_path("Aula", "serif", 40, 0, 0)
    items = [wa, SYM_W*s]
    if vname: dv, wv = text_path(vname, "sans", 26, 0, 0, tracking=-.2); items.append(wv)
    if sector: ds, wsct = text_path(sector.upper(), "sans", 9, 0, 0, tracking=1.6); items.append(wsct)
    W = max(items); cx = W/2
    body = f'<g transform="translate({pad+cx-SYM_W*s/2+0.6*s:.2f},{pad-0.4*s:.2f}) scale({s})">{arch(c,base)}</g>'
    y = SYM_H*s + 40
    body += f'<path transform="translate({pad+cx-wa/2:.2f},{pad+y:.2f})" d="{d}" fill="{c}"/>'
    if vname: y += 34; body += f'<path transform="translate({pad+cx-wv/2:.2f},{pad+y:.2f})" d="{dv}" fill="{sc}"/>'
    if sector: y += 22; body += f'<path transform="translate({pad+cx-wsct/2:.2f},{pad+y:.2f})" d="{ds}" fill="{c}" opacity=".62"/>'
    H = y + 8
    return svg(W+2*pad, H+2*pad, body, f"Aula {vname or ''}".strip(), bg), (W, H)

def app_icon(bg, c, base, size=1024, rx=.2237):
    k = size/64
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="{size}" height="{size}" role="img" aria-label="Icono Aula">'
            f'<rect width="64" height="64" rx="{64*rx:.2f}" fill="{bg}"/><g transform="translate(14.4,12.6) scale(.98)">{arch(c,base)}</g></svg>')
def app_icon_full(bg, c, base):  # store version (no rounding; OS masks)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="1024" height="1024"><rect width="64" height="64" fill="{bg}"/>'
            f'<g transform="translate(14.4,12.6) scale(.98)">{arch(c,base)}</g></svg>')

# ---------- write logo assets ----------
assets = []
def save(name, content, folder="logos"):
    p = os.path.join(OUT, folder, name); open(p, "w").write(content); assets.append(f"{folder}/{name}")
save("aula-symbol.svg", symbol_svg(P['ink'], P['gold']))
save("aula-symbol-reverse.svg", symbol_svg(P['paper'], P['gold_rev'], P['ink'], 8))
save("aula-symbol-mono-black.svg", symbol_svg(P['ink'], P['ink']))
save("aula-symbol-mono-white.svg", symbol_svg("#FFFFFF", "#FFFFFF"))
save("aula-primary.svg", horiz()[0])
save("aula-primary-reverse.svg", horiz(c=P['paper'], base=P['gold_rev'], bg=P['ink'], pad=24)[0])
save("aula-primary-mono-black.svg", horiz(c=P['ink'], base=P['ink'])[0])
save("aula-primary-mono-white.svg", horiz(c="#FFFFFF", base="#FFFFFF")[0])
save("aula-stacked.svg", stacked(sc=P['gold'])[0])
save("aula-stacked-reverse.svg", stacked(c=P['paper'], base=P['gold_rev'], bg=P['ink'], pad=24)[0])
d_tag, w_tag = text_path("Estudia como se examina.", "serif", 20, 0, 0)
hz, (hw, hh) = horiz()
save("aula-tagline.svg", svg(max(hw, w_tag), hh+40, hz.replace('<svg', '<svg x="0" y="0"', 1) + f'<path transform="translate(1,{hh+32})" d="{d_tag}" fill="{P["muted"]}"/>', "Aula · Estudia como se examina."))
for n, slug, sector, ink, acc, rev, bg, st in V:
    save(f"aula-{slug}-primary.svg", horiz(n, ink, acc, ink)[0])
    save(f"aula-{slug}-primary-reverse.svg", horiz(n, P['paper'], rev, P['paper'], bg=ink, pad=24)[0])
    save(f"aula-{slug}-primary-mono-black.svg", horiz(n, P['ink'], P['ink'], P['ink'])[0])
    save(f"aula-{slug}-stacked.svg", stacked(n, ink, acc, mix(acc,"#000000",.14), sector)[0])
    save(f"aula-{slug}-stacked-reverse.svg", stacked(n, P['paper'], rev, rev, sector, bg=ink, pad=24)[0])
    save(f"icon-{slug}-1024.svg", app_icon_full(ink, P['paper'], rev), "icons")
save("icon-aula-1024.svg", app_icon_full(P['ink'], P['paper'], P['gold_rev']), "icons")
save("favicon.svg", app_icon(P['ink'], P['paper'], P['gold_rev'], 32), "icons")

# ---------- tokens ----------
tok = {"platform": P, "radius": {"r-sm":"10px","r-md":"16px","r-lg":"22px","r-pill":"999px"},
       "space": {"s-1":"4px","s-2":"8px","s-3":"12px","s-4":"16px","s-5":"24px","s-6":"32px","s-7":"48px"},
       "type": {"serif":"'Source Serif 4','Iowan Old Style',Georgia,serif","sans":"Inter,system-ui,-apple-system,'Segoe UI',Roboto,sans-serif"},
       "verticals": {slug: dict(name=n, status=st, accent_on_dark=rev, **scale(ink,acc,bg)) for n,slug,s,ink,acc,rev,bg,st in V}}
tok["verticals"]["aula"] = dict(name="Aula (paraguas)", status="Bloqueado", accent_on_dark=P['gold_rev'], **scale(P['ink'], P['gold'], P['paper']))
json.dump(tok, open(os.path.join(OUT, "aula-tokens.json"), "w"), ensure_ascii=False, indent=2); assets.append("aula-tokens.json")
css = [":root{"] + [f"  --{k.replace('_','-')}:{v};" for k,v in P.items()] + [f"  --{k}:{v};" for k,v in tok['radius'].items()] + \
      [f"  --{k}:{v};" for k,v in tok['space'].items()] + [f"  --serif:{tok['type']['serif']};", f"  --sans:{tok['type']['sans']};",
      "  --sh-1:0 1px 2px rgba(23,36,43,.06),0 2px 8px rgba(23,36,43,.05);", "  --focus:0 0 0 3px var(--gold);"] + \
      [f"  --v-{k}:{v};" for k,v in scale(P['ink'],P['gold'],P['paper']).items()] + [f"  --v-acc-dark:{P['gold_rev']};", "}"]
for n,slug,s,ink,acc,rev,bg,st in V:
    css.append(f'[data-vertical="{slug}"]{{ /* {n} · {st} */')
    css += [f"  --v-{k}:{v};" for k,v in scale(ink,acc,bg).items()] + [f"  --v-acc-dark:{rev};", "}"]
CSS_TOKENS = "\n".join(css)
open(os.path.join(OUT, "aula-tokens.css"), "w").write(CSS_TOKENS + "\n"); assets.append("aula-tokens.css")
json.dump(assets, open("/tmp/aula_assets.json","w"))
print("assets", len(assets))

# =================== HTML BOOK ===================
def rd(p): return open(os.path.join(OUT, p)).read()
E = html.escape
def swatch(hexv, name, role, token):
    fg = "#FFFFFF" if lum(hexv) < .35 else P['text']
    return (f'<div class="sw"><div class="chipc" style="background:{hexv};color:{fg}"><span>{cr(hexv,"#FFFFFF"):.1f}:1 ⬜ · {cr(hexv,P["ink"]):.1f}:1 ⬛</span></div>'
            f'<b>{name}</b><code>{hexv}</code><code class="t">--{token}</code><small>{role}</small></div>')

SEC = []
def section(num, sid, kicker, title, body):
    SEC.append((num, sid, kicker)); return f'<section id="{sid}"><p class="kicker">{num} · {kicker}</p><h2>{title}</h2>{body}</section>'

# ---- 1 logo system
hz_svg = horiz()[0]
s1 = f'''<p class="lead">El símbolo es un <b>arco doble sobre un basamento</b>: el aula (arco exterior), el método (arco interior) y la base firme de la convocatoria (basamento). Es la evolución del arco de Aula Museos, que asciende a símbolo de toda la línea. El basamento es la única parte que cambia de color: lleva el acento de cada vertical.</p>
<div class="g2">
 <figure class="panel big">{hz_svg}<figcaption>Logotipo principal (horizontal) · <a href="logos/aula-primary.svg">SVG</a></figcaption></figure>
 <figure class="panel big">{rd("logos/aula-stacked.svg")}<figcaption>Logotipo apilado · <a href="logos/aula-stacked.svg">SVG</a></figcaption></figure>
</div>
<div class="g4">
 <figure class="panel">{rd("logos/aula-symbol.svg")}<figcaption>Símbolo · <a href="logos/aula-symbol.svg">SVG</a></figcaption></figure>
 <figure class="panel dark">{rd("logos/aula-primary-reverse.svg")}<figcaption>Inverso (sobre tinta) · <a href="logos/aula-primary-reverse.svg">SVG</a></figcaption></figure>
 <figure class="panel">{rd("logos/aula-primary-mono-black.svg")}<figcaption>Monocromo negro · <a href="logos/aula-primary-mono-black.svg">SVG</a></figcaption></figure>
 <figure class="panel" style="background:#8A6A2E">{rd("logos/aula-primary-mono-white.svg")}<figcaption style="color:#fff">Monocromo blanco (fotos, fondos de color) · <a style="color:#fff" href="logos/aula-primary-mono-white.svg">SVG</a></figcaption></figure>
</div>
<h3>Anatomía y construcción</h3>
<div class="g2">
 <div class="panel"><svg viewBox="-30 -26 330 112" width="100%" role="img" aria-label="Área de respeto">
  <rect x="-20.6" y="-17.4" width="291" height="86.6" fill="none" stroke="#C49A45" stroke-dasharray="4 3" stroke-width=".8"/>
  <rect x="0" y="0" width="{horiz()[1][0]:.1f}" height="{horiz()[1][1]:.1f}" fill="#C49A4514"/>
  {hz_svg.replace('<svg', '<svg x="0" y="0"',1)}
  <g font-family="Inter" font-size="7" fill="#8A5A12"><text x="-27" y="28">x</text><text x="125" y="-20">x</text><text x="125" y="80">x</text><text x="276" y="28">x</text></g>
  <path d="M-20.6 -21h20.6" stroke="#8A5A12" stroke-width=".8"/>
 </svg><p class="note"><b>Área de respeto = x</b>, donde x es el ancho del arco interior (≈ 0,4 × altura del símbolo). Ningún texto, borde o imagen entra en ese margen.</p></div>
 <div class="panel"><table class="t"><tr><th>Elemento</th><th>Regla</th></tr>
  <tr><td>Proporción</td><td>Símbolo : «Aula» : vertical = 1,35 : 38 pt : 30 pt (artes finales en <code>logos/</code>; no recomponer a mano)</td></tr>
  <tr><td>«Aula»</td><td>Source Serif 4 Semibold (600, opsz 36), convertida a trazados</td></tr>
  <tr><td>Vertical</td><td>Inter Medium (500), tracking −1 %, en la tinta de la vertical</td></tr>
  <tr><td>Alineación</td><td>La línea base de «Aula» se apoya en el basamento</td></tr>
  <tr><td>Trazos</td><td>Arco exterior 3,2 · interior 2,2 · basamento 3,2 (sobre 36 u), terminales redondeados</td></tr>
  <tr><td>Tamaño mínimo</td><td>Horizontal 96 px / 24 mm · Apilado 64 px / 16 mm · Símbolo 16 px / 5 mm. Por debajo de 24 px el símbolo usa versión «favicon» (trazos +15 %)</td></tr>
 </table></div>
</div>
<h3>Sí / No</h3>
<div class="g4 dd">
 <figure class="panel ok">{horiz(c=P['ink'], base=P['gold'])[0]}<figcaption>✓ Tinta + oro sobre papel</figcaption></figure>
 <figure class="panel ok" style="background:#14304D">{horiz("Justicia", P['paper'], "#D9A24E", P['paper'])[0]}<figcaption style="color:#fff">✓ Inverso de vertical: papel + acento claro</figcaption></figure>
 <figure class="panel no">{horiz(c="#C0643F", base="#14304D")[0]}<figcaption>✗ Mezclar colores de dos verticales</figcaption></figure>
 <figure class="panel no"><div style="transform:scale(1.25,.8) skewX(-12deg);transform-origin:left;width:200px">{horiz()[0]}</div><figcaption>✗ Deformar, estirar o inclinar</figcaption></figure>
 <figure class="panel no"><div style="font:700 40px/1 Impact,'Arial Black',sans-serif;color:#17242B;display:flex;gap:10px;align-items:flex-end"><span style="width:48px;display:inline-block">{symbol_svg(P['ink'],P['gold']).replace('width="37" height="38"','width="48" height="49"')}</span><span>AULA</span></div><figcaption>✗ Cambiar la tipografía de «Aula»</figcaption></figure>
 <figure class="panel no"><div style="filter:drop-shadow(3px 4px 2px #0006)">{horiz()[0]}</div><figcaption>✗ Sombras, biseles, degradados</figcaption></figure>
 <figure class="panel no" style="background:#C49A45">{horiz()[0]}<figcaption>✗ Poco contraste (tinta sobre oro)</figcaption></figure>
 <figure class="panel no">{horiz("Museos · Justicia", P['ink'], P['gold'])[0]}<figcaption>✗ Dos verticales en un mismo logotipo</figcaption></figure>
</div>'''

# ---- 2 palette
pal = ''.join([swatch(P['ink'],"Tinta Atrio","logotipo, titulares, botón primario paraguas","ink"), swatch(P['paper'],"Papel","fondo de página","paper"),
  swatch(P['surface'],"Superficie","tarjetas, opciones","surface"), swatch(P['paper2'],"Papel 2","bandas, zonas secundarias","paper-2"),
  swatch(P['line'],"Línea","bordes y filetes","line"), swatch(P['gold'],"Oro pátina","basamento paraguas, foco, sello","gold"),
  swatch(P['text'],"Texto","cuerpo de texto","text"), swatch(P['muted'],"Texto suave","metadatos","muted")])
sem = ''.join([swatch(P['ok'],"Acierto","+1, correcto","ok"), swatch(P['err'],"Error","−1/3, incorrecto (nunca rojo alarma)","err"),
  swatch(P['subtle'],"En blanco","0, sin responder","subtle"), swatch(P['warn'],"Aviso","fuente insuficiente, provisional","warn"),
  swatch(P['ai'],"Violeta IA","solo Contenido IA","ai")])
vrows = ""
for n,slug,sector,ink,acc,rev,bg,st in V:
    sc_ = scale(ink,acc,bg); prov = ' prov' if st=="Provisional" else ''
    chips = ''.join(f'<div class="mini-sw" style="background:{sc_[k]}" title="{k} {sc_[k]}"><small style="color:{"#fff" if lum(sc_[k])<.35 else P["text"]}">{k}<br>{sc_[k]}</small></div>' for k in ["ink-900","ink-800","ink-700","ink-600","ink-100","ink-50","acc-600","acc-500","acc-100"])
    vrows += f'<div class="vpal{prov}"><div class="vh"><b>Aula {n}</b><span class="badge{prov}">{st}</span><small>{sector}</small></div><div class="ms">{chips}<div class="mini-sw" style="background:{rev}"><small>acc-dark<br>{rev}</small></div><div class="mini-sw" style="background:{bg};border:1px solid #0001"><small>bg<br>{bg}</small></div></div></div>'
s2 = f'''<p class="lead">Una paleta de plataforma cálida y sobria, común a todas las verticales, y <b>un par de colores por vertical</b> (tinta + acento) que se enchufa mediante tokens <code>--v-*</code>. Los colores de estado (acierto, error, IA) son de plataforma: nunca cambian entre verticales.</p>
<h3>Plataforma</h3><div class="sws">{pal}</div>
<h3>Estados y semántica (comunes)</h3><div class="sws">{sem}</div>
<h3>Cómo se enchufa una vertical</h3>
<div class="g2"><div class="panel"><ol class="steps"><li>Elegir <b>tinta</b> (oscura, contraste ≥ 10:1 con papel) y <b>acento</b> (≥ 3:1 con papel; texto pequeño en <code>acc-600</code>).</li>
<li>Generar la escala automáticamente (<code>build.py → scale()</code>): ink-900…50, acc-600/500/100, acc-dark para fondos oscuros.</li>
<li>Declarar <code>[data-vertical="slug"]</code> en <code>aula-tokens.css</code>. Ningún componente usa hex directos.</li>
<li>Regla de oro: <b>una vertical por pantalla</b>; el oro Atrio solo aparece en lo que es de Aula (paraguas, foco, sello de logro).</li></ol></div>
<div class="panel"><table class="t"><tr><th>Token</th><th>Uso</th></tr><tr><td><code>--v-ink-800</code></td><td>logotipo, botón primario, cabecera</td></tr><tr><td><code>--v-ink-50/100</code></td><td>fondos de selección, progreso</td></tr><tr><td><code>--v-acc-500</code></td><td>basamento, barra de progreso, racha</td></tr><tr><td><code>--v-acc-600</code></td><td>texto de acento ≤ 18 px</td></tr><tr><td><code>--v-acc-dark</code></td><td>basamento en inverso / icono</td></tr><tr><td><code>--v-bg</code></td><td>fondo de app de la vertical</td></tr></table></div></div>
<div class="vpals">{vrows}</div>
<p class="note"><b>Policía y Administración son provisionales</b> (marcados con trama): validar con el equipo de cada vertical antes de lanzar. Museos y Justicia quedan bloqueados.</p>'''

# ---- 3 typography
TS = [("Display","serif",600,44,52,"-0.5px","Aula, para cada convocatoria"),("H1","serif",600,32,40,"-0.3px","Tema 7 · Patrimonio Histórico"),
      ("H2","serif",600,24,32,"0","Resultado del simulacro"),("Enunciado","serif",500,20,28,"0","¿Qué órgano es el gobierno del Poder Judicial?"),
      ("Cuerpo","sans",400,16,24,"0","La explicación cita norma, artículo y fecha de publicación."),("Etiqueta UI","sans",500,14,20,"0","Continuar · Revisar · Entregar"),
      ("Pie / fuente","sans",500,12,16,"0","BOE-A-1978-31229 · art. 122.2"),("Sobretítulo","sans",700,11,16,"1.4px","CONTENIDO IA · CON FUENTE"),("Cifras","sans",600,28,32,"0","26,00 / 40")]
trows = ''.join(f'<tr><td><b>{a}</b><br><small>{"Source Serif 4" if f=="serif" else "Inter"} {w} · {sz}/{lh}</small></td><td><span style="font-family:var(--{f});font-weight:{w};font-size:{sz}px;line-height:{lh}px;letter-spacing:{ls};{"font-variant-numeric:tabular-nums;" if a=="Cifras" else ""}">{t}</span></td></tr>' for a,f,w,sz,lh,ls,t in TS)
s3 = f'''<p class="lead"><b>Serif para el saber, sans para la herramienta.</b> Source Serif 4 da voz a la marca y al contenido de estudio (titulares, enunciados); Inter resuelve la interfaz, las cifras y el nombre de la vertical. Es el mismo par que Aula Museos v1 y la app web v0.1. Ambas son libres (SIL OFL) vía Google Fonts.</p>
<div class="g2"><div class="panel tspec"><p style="font-family:var(--serif);font-weight:600;font-size:64px;line-height:1;margin:0">Aa</p><p><b>Source Serif 4</b> · 400 / 500 / 600 / 700, cursiva 500 · opsz automático</p><p style="font-family:var(--serif);font-size:18px">ABCDEFGHIJKLMNÑOPQRSTUVWXYZ<br>abcdefghijklmnñopqrstuvwxyz áéíóúü ¿? ¡! «» 0123456789 § ª º</p></div>
<div class="panel tspec"><p style="font-family:var(--sans);font-weight:500;font-size:64px;line-height:1;margin:0">Aa</p><p><b>Inter</b> · 400 / 500 / 600 / 700 · cifras tabulares en puntuaciones</p><p style="font-family:var(--sans);font-size:17px">ABCDEFGHIJKLMNÑOPQRSTUVWXYZ<br>abcdefghijklmnñopqrstuvwxyz áéíóúü ¿? ¡! «» 0123456789 +1 0 −1/3</p></div></div>
<h3>Escala y roles</h3><table class="t ts">{trows}</table>
<p class="note">Reglas: enunciados siempre en serif; opciones de respuesta, botones y cifras en Inter. Usar el signo menos real «−» (U+2212) en «−1/3». Comillas latinas «» en textos de marca. Mínimo 14 px para texto funcional en móvil.</p>'''

# ---- 4 voice
VO = [("Bienvenida","«Buenas tardes, Lucía. Hoy toca el Tema 4: unos 10 minutos.»","«¡¡Hola crack!! ¿Lista para petarlo? 🚀»"),
      ("Acierto","«Correcto. El art. 122.2 CE define al CGPJ como órgano de gobierno del Poder Judicial.»","«¡Increíble! ¡Eres un genio!»"),
      ("Error","«No es esta. La clave está en el art. 122.2: lo vemos en 30 segundos.»","«¡Mal! Has perdido una vida.»"),
      ("Examen","«Nota orientativa: 26,00 / 40 (+1 · 0 · −1/3). No es una calificación oficial.»","«¡Aprobado seguro!»"),
      ("Contenido IA","«Explicación generada con IA · Fuente: BOE-A-1978-31229, art. 122.2.»","Explicaciones sin fuente o presentadas como doctrina oficial."),
      ("Sin fuente","«No tengo una fuente suficiente para explicarlo. Revisa el artículo en el temario oficial.»","Inventar una respuesta «plausible»."),
      ("Error técnico","«No hemos podido guardar tu examen. Tus respuestas siguen aquí; vuelve a intentarlo.»","«Ups 🙈 algo salió mal.»"),
      ("Racha","«Llevas 12 días seguidos. Hoy puedes descansar sin perderla.»","«¡Tu racha va a MORIR si no estudias YA!»")]
vrows_ = ''.join(f'<tr><td><b>{a}</b></td><td class="yes">{b}</td><td class="nop">{c}</td></tr>' for a,b,c in VO)
s4 = f'''<p class="lead">Aula habla como <b>un buen preparador de oposiciones</b>: sereno, exacto y cercano sin ser informal. Oficial en los datos, humano en el ánimo. Español de España, tuteo respetuoso (en comunicaciones institucionales o a terceros: usted).</p>
<div class="taghero"><p class="tagline">«Estudia como se examina.»</p><p class="note">Lema de la línea. Alternativas aprobables: «Del temario a la plaza, cada día.» · «Tu oposición, pregunta a pregunta.» · Por vertical: «Aula Justicia. Estudia como se examina.»</p></div>
<div class="g4 pr"><div class="panel"><b>1 · Exacta</b><p>Cita norma, artículo y fecha. Si algo no está confirmado, lo dice.</p></div><div class="panel"><b>2 · Serena</b><p>Sin urgencias artificiales, mayúsculas ni exclamaciones en serie.</p></div><div class="panel"><b>3 · Cercana</b><p>Reconoce el esfuerzo con datos, no con euforia. Nunca infantiliza.</p></div><div class="panel"><b>4 · Transparente</b><p>Todo Contenido IA va etiquetado y con fuente; si no hay fuente, se abstiene.</p></div></div>
<table class="t voice"><tr><th>Situación</th><th>Sí</th><th>No</th></tr>{vrows_}</table>
<div class="g2"><div class="panel"><h4>Vocabulario de la línea</h4><p>opositor/a · convocatoria · temario · tema · prueba (práctica con feedback inmediato) · examen / simulacro (+1 · 0 · −1/3, feedback al final) · fuente oficial · «Mi aula» · «Continuar en el aula».</p></div>
<div class="panel"><h4>Evitar</h4><p>Prometer plaza o aprobado · comparar con otros opositores · emojis en contenido de estudio · jerga gamer (vidas, boss, nivel épico) · «academia» · nombres de organismos oficiales como si fuéramos ellos (Aula no es una web del Ministerio).</p></div></div>'''

# ---- 5 vertical lockups
lk = ""
for n,slug,sector,ink,acc,rev,bg,st in V:
    prov = ' <span class="badge prov">Provisional</span>' if st=="Provisional" else ''
    lk += f'''<div class="lkrow"><div class="lkh"><b>Aula {n}</b>{prov}<small>{sector} · tinta {ink} · acento {acc}</small></div>
<div class="lkg"><figure class="panel" style="background:{bg}">{rd(f"logos/aula-{slug}-primary.svg")}<figcaption><a href="logos/aula-{slug}-primary.svg">horizontal</a></figcaption></figure>
<figure class="panel" style="background:{ink}">{rd(f"logos/aula-{slug}-primary-reverse.svg")}<figcaption style="color:#fff"><a style="color:#fff" href="logos/aula-{slug}-primary-reverse.svg">inverso</a></figcaption></figure>
<figure class="panel st" style="background:{bg}">{rd(f"logos/aula-{slug}-stacked.svg")}<figcaption><a href="logos/aula-{slug}-stacked.svg">apilado</a></figcaption></figure>
<figure class="panel st" style="background:{ink}">{rd(f"logos/aula-{slug}-stacked-reverse.svg")}<figcaption style="color:#fff"><a style="color:#fff" href="logos/aula-{slug}-stacked-reverse.svg">apilado inverso</a></figcaption></figure></div></div>'''
s5 = f'''<p class="lead">Fórmula fija: <b>[arco] Aula</b> (Source Serif 4) + <b>Vertical</b> (Inter Medium), mismo color de tinta; el acento de la vertical va solo en el basamento. En apilado, el nombre de la vertical toma el acento y se puede añadir la línea de cuerpos en versalitas.</p>
<div class="g3"><div class="panel"><b>Nomenclatura</b><p>Siempre «Aula» + nombre corto del ámbito, en singular y sin artículos: Aula Museos, Aula Justicia, Aula Policía, Aula Administración. Futuras: Aula Hacienda, Aula Correos, Aula Educación…</p></div>
<div class="panel"><b>Cuándo usar el paraguas</b><p>Web corporativa, selector de verticales, facturas, legal, prensa. Dentro de una app de vertical, solo el lockup de esa vertical.</p></div>
<div class="panel"><b>Nombre de cuerpo</b><p>La línea de sector (p. ej. «Tramitación · Auxilio · Gestión») es descriptiva, nunca forma parte del nombre de marca ni del icono.</p></div></div>
{lk}'''

# ---- 6 app icons
ic = f'<figure class="icn"><div class="ii">{app_icon(P["ink"],P["paper"],P["gold_rev"],120)}</div><figcaption><b>Aula</b><br><small>paraguas / selector</small><br><a href="icons/icon-aula-1024.svg">SVG 1024</a> · <a href="icons/icon-aula-1024.png">PNG</a></figcaption></figure>'
for n,slug,sector,ink,acc,rev,bg,st in V:
    ic += f'<figure class="icn"><div class="ii">{app_icon(ink,P["paper"],rev,120)}</div><figcaption><b>Aula {n}</b>{" <span class=\"badge prov\">prov.</span>" if st=="Provisional" else ""}<br><small>{ink} + {rev}</small><br><a href="icons/icon-{slug}-1024.svg">SVG 1024</a> · <a href="icons/icon-{slug}-1024.png">PNG</a></figcaption></figure>'
home = ''.join(f'<div class="hs"><div>{app_icon(ink,P["paper"],rev,60)}</div><small>Aula {n}</small></div>' for n,slug,sector,ink,acc,rev,bg,st in V)
sizes = ''.join(f'<div class="sz">{app_icon(V[1][3],P["paper"],V[1][5],px)}<small>{px}px</small></div>' for px in (120,60,40,29,20))
s6 = f'''<p class="lead">Un único dibujo para toda la línea: el arco en papel sobre la tinta de la vertical, con el basamento en el acento claro (<code>acc-dark</code>). Sin texto en el icono; el nombre lo pone el sistema («Aula Museos»).</p>
<div class="icons">{ic}</div>
<div class="g2"><div class="panel phonebg"><div class="hsg">{home}</div><p class="note" style="color:#fff">Pantalla de inicio: las verticales conviven y se distinguen por color.</p></div>
<div class="panel"><div class="szs">{sizes}</div><p class="note">Retícula 64 u · símbolo 36 u centrado ópticamente (14,4 / 12,6). iOS: entregar 1024 × 1024 sin esquinas (el sistema aplica la máscara). Android adaptive: zona segura 66 %; el símbolo cabe entero. Favicon: <a href="icons/favicon.svg">favicon.svg</a>.</p></div></div>'''

# ---- 7 UI tokens
def btn(label, kind): return f'<button class="b {kind}">{label}</button>'
s7 = f'''<p class="lead">Los componentes consumen solo tokens. Cambiar <code>data-vertical</code> en el <code>&lt;html&gt;</code> re-tematiza toda la app (abajo: misma pieza en Museos y en Justicia). Archivos: <a href="aula-tokens.css">aula-tokens.css</a> · <a href="aula-tokens.json">aula-tokens.json</a>.</p>
<div class="g2"><div class="panel"><h4>Radios y espacio</h4><div class="radii"><div style="border-radius:10px">r-sm 10<br><small>chips, inputs</small></div><div style="border-radius:16px">r-md 16<br><small>botones, opciones</small></div><div style="border-radius:22px">r-lg 22<br><small>tarjetas, hojas</small></div><div style="border-radius:999px">pill<br><small>etiquetas</small></div></div>
<p class="note">Espaciado base 4: 4 · 8 · 12 · 16 · 24 · 32 · 48. Objetivo táctil ≥ 44 px. Sombra única <code>--sh-1</code>. Foco: anillo 3 px oro Atrio (común a todas las verticales).</p></div>
<div class="panel"><h4>Tipografía en UI</h4><p class="note"><code>--serif</code> → H1/H2/enunciado · <code>--sans</code> → todo lo demás. Tamaños: 32 / 24 / 20 / 16 / 14 / 12 / 11. Cifras: <code>font-variant-numeric: tabular-nums</code>.</p></div></div>
<div class="g2 themes">
 <div class="panel" data-vertical="museos"><h4>Aula Museos</h4><div class="row">{btn("Continuar","pri")}{btn("Revisar","sec")}{btn("Ver fuente","ghost")}{btn("Entregar","pri dis")}</div>
  <div class="row"><span class="chip tema">Tema 7</span><span class="chip mode">Prueba</span><span class="chip mode ex">Examen</span><span class="chip ai">◆ Contenido IA</span><span class="chip src">Fuente oficial · BOE</span><span class="chip warn">Sin fuente suficiente</span></div>
  <div class="prog"><span style="width:62%"></span></div><small class="pl">Progreso 25/40 · racha 12 días</small></div>
 <div class="panel" data-vertical="justicia"><h4>Aula Justicia</h4><div class="row">{btn("Continuar","pri")}{btn("Revisar","sec")}{btn("Ver fuente","ghost")}{btn("Entregar","pri dis")}</div>
  <div class="row"><span class="chip tema">Tema 3</span><span class="chip mode">Prueba</span><span class="chip mode ex">Examen</span><span class="chip ai">◆ Contenido IA</span><span class="chip src">Fuente oficial · BOE</span><span class="chip warn">Sin fuente suficiente</span></div>
  <div class="prog"><span style="width:62%"></span></div><small class="pl">Progreso 25/40 · racha 12 días</small></div>
</div>
<h3>Estados de examen (+1 · 0 · −1/3)</h3>
<div class="g3 states">
 <div class="state ok"><b>+1</b><span>Acierto</span><small>borde y fondo --ok · icono ✓ · solo visible al entregar en examen; inmediato en prueba</small></div>
 <div class="state bl"><b>0</b><span>En blanco</span><small>borde discontinuo --subtle · «Dejar en blanco» siempre disponible, nunca penalizado</small></div>
 <div class="state er"><b>−1/3</b><span>Error</span><small>borde y fondo --err (teja, no rojo alarma) · explicación + fuente</small></div>
</div>
<h3>Opciones de respuesta</h3>
<div class="g4 opts" data-vertical="justicia"><div class="opt"><i>A</i>Por defecto</div><div class="opt sel"><i>B</i>Seleccionada (examen)</div><div class="opt okk"><i>✓</i>Correcta (revisión)</div><div class="opt err"><i>✗</i>Elegida y errónea</div></div>
<h3>Bloque Contenido IA (contrato RAG <code>/v0/explain</code>)</h3>
<div class="g2"><div class="aibox"><small class="ov">◆ CONTENIDO IA · CON FUENTE</small><p>El Consejo General del Poder Judicial es el órgano de gobierno del Poder Judicial; lo regula una ley orgánica.</p><a>BOE-A-1978-31229 · Constitución Española, art. 122.2</a><blockquote>«El Consejo General del Poder Judicial es el órgano de gobierno del mismo.»</blockquote><small class="lv">Nivel de fuente: Legislación</small></div>
<div class="aibox abst"><small class="ov">◆ CONTENIDO IA · SIN FUENTE SUFICIENTE</small><p>No tengo una fuente suficiente para explicar esta respuesta. Revisa el artículo en el temario oficial.</p><small class="lv">Se muestra <code>message_es</code> cuando <code>abstain = true</code>; nunca un texto «fundamentado».</small></div></div>
<details><summary>Ver aula-tokens.css</summary><pre>{E(CSS_TOKENS)}</pre></details>'''

# ---- 8 exam mock
def phone(vert, q, opts, sel, cite, quote, cnum, brand, review=False):
    def cls(i):
        if not review: return " sel" if i==sel else ""
        return " okk" if i==1 else (" err" if i==sel and sel!=1 else "")
    def mark(i):
        if review and i==1: return "✓"
        if review and i==sel: return "✗"
        return "ABCD"[i]
    oh = ''.join(f'<div class="opt{cls(i)}"><i>{mark(i)}</i>{o}</div>' for i,o in enumerate(opts))
    if review:
        chip = f'<span class="chip mode">Revisión · {cnum}/40</span>'; meta = '<span>Tu respuesta: C · <b class="r">−1/3</b></span><span>Tema 2</span>'
        extra = f'<div class="aibox sm"><small class="ov">◆ CONTENIDO IA · CON FUENTE</small><p>{quote}</p><a>{cite}</a></div>'
        btns = '<button class="b sec">Anterior</button><button class="b pri">Siguiente error</button>'
    else:
        chip = f'<span class="chip mode ex">Examen · {cnum}/40</span>'; meta = '<span>⏱ 31:20 restantes</span><span>Respondidas 24 · en blanco 3</span>'
        extra = '<p class="fm" style="text-align:left">Sin corrección hasta entregar. Acierto +1 · en blanco 0 · error −1/3.</p>'
        btns = '<button class="b sec">Dejar en blanco</button><button class="b pri">Siguiente</button>'
    return f'''<div class="phone" data-vertical="{vert}"><div class="scr">
<div class="ph-top"><span class="pbrand">{brand}</span>{chip}</div>
<div class="prog"><span style="width:{cnum/40*100:.0f}%"></span></div>
<div class="ph-meta">{meta}</div>
<p class="ph-q">{q}</p>{oh}{extra}
<div class="ph-b">{btns}</div></div></div>'''
def result(vert, brand):
    return f'''<div class="phone" data-vertical="{vert}"><div class="scr res">
<div class="ph-top"><span class="pbrand">{brand}</span><span class="chip mode ex">Simulacro entregado</span></div>
<p class="ov2">NOTA ORIENTATIVA</p><p class="big">26,00<small> / 40</small></p><p class="ten">6,50 sobre 10</p>
<div class="rgrid"><div class="state ok"><b>28</b><span>+1 aciertos</span></div><div class="state bl"><b>6</b><span>0 en blanco</span></div><div class="state er"><b>6</b><span>−2,00 errores</span></div></div>
<p class="fm">Neta = aciertos − errores ÷ 3 = 28 − 6 ÷ 3. No es una calificación oficial.</p>
<div class="seal"><svg viewBox="0 0 38 40" width="26">{arch("var(--gold)","var(--gold)")}</svg> Mejor nota de la semana · +2,3 sobre el anterior</div>
<div class="ph-b"><button class="b sec">Revisar errores</button><button class="b pri">Nuevo simulacro</button></div></div></div>'''
pj = '<span class="ps">Aula</span> <span class="pv">Justicia</span>'; pm = '<span class="ps">Aula</span> <span class="pv">Museos</span>'
s8 = f'''<p class="lead">Pantalla de examen y resultado en estilo Atrio. Mismo componente, dos verticales: solo cambia <code>data-vertical</code>. 1) examen en curso (sin feedback, «Dejar en blanco» siempre visible), 2) resultado con nota neta, 3) revisión: correcta en verde, elegida errónea en teja, explicación IA con fuente.</p>
<div class="phones">{phone("justicia","Según la Constitución, ¿qué órgano es el gobierno del Poder Judicial?",["El Tribunal Supremo","El Consejo General del Poder Judicial","El Ministerio de Justicia","El Tribunal Constitucional"],1,"BOE-A-1978-31229 · CE, art. 122.2","El CGPJ es el órgano de gobierno del Poder Judicial (art. 122.2 CE). El Tribunal Supremo es el órgano jurisdiccional superior (art. 123).",25,pj)}
{result("justicia",pj)}
{phone("museos","¿Qué norma regula el Patrimonio Histórico Español?",["Real Decreto 620/1987","Ley 16/1985, de 25 de junio","Ley 10/2007","Ley 23/1982"],2,"BOE-A-1985-12534 · Ley 16/1985, art. 1","La Ley 16/1985, de 25 de junio, es la norma básica del Patrimonio Histórico Español; la Ley 10/2007 regula la lectura, el libro y las bibliotecas.",7,pm,True)}</div>'''

# ---- 9 relationship
s9 = '''<div class="g2"><div class="panel"><h4>Qué se mantiene de Aula Museos v1 y la web v0.1</h4><ul>
<li>Par tipográfico Source Serif 4 + Inter, papel #F6F1E8, superficie, línea y textos.</li>
<li>Colores de Museos: tinta #15393F + terracota #C0643F (acento) — ahora tokens <code>--v-*</code> de la vertical Museos; el oro #C49A45 pasa a ser el oro de la plataforma.</li>
<li>Semántica: acierto #2D6B4C, error #9A3B28, violeta IA #4B3F8F; radios 10/16/22/pill; foco en oro.</li>
<li>Voz (preparadora precisa, serena, de tú), modos prueba / examen (+1 · 0 · −1/3), etiqueta Contenido IA siempre con fuente.</li>
<li>La app v0.1 (<a href="https://muratpod.github.io/polina-design/app/">/app/</a>) es conforme: solo requiere renombrar variables a <code>--v-*</code> y añadir <code>data-vertical="museos"</code>.</li></ul></div>
<div class="panel"><h4>Qué cambia</h4><ul>
<li>El símbolo de Museos (arco) se convierte en el símbolo Atrio de toda la línea: arco doble + basamento de color. Los logotipos y el monograma «AM» de Museos v1 quedan como históricos; usar <code>logos/aula-museos-*.svg</code> de este manual.</li>
<li>El nombre de la vertical va en Inter (antes serif): diferencia la marca común (serif) del ámbito (sans).</li>
<li>El manual de Museos v1 sigue válido para contenido propio de Museos (catalogación, fichas, jerarquía de fuentes); en logotipo, color de plataforma y tokens manda este manual.</li>
<li>Siguiente: manual de vertical Aula Justicia (navy #14304D + ámbar #B07A2A, bloqueados aquí).</li></ul></div></div>
<p class="note">Fuera de alcance: dominios, registro de marca (OEPM/EUIPO) y búsquedas de anterioridad — pendientes antes de uso comercial.</p>'''

secs = [section("01","logo","Logotipo","Símbolo Atrio y logotipo Aula",s1), section("02","color","Color","Paleta de plataforma y verticales",s2),
        section("03","tipo","Tipografía","Source Serif 4 + Inter",s3), section("04","voz","Voz y tono","Cómo habla Aula",s4),
        section("05","verticales","Verticales","Lockups de verticales",s5), section("06","iconos","Iconos de app","Un arco, cuatro colores",s6),
        section("07","tokens","UI tokens","Tokens y componentes",s7), section("08","examen","Pantalla de examen","Examen en estilo Atrio",s8),
        section("09","relacion","Relación","Museos v1 y web v0.1",s9)]
nav = ''.join(f'<a href="#{sid}">{num} {k}</a>' for num,sid,k in SEC)
files = ''.join(f'<li><a href="{a}">{a}</a></li>' for a in assets + ["icons/icon-aula-1024.png"] + [f"icons/icon-{v[1]}-1024.png" for v in V])

CSS = rd("aula-tokens.css") + r'''
*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;font-family:var(--sans);color:var(--text);background:var(--paper);line-height:1.5;font-size:15px}
a{color:var(--v-ink-700)}code{font-size:.88em;background:#17242B0d;padding:1px 5px;border-radius:5px}
.top{position:sticky;top:0;z-index:9;background:#17242Bf2;backdrop-filter:blur(6px);display:flex;gap:6px;align-items:center;padding:8px 22px;flex-wrap:wrap}
.top .lg{margin-right:auto;display:flex;align-items:center}.top .lg svg{height:26px;width:auto}.top a{color:#F6F1E8;text-decoration:none;font-size:12.5px;padding:5px 10px;border-radius:999px}.top a:hover{background:#ffffff1f}
.wrap{max-width:1160px;margin:0 auto;padding:0 28px 60px}
.cover{background:var(--ink);color:var(--paper);border-radius:0 0 28px 28px;padding:64px 56px 48px;margin:0 -28px 20px;position:relative;overflow:hidden}
.cover .cl svg{width:min(420px,80%);height:auto}.cover h1{font-family:var(--serif);font-weight:600;font-size:46px;letter-spacing:-.5px;margin:34px 0 4px}.cover p{color:#E9E1D2;max-width:720px}
.cover .tg{font-family:var(--serif);font-size:26px;color:var(--gold-rev);margin:6px 0 24px}.cover .meta{font-size:12.5px;letter-spacing:1.4px;text-transform:uppercase;color:#B9B19F}
.cover .vlist{display:flex;gap:10px;flex-wrap:wrap;margin-top:26px}.cover .vlist span{border:1px solid #ffffff2e;border-radius:999px;padding:5px 12px 5px 8px;font-size:13px;display:flex;gap:7px;align-items:center}.cover .vlist i{width:14px;height:14px;border-radius:4px;display:inline-block}
.cover .bigarch{position:absolute;right:-40px;bottom:-60px;width:380px;opacity:.09}
section{padding:46px 0 10px;border-top:1px solid var(--line);scroll-margin-top:50px}
.kicker{font-size:12px;letter-spacing:1.6px;text-transform:uppercase;color:#8A6A2E;font-weight:700;margin:0}
h2{font-family:var(--serif);font-weight:600;font-size:34px;letter-spacing:-.4px;margin:.15em 0 .4em;color:var(--ink)}
h3{font-family:var(--serif);font-weight:600;font-size:21px;margin:30px 0 12px;color:var(--ink)}h4{margin:0 0 8px;font-size:14px;color:var(--ink)}
.lead{font-size:17px;max-width:880px;color:#33403D}.note{font-size:13.5px;color:var(--muted);margin:10px 0 0}
.g2{display:grid;grid-template-columns:1fr 1fr;gap:16px}.g3{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}.g4{display:grid;grid-template-columns:repeat(4,1fr);gap:14px}
.panel{background:var(--surface);border:1px solid var(--line);border-radius:var(--r-lg);padding:18px 20px;margin:0}
figure.panel{display:flex;flex-direction:column;justify-content:center;align-items:flex-start;min-height:120px}figure svg{max-width:100%;height:auto}
figure.big{min-height:220px;align-items:center}figure.big svg{width:min(360px,90%)}figure.panel.big:nth-child(2) svg{width:auto;max-height:190px}
figcaption{font-size:12px;color:var(--subtle);margin-top:12px}.panel.dark{background:var(--ink)}.panel.dark figcaption,.panel.dark figcaption a{color:#E9E1D2}
.dd figure{min-height:110px}.dd svg{width:200px}.panel.ok{border:2px solid var(--ok)}.panel.no{border:2px solid var(--err);position:relative;overflow:hidden}.panel.no figcaption{color:var(--err);font-weight:600}.panel.ok figcaption{color:var(--ok);font-weight:600}
table.t{width:100%;border-collapse:collapse;font-size:13.5px;background:var(--surface);border-radius:14px;overflow:hidden}.t th,.t td{padding:9px 12px;border-bottom:1px solid var(--line);text-align:left;vertical-align:top}.t th{background:var(--paper-2);font-size:12px;letter-spacing:.6px;text-transform:uppercase}
.sws{display:grid;grid-template-columns:repeat(4,1fr);gap:14px}.sw{display:flex;flex-direction:column;font-size:13px}.sw .chipc{height:78px;border-radius:14px;border:1px solid #0000001a;margin-bottom:6px;display:flex;align-items:flex-end;padding:6px 9px}.sw .chipc span{font-size:10.5px;opacity:.85}
.sw code{background:none;padding:0;color:var(--muted)}.sw code.t{color:#8A6A2E}.sw small{color:var(--subtle)}
.steps{margin:0;padding-left:20px}.steps li{margin-bottom:6px}
.vpals{display:grid;gap:12px;margin-top:16px}.vpal{background:var(--surface);border:1px solid var(--line);border-radius:18px;padding:14px 16px}.vpal.prov{background-image:repeating-linear-gradient(45deg,#0000 0 10px,#8A5A1209 10px 20px)}
.vh{display:flex;gap:10px;align-items:center;margin-bottom:10px}.vh small{color:var(--subtle);margin-left:auto}
.badge{font-size:11px;font-weight:700;padding:2px 9px;border-radius:999px;background:var(--ok-100);color:var(--ok)}.badge.prov{background:var(--warn-100);color:var(--warn)}
.ms{display:grid;grid-template-columns:repeat(11,1fr);gap:6px}.mini-sw{height:62px;border-radius:10px;display:flex;align-items:flex-end;padding:5px}.mini-sw small{font-size:9.5px;line-height:1.25}
.ts td:first-child{width:200px;color:var(--muted)}.tspec p{margin:.4em 0}
.taghero{background:var(--ink);color:var(--paper);border-radius:var(--r-lg);padding:26px 30px;margin:16px 0}.taghero .note{color:#D9D1C1}.tagline{font-family:var(--serif);font-size:38px;margin:0;color:var(--paper)}
.pr .panel p{font-size:13.5px;color:var(--muted);margin:6px 0 0}.voice{margin-top:16px}.voice td.yes{color:var(--ok)}.voice td.nop{color:var(--err);text-decoration:line-through;text-decoration-color:#9A3B2866}
.g2 ul,.panel ul{margin:0;padding-left:18px;font-size:14px}.panel li{margin-bottom:6px}.g3 .panel p{font-size:13.5px;color:var(--muted);margin:6px 0 0}
.lkrow{margin-top:22px}.lkh{display:flex;gap:10px;align-items:center;margin-bottom:8px}.lkh small{color:var(--subtle)}.lkg{display:grid;grid-template-columns:1.4fr 1.4fr 1fr 1fr;gap:12px}.lkg figure{min-height:130px;align-items:center}.lkg svg{width:92%}.lkg .st svg{width:auto;max-height:150px;max-width:95%}
.icons{display:flex;flex-wrap:wrap;gap:22px;margin:10px 0 20px}.icn{margin:0;text-align:center;font-size:13px}.icn small{color:var(--subtle)}.icn a{font-size:12px}.ii svg{filter:drop-shadow(0 6px 14px #17242B33)}
.phonebg{background:linear-gradient(160deg,#3B4F58,#1C2A31)}.hsg{display:flex;gap:22px;justify-content:center;padding:14px}.hs{text-align:center;color:#fff;font-size:11px}.hs small{display:block;margin-top:6px}
.szs{display:flex;align-items:flex-end;gap:18px}.sz{text-align:center;font-size:11px;color:var(--subtle)}.sz small{display:block}
.radii{display:flex;gap:10px}.radii div{flex:1;border:1.5px solid var(--v-ink-800);padding:12px 8px;text-align:center;font-size:13px;font-weight:600;background:var(--v-ink-50)}.radii small{font-weight:400;color:var(--subtle)}
.themes .panel{background:var(--v-bg)}.row{display:flex;flex-wrap:wrap;gap:8px;margin-bottom:12px}
.b{font:600 14.5px var(--sans);border-radius:var(--r-md);padding:12px 18px;min-height:46px;border:1.5px solid transparent;cursor:pointer}
.b.pri{background:var(--v-ink-800);color:#fff}.b.sec{background:var(--surface);border-color:var(--v-ink-800);color:var(--v-ink-800)}.b.ghost{background:none;color:var(--v-ink-700);text-decoration:underline;text-underline-offset:3px}.b.dis{opacity:.38;cursor:not-allowed}.b:focus-visible{box-shadow:var(--focus);outline:0}
.chip{font:600 12px var(--sans);padding:5px 11px;border-radius:var(--r-pill);display:inline-flex;align-items:center;gap:5px}.chip.tema{background:var(--v-ink-100);color:var(--v-ink-800)}.chip.mode{border:1.5px solid var(--v-ink-800);color:var(--v-ink-800);background:var(--surface)}.chip.mode.ex{background:var(--v-ink-800);color:#fff}
.chip.ai{background:var(--ai-100);color:var(--ai)}.chip.src{background:var(--gold-100);color:#6B5320}.chip.warn{background:var(--warn-100);color:var(--warn)}
.prog{height:8px;border-radius:99px;background:var(--v-ink-100);overflow:hidden}.prog span{display:block;height:100%;background:var(--v-acc-500);border-radius:99px}.pl{color:var(--subtle);font-size:12px}
.states .state,.rgrid .state{border-radius:var(--r-md);padding:14px 16px;display:flex;flex-direction:column;border:1.5px solid}.state b{font:600 30px var(--sans);font-variant-numeric:tabular-nums}.state span{font-weight:600}.state small{color:var(--muted);font-size:12.5px;margin-top:4px}
.state.ok{border-color:var(--ok);background:var(--ok-100);color:var(--ok)}.state.er{border-color:var(--err);background:var(--err-100);color:var(--err)}.state.bl{border-color:var(--subtle);border-style:dashed;background:var(--surface);color:var(--subtle)}
.opt{display:flex;align-items:center;gap:10px;background:var(--surface);border:1.5px solid var(--line);border-radius:var(--r-md);padding:11px 13px;font-size:14px;margin-bottom:8px}.opt i{font-style:normal;font-weight:700;width:26px;height:26px;border-radius:8px;display:grid;place-items:center;background:var(--paper-2);font-size:13px;flex:none}
.opt.sel{border-color:var(--v-ink-800);background:var(--v-ink-50)}.opt.sel i{background:var(--v-ink-800);color:#fff}.opt.okk{border-color:var(--ok);background:var(--ok-100)}.opt.okk i{background:var(--ok);color:#fff}.opt.err{border-color:var(--err);background:var(--err-100)}.opt.err i{background:var(--err);color:#fff}
.aibox{border:1px solid #4B3F8F33;background:#4B3F8F0b;border-radius:var(--r-md);padding:13px 15px;display:flex;flex-direction:column;gap:4px}.aibox p{margin:2px 0;font-size:14px}.aibox a{color:var(--ai);font-size:12.5px;text-decoration:underline}.aibox blockquote{margin:4px 0;padding-left:10px;border-left:3px solid var(--gold);font-family:var(--serif);font-style:italic;font-size:14px;color:var(--muted)}
.aibox .ov{color:var(--ai);font-weight:700;font-size:10.5px;letter-spacing:1.3px}.aibox .lv{color:var(--subtle);font-size:11.5px}.aibox.abst{border-color:#8A5A1240;background:var(--warn-100)}.aibox.abst .ov{color:var(--warn)}
details{margin-top:18px}summary{cursor:pointer;font-weight:600}pre{background:var(--ink);color:#E9E1D2;padding:16px;border-radius:14px;font-size:11.5px;overflow:auto;max-height:420px}
.phones{display:flex;gap:26px;justify-content:center;flex-wrap:wrap;margin-top:12px}.phone{width:330px;border-radius:44px;background:#0E1418;padding:11px;box-shadow:0 18px 40px #17242B40}
.scr{background:var(--v-bg);border-radius:34px;padding:22px 16px 18px;min-height:640px;display:flex;flex-direction:column}
.ph-top{display:flex;justify-content:space-between;align-items:center;margin-bottom:12px}.pbrand .ps{font:600 19px var(--serif);color:var(--v-ink-800)}.pbrand .pv{font:500 16px var(--sans);color:var(--v-ink-800)}
.ph-meta{display:flex;justify-content:space-between;font-size:12px;color:var(--muted);margin:8px 0 6px}.ph-meta .g{color:var(--ok)}.ph-meta .n{color:var(--subtle)}.ph-meta .r{color:var(--err)}
.ph-q{font:500 19px/1.35 var(--serif);color:var(--v-ink-900);margin:8px 0 14px}.aibox.sm p{font-size:13px}.ph-b{margin-top:auto;display:flex;gap:8px;padding-top:12px}.ph-b .b{flex:1;padding:12px 8px;font-size:14px}
.res .ov2{font-size:11px;letter-spacing:1.4px;font-weight:700;color:var(--muted);margin:22px 0 0;text-align:center}.res .big{font:600 56px var(--sans);font-variant-numeric:tabular-nums;color:var(--v-ink-800);text-align:center;margin:0}.res .big small{font-size:22px;color:var(--subtle)}
.res .ten{text-align:center;margin:0 0 18px;color:var(--v-acc-600);font-weight:600}.rgrid{display:grid;grid-template-columns:repeat(3,1fr);gap:8px}.rgrid .state{padding:10px;align-items:center;text-align:center}.rgrid .state b{font-size:24px}.rgrid .state span{font-size:11.5px}
.fm{font-size:12px;color:var(--muted);text-align:center;margin:12px 0}.seal{display:flex;align-items:center;gap:10px;background:var(--surface);border:1px solid var(--gold);border-radius:var(--r-md);padding:10px 12px;font-size:13px;font-weight:600;color:#6B5320}
.files{columns:3;font-size:12.5px}.foot{color:var(--subtle);font-size:12.5px;text-align:center;padding:36px 0 0}
@media screen and (max-width:900px){.g2,.g3,.g4,.sws,.lkg{grid-template-columns:1fr 1fr}.ms{grid-template-columns:repeat(6,1fr)}.files{columns:1}.cover{padding:40px 28px}}
@page{size:330mm 467mm;margin:0}@media print{html,body{background:var(--paper)}.wrap{padding:0 40px 40px}.top{display:none}section{break-inside:auto}.panel,.phone,.lkrow,.vpal,table{break-inside:avoid}body{-webkit-print-color-adjust:exact;print-color-adjust:exact}.cover{margin:0;border-radius:0}h2{break-after:avoid}details pre{max-height:none}}
'''
cover_logo = horiz(c=P['paper'], base=P['gold_rev'])[0]
vlist = ''.join(f'<span><i style="background:{v[3]};border:2px solid {v[5]}"></i>Aula {v[0]}{" · prov." if v[7]=="Provisional" else ""}</span>' for v in V)
HTML = f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Aula · Manual de marca · Atrio v1</title><link rel="icon" href="icons/favicon.svg">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,500;0,8..60,600;0,8..60,700;1,8..60,500&display=swap" rel="stylesheet">
<style>{CSS}</style></head><body>
<nav class="top"><span class="lg">{horiz(c=P['paper'], base=P['gold_rev'])[0]}</span>{nav}<a href="#archivos">Archivos</a></nav>
<div class="wrap">
<header class="cover"><div class="cl">{cover_logo}</div><svg class="bigarch" viewBox="0 0 38 40">{arch(P['paper'],P['gold_rev'])}</svg>
<h1>Manual de marca de la plataforma</h1><p class="tg">«Estudia como se examina.»</p>
<p>Aula es la marca común de una línea de apps para preparar oposiciones en España. Una sola familia —el atrio— y una sala por cuerpo: cada vertical aporta su par de colores sin romper la familia. Este manual fija el sistema; cada vertical tendrá su propio anexo.</p>
<div class="vlist">{vlist}</div>
<p class="meta" style="margin-top:28px">Dirección C · Atrio · aprobada · v1.0 · 31 oct 2026 · Uso interno</p></header>
{''.join(secs)}
<section id="archivos"><p class="kicker">Anexo · Archivos</p><h2>Descargas</h2><p class="lead">Todos los logotipos tienen el texto convertido a trazados (no dependen de fuentes instaladas). PDF del manual: <a href="aula-brandbook-atrio-v1.pdf">aula-brandbook-atrio-v1.pdf</a> · todo en un ZIP: <a href="aula-brandbook-atrio-v1.zip">aula-brandbook-atrio-v1.zip</a>.</p><ul class="files">{files}</ul></section>
<p class="foot">Aula · Manual de marca de plataforma · Atrio v1.0 · Policía y Administración: colores provisionales · Sin dominios ni registro de marca (pendiente OEPM/EUIPO).</p>
</div></body></html>'''
open(os.path.join(OUT, "index.html"), "w").write(HTML); print("html", len(HTML))
