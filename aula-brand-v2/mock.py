import json,pathlib
H=pathlib.Path(__file__).parent
def logo(k,p,path):
    n=p['navy']
    if k=='a':
        mark=f'''<g transform="translate(40,34)" fill="none" stroke="{p['gold']}" stroke-width="3"><path d="M0 52 V22 A20 20 0 0 1 40 22 V52"/><path d="M10 52 V26 A10 10 0 0 1 30 26 V52"/><line x1="-6" y1="54" x2="46" y2="54"/><circle cx="20" cy="12" r="2.5" fill="{p['gold']}" stroke="none"/></g>
<text x="104" y="86" font-family="Fraunces, Georgia, serif" font-size="64" font-weight="600" fill="{p['gold']}" letter-spacing="1">Aula</text>'''
    else:
        mark=f'''<g transform="translate(36,30)" stroke="{p['gold']}" stroke-width="1.5" fill="{p['gold']}"><line x1="4" y1="54" x2="24" y2="6"/><line x1="24" y1="6" x2="44" y2="54"/><line x1="12" y1="36" x2="36" y2="36"/><circle cx="24" cy="6" r="4"/><circle cx="4" cy="54" r="3"/><circle cx="44" cy="54" r="3"/><circle cx="12" cy="36" r="2.5"/><circle cx="36" cy="36" r="2.5"/></g>
<text x="102" y="84" font-family="Outfit, system-ui, sans-serif" font-size="58" font-weight="500" fill="{p['gold']}" letter-spacing="6">AULA</text>'''
    svg=f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 120" width="320" height="120" role="img" aria-label="Aula">
<defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{n[0]}"/><stop offset=".55" stop-color="{n[1]}"/><stop offset="1" stop-color="{n[2]}"/></linearGradient></defs>
<rect width="320" height="120" rx="22" fill="url(#g)"/>{mark}</svg>'''
    path.write_text(svg); return svg
def mobile(k,p,svg):
    n=p['navy'];serif=k=='a'
    star='' if serif else "background-image:radial-gradient(circle,rgba(242,201,76,.35) 1px,transparent 1.5px),linear-gradient(rgba(255,255,255,.04) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.04) 1px,transparent 1px),linear-gradient(%s,%s,%s,%s);background-size:56px 56px,28px 28px,28px 28px,100%% 100%%;"%(p['angle'],n[0],n[1],n[2])
    bg=star or f"background:linear-gradient({p['angle']},{n[0]},{n[1]} 55%,{n[2]})"
    return f'''<!doctype html><html lang="es"><meta charset="utf-8"><style>
@font-face{{font-family:'{p['display']}';src:url(../fonts/{p['dfile']}.woff2)}}@font-face{{font-family:'{p['ui']}';src:url(../fonts/{p['ufile']}.woff2)}}
body{{margin:0;width:390px;height:844px;font:15px/1.45 '{p['ui']}',sans-serif;background:{p['surface']};color:{p['ink']}}}
.top{{{bg};padding:20px 20px 28px;border-radius:0 0 28px 28px;color:#fff}}
.row{{display:flex;justify-content:space-between;align-items:center}}.logo svg{{height:38px;width:auto}}
.pill{{border:1px solid {p['gold']}66;color:{p['gold']};border-radius:999px;padding:6px 12px;font-weight:600;font-size:14px}}
h1{{font-family:'{p['display']}';font-weight:{600 if serif else 500};font-size:30px;line-height:1.15;color:{p['gold']};margin:22px 0 6px;{'' if serif else 'letter-spacing:.01em'}}}
.sub{{color:#C9D2E3;margin:0 0 18px}}
.xp{{background:rgba(255,255,255,.07);border:1px solid rgba(255,255,255,.12);border-radius:16px;padding:14px}}
.bar{{height:8px;background:rgba(255,255,255,.12);border-radius:9px;margin-top:8px}}.bar i{{display:block;height:8px;width:64%;background:{p['gold']};border-radius:9px}}
.days{{display:flex;gap:6px;margin-top:12px}}.days b{{flex:1;text-align:center;font-size:11px;padding:5px 0;border-radius:8px;background:rgba(255,255,255,.06);color:#C9D2E3;font-weight:500}}.days b.on{{background:{p['gold']};color:{n[0]};font-weight:700}}
.main{{padding:18px 20px}}
.card{{background:#fff;border:1px solid {p['line']};border-radius:16px;padding:16px;margin-bottom:14px}}
.k{{font-size:12px;letter-spacing:.08em;text-transform:uppercase;font-weight:600;color:{p['muted']}}}
h2{{font-family:'{p['display']}';font-size:21px;margin:4px 0 6px;color:{p['ink']};font-weight:600}}
.btn{{display:block;text-align:center;background:linear-gradient(135deg,{n[0]},{n[2]});color:{p['gold']};font-weight:700;border-radius:999px;padding:13px;margin-top:12px}}
.tag{{display:inline-block;border-radius:999px;padding:3px 9px;font-size:12px;font-weight:600;margin-right:6px}}
.m{{background:{p['museosDeep']};color:#fff}}.ai{{background:{p['aiBg']};color:{p['ai']}}}
.mono{{font-variant-numeric:tabular-nums}}
.tab{{position:absolute;bottom:0;left:0;right:0;height:64px;background:{n[0]};display:flex;justify-content:space-around;align-items:center;color:#9AA6BD;font-size:12px}}.tab .on{{color:{p['gold']};font-weight:700}}
</style><body style="position:relative"><div class="top">
<div class="row"><span class="logo">{svg.replace('width="320" height="120"','')}</span><span class="pill">🔥 12 días · 340 XP</span></div>
<h1>Buenas tardes, Lucía.</h1><p class="sub">Estudia como se examina.</p>
<div class="xp"><div class="row"><span>Meta diaria · Regular</span><span class="mono" style="color:{p['gold']};font-weight:700">32 / 50 XP</span></div><div class="bar"><i></i></div>
<div class="days"><b class="on">L</b><b class="on">M</b><b class="on">X</b><b class="on">J</b><b>V</b><b>S</b><b>D</b></div></div></div>
<div class="main"><div class="card"><span class="tag m">Museos</span><div class="k" style="margin-top:8px">Lección de hoy · 6 min</div><h2>Tema 18 · Funciones del museo</h2><p style="margin:0;color:{p['muted']}">10 preguntas con explicación al instante.</p><span class="btn">Empezar lección</span></div>
<div class="card"><div class="k">Simulacro</div><h2>Examen completo</h2><p class="mono" style="margin:0;color:{p['muted']}">100 + 10 preguntas · 100 min · +1 / 0 / −1/3</p><div style="margin-top:10px"><span class="tag ai">Contenido generado por IA</span><span style="font-size:12px;color:{p['muted']}">con fuente</span></div></div></div>
<div class="tab"><span class="on">Hoy</span><span>Temario</span><span>Simulacro</span><span>Perfil</span></div></body></html>'''
for k in 'ab':
    p=json.loads((H/f'direction-{k}'/'palette.json').read_text())
    svg=logo(k,p,H/f'direction-{k}'/'logo-aula.svg')
    (H/f'direction-{k}'/'mobile.html').write_text(mobile(k,p,svg))
from playwright.sync_api import sync_playwright
with sync_playwright() as pw:
    b=pw.chromium.launch()
    for k in 'ab':
        pg=b.new_page(viewport={'width':390,'height':844},device_scale_factor=2)
        pg.goto((H/f'direction-{k}'/'mobile.html').as_uri());pg.wait_for_load_state('networkidle');pg.evaluate('document.fonts.ready');pg.wait_for_timeout(300)
        pg.screenshot(path=str(H/f'direction-{k}'/'mobile.png'))
    (H/'compare.html').write_text('<body style="margin:0;background:#1b1f2a;font:600 18px system-ui;color:#eee;display:flex;gap:40px;padding:30px;width:880px"><div><p>A · Noche de estudio</p><img src="direction-a/mobile.png" width="390"></div><div><p>B · Constelación</p><img src="direction-b/mobile.png" width="390"></div></body>')
    pg=b.new_page(viewport={'width':940,'height':1000},device_scale_factor=2)
    pg.goto((H/'compare.html').as_uri());pg.wait_for_load_state('networkidle');pg.screenshot(path=str(H/'compare.png'),full_page=True)
    b.close()
