import json
T=json.load(open('tokens/_t.json'));C=json.load(open('tokens/contrast.json'));L=json.load(open('logo/_list.json'));I=json.load(open('icons/_list.json'))
VN={'museos':'Museos','justicia':'Justicia','policia':'Policía','educacion':'Educación'}
sw=lambda n,h,fg:f'<div class="sw"><div style="background:{h};color:{fg}">{n}</div><code>{h}</code></div>'
dk=lambda h: sum(int(h[i:i+2],16) for i in (1,3,5))<380
pal=lambda g: ''.join(sw(k,v,'#F4F1EA' if dk(v) else '#142A3D') for k,v in T[g].items())
rows=''.join(f'<tr><td>{r["name"]}</td><td><span class="chipc" style="background:{r["bg"]};color:{r["fg"]}">Aa</span> <code>{r["fg"]}</code> / <code>{r["bg"]}</code></td><td><b>{r["ratio"]}</b></td><td>{"AA ✓" if r["AA"] else ("solo grande" if r["AA_large"] else "no texto")}</td><td>{r["use"]}</td></tr>' for r in C['contrast'])
comp=''.join(f'<tr><td><code>{c["hex"]}</code> {c["ours"]}</td><td><code>{c["refhex"]}</code> {c["ref"]}</td><td><b>{c["dE2000"]}</b></td></tr>' for c in C['competitors'])
fig=lambda src,cap,cls='':f'<figure class="{cls}"><img src="{src}" alt="{cap}" loading="lazy"><figcaption>{cap}</figcaption></figure>'
logos=''.join(f'<figure class="lg {"dk" if ("on-dark" in n or n.endswith("-dark")) else ""}"><img src="logo/{n}.svg" alt="{n}"><figcaption><a href="logo/{n}.svg">SVG</a> · <a href="logo/png/{n}.png">PNG</a> · {n}</figcaption></figure>' for n in L)
icons=''.join(f'<figure class="icn"><img src="icons/{k}.svg" alt="{k}"><figcaption>{k}</figcaption></figure>' for k in I)
verts=''.join(f'<tr><td><span class="marker" style="background:{v["light"]}"></span> <b>{VN[k]}</b></td><td><code>{v["light"]}</code></td><td><code>{v["dark"]}</code></td></tr>' for k,v in T['vertical'].items())
tone=[('Decimos','No decimos'),('Menos ruido. Más temario.','¡¡Arrasa en tu oposición!!'),('Cada respuesta, explicada con la norma.','Promesas de resultado'),('Estudia con método, no con suerte.','Comparaciones con otras apps'),('Era la B. La Ley 16/1985 es la norma básica…','¡Fallaste! 😢'),('12 días seguidos. Buen ritmo.','¡¡RACHA ÉPICA!! 🔥🔥🔥'),('Sin fuente — revisa con el temario oficial.','Inventar una cita o un artículo')]
tonet=''.join(f'<tr><td>{a}</td><td>{b}</td></tr>' for a,b in tone[1:])
html=f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex,nofollow"><title>Aula. — Brandbook · D · Editorial</title>
<link rel="icon" href="favicon/favicon.svg"><link rel="stylesheet" href="ui/aula-ui.css"><style>
.wrap{{max-width:1120px;margin:0 auto;padding:24px}}section{{padding:40px 0;border-bottom:1px solid var(--line)}}h2{{font-size:34px}}h3{{margin-top:22px}}
.toc{{display:flex;flex-wrap:wrap;gap:6px 18px;font-size:14px}}.grid{{display:grid;gap:12px;grid-template-columns:repeat(auto-fill,minmax(140px,1fr))}}
.sw div{{height:68px;border-radius:8px;display:flex;align-items:flex-end;padding:8px;font-size:13px;border:1px solid var(--line)}}.sw code{{font-size:12px}}
.tw{{overflow-x:auto}}table{{border-collapse:collapse;width:100%;font-size:14px;background:#fff;min-width:620px}}td,th{{padding:7px 10px;border-bottom:1px solid var(--line);text-align:left}}.chipc{{display:inline-block;padding:2px 8px;border-radius:5px;font:500 12px var(--font-mono)}}
.lgs{{display:grid;gap:12px;grid-template-columns:repeat(auto-fill,minmax(240px,1fr))}}.lg{{margin:0;background:#fff;border:1px solid var(--line);border-radius:12px;padding:12px}}.lg.dk{{background:#142A3D}}.lg img{{height:52px;max-width:100%;display:block}}.lg figcaption{{font-size:11px;margin-top:6px;color:var(--subtle);word-break:break-all}}.lg.dk figcaption,.lg.dk a{{color:#B9BCC8}}
.icons{{display:grid;grid-template-columns:repeat(auto-fill,minmax(72px,1fr));gap:10px;background:#fff;padding:16px;border-radius:12px}}.icn{{margin:0;text-align:center;font-size:11px;color:var(--subtle)}}.icn img{{width:28px}}
figure{{margin:0}}figure img{{max-width:100%;display:block;border-radius:10px;border:1px solid var(--line)}}figcaption{{font-size:12px;color:var(--subtle);margin-top:4px}}.phs{{display:grid;gap:14px;grid-template-columns:repeat(auto-fill,minmax(170px,1fr))}}.two{{display:grid;gap:14px;grid-template-columns:repeat(auto-fit,minmax(320px,1fr))}}
pre{{background:#fff;border:1px solid var(--line);padding:14px;border-radius:10px;overflow:auto;font:500 12px/1.5 var(--font-mono);max-height:360px}}
</style></head><body><div class="wrap">
<header style="display:flex;justify-content:space-between;align-items:center;gap:12px;flex-wrap:wrap"><img src="logo/aula-umbrella-horizontal.svg" height="40" alt="Aula."><span class="eyebrow">Brandbook · Dirección D · Editorial · v1</span></header>
<section><h1 style="font-size:56px">Menos ruido<span class="dot">.</span> Más temario<span class="dot">.</span></h1><p class="muted" style="font-size:19px;max-width:720px">Aula es una plataforma para preparar oposiciones con calma y método. Papel, tinta navy y un único acento dorado. El punto del logotipo significa «resuelto».</p>
<nav class="toc">{''.join(f'<a href="#{a}">{b}</a>' for a,b in [('logo','Logotipo'),('icono','Icono y favicon'),('web','Web'),('color','Color'),('tipo','Tipografía'),('ui','UI kit'),('pantallas','Pantallas'),('verticales','Verticales'),('tono','Tono'),('iconos','Iconos'),('plantillas','Plantillas'),('tokens','Tokens')])}</nav>
<figure style="margin-top:18px"><img src="png/board-summary.png" alt="Resumen"></figure></section>
<section id="logo"><h2>Logotipo</h2><p>«Aula.» en Fraunces 600. El punto dorado es la firma: «resuelto». Versiones horizontal, apilada y marca «A.». Zona de respeto = x (altura de la «A»). Tamaño mínimo: 72 px de ancho (wordmark), 16 px (marca).</p>
<img src="ui/logo-sheet.png" alt="Hoja de logotipo" style="max-width:100%;border-radius:10px"><h3>Todos los archivos</h3><div class="lgs">{logos}</div></section>
<section id="icono"><h2>Icono de app y favicon</h2><p>Marca «A.» en papel sobre navy, punto dorado. iOS 20–1024, Android mdpi–xxxhdpi y Play Store 512, adaptive icon con capa monocroma.</p>
<div class="two">{fig('app-icon/master-1024.png','master 1024')}{fig('app-icon/android-adaptive-preview.png','Android adaptive: círculo, squircle, gota, monocromo')}</div>
<p style="margin-top:12px">{''.join(f'<img src="favicon/favicon-{s}.png" width="{s}" style="margin-right:12px;vertical-align:bottom"> ' for s in [16,32,48,64])} <a href="favicon/head-snippet.html">head-snippet.html</a> · <a href="favicon/favicon.svg">favicon.svg</a></p></section>
<section id="web"><h2>Web: cabecera, héroe y pie</h2><div class="two">{fig('web/site-desktop-1280.png','Escritorio 1280')}{fig('web/site-mobile-390.png','Móvil 390')}</div><p class="muted" style="margin-top:10px">Pie obligatorio: «Aviso legal · Privacidad · no afiliada al Ministerio de Cultura».</p></section>
<section id="color"><h2>Color</h2><p>Papel <code>#F4F1EA</code> y tinta navy <code>#142A3D</code> llevan la marca. El oro <code>#D9A21B</code> es <b>solo acento</b> (punto, marcador, barra de meta); como texto se usa <code>gold-700 #856000</code> (AA). Botón principal: navy.</p>
<h3>Marca</h3><div class="grid">{pal('brand')}</div><h3>Neutros</h3><div class="grid">{pal('neutral')}</div><h3>Semánticos</h3><div class="grid">{pal('semantic')}</div><h3>Modo oscuro</h3><div class="grid">{pal('dark')}</div>
<h3>Contraste WCAG 2.2</h3><div class="tw" data-ovok><table><tr><th>Par</th><th>Muestra</th><th>Ratio</th><th>Nivel</th><th>Uso</th></tr>{rows}</table></div>
<h3>Distancia vs competencia (ΔE2000)</h3><div class="tw" data-ovok><table><tr><th>Aula</th><th>Referencia</th><th>ΔE2000</th></tr>{comp}</table></div><img src="ui/competitor-check.png" style="max-width:100%;margin-top:10px" alt=""></section>
<section id="tipo"><h2>Tipografía</h2><p><b class="serif">Fraunces</b> (titulares, cifras grandes) + <b>IBM Plex Sans</b> (interfaz y texto) + <span class="mono">IBM Plex Mono</span> (fórmulas, contadores). Las tres con licencia OFL, servidas desde <code>fonts/</code>, sin CDN.</p>
<div class="tw" data-ovok><table>{''.join(f'<tr><td><b>{k}</b></td><td>{v}</td></tr>' for k,v in T['type'].items())}</table></div>
<p class="serif" style="font-size:48px;margin-top:18px">Funciones del museo<span class="dot">.</span></p><p style="max-width:640px">La Ley 16/1985 es la norma básica del Patrimonio Histórico Español. Texto de lectura en Plex Sans 16/1,55.</p><p class="mono">D = aciertos − errores ÷ 3</p></section>
<section id="ui"><h2>UI kit</h2>{fig('ui/ui-kit.png','Claro')}<div style="height:14px"></div>{fig('ui/ui-kit-dark.png','Oscuro')}
<h3>Motivación, con contención</h3><p>Racha y XP se mantienen, en tamaño pequeño y sin animaciones ruidosas: chip «12 días», meta diaria con barra dorada fina, puntos por día. Sin mascotas, sin vidas, sin ligas.</p></section>
<section id="pantallas"><h2>Pantallas</h2><div class="phs">{''.join(fig(f'screens/{k}.png',n) for k,n in [('home','Hoy'),('home-dark','Hoy · oscuro'),('question','Pregunta'),('explanation','Explicación · IA + fuente'),('result','Resultado'),('simulacro','Simulacro')])}</div>
<p class="muted" style="margin-top:10px">Explicación: etiqueta «Contenido generado por IA» y fuente citada; si no hay fuente verificable se muestra «Sin fuente». Nota del simulacro: escala 0–30, 15 = «nota de corte orientativa».</p></section>
<section id="verticales"><h2>Verticales</h2><p>La vertical se indica solo con un <b>marcador cuadrado pequeño</b> (9 px, radio 2) junto al nombre o la etiqueta. Nunca recolorea botones, fondos ni el logotipo; el CTA es siempre navy.</p>
<div class="tw" data-ovok><table><tr><th>Vertical</th><th>Claro</th><th>Oscuro</th></tr>{verts}</table></div></section>
<section id="tono"><h2>Tono de voz</h2><p>Calmado, preciso, de tú. Frases cortas que terminan en punto. Explicamos con la norma y decimos cuando no sabemos. Nada de promesas de resultado.</p>
<div class="tw" data-ovok><table><tr><th>Decimos</th><th>No decimos</th></tr>{tonet}</table></div></section>
<section id="iconos"><h2>Iconos</h2><p>Rejilla 24 px, trazo 1,5, extremos redondeados, color <code>currentColor</code>.</p><div class="icons">{icons}</div></section>
<section id="plantillas"><h2>Plantillas</h2><div class="phs">{fig('templates/instagram-post-1080.png','Instagram post 1080')}{fig('templates/instagram-story-1080x1920.png','Story 1080×1920')}{''.join(fig(f'templates/appstore-6.7-{i}-1290x2796.png',f'App Store 6,7" · {i}') for i in range(1,5))}</div>
<div class="two" style="margin-top:14px">{fig('templates/og-image-1200x630.png','OG 1200×630')}{fig('templates/email-signature.png','Firma de correo · <a href="templates/email-signature.html">HTML</a>')}</div></section>
<section id="tokens"><h2>Tokens</h2><p><a href="tokens/aula-tokens.json">aula-tokens.json</a> · <a href="tokens/aula-tokens.css">aula-tokens.css</a> · <a href="tokens/contrast.json">contrast.json</a></p><pre data-ovok>{open('tokens/aula-tokens.css').read()}</pre></section>
<footer style="padding:28px 0;font-size:14px" class="muted">Aviso legal · Privacidad · no afiliada al Ministerio de Cultura</footer></div></body></html>'''
open('index.html','w').write(html)
# board
B=f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><link rel="stylesheet" href="ui/aula-ui.css"><style>body{{width:1880px;padding:36px;overflow:hidden}}.b{{display:grid;grid-template-columns:330px 1fr 1fr 1fr 1fr 1fr;gap:18px;align-items:start}}.b img{{width:100%;display:block;border-radius:14px;border:1px solid var(--line)}}.c{{font-size:13px}}.k{{display:flex;gap:6px;margin:6px 0}}.k i{{flex:1;height:40px;border-radius:6px;border:1px solid var(--line)}}</style></head><body>
<div style="display:flex;justify-content:space-between;align-items:end;margin-bottom:22px"><div><p class="eyebrow">Aula · Brandbook · Dirección D · Editorial</p><h1 style="font-size:52px;margin:0">Menos ruido<span class="dot">.</span> Más temario<span class="dot">.</span></h1></div><img src="logo/aula-umbrella-horizontal.svg" height="64" style="border:0"></div>
<div class="b"><div class="c"><img src="logo/aula-stacked-light.svg" style="width:150px;border:0;margin-bottom:10px">
<p class="eyebrow">Color</p><div class="k"><i style="background:#F4F1EA"></i><i style="background:#142A3D"></i><i style="background:#D9A21B"></i><i style="background:#856000"></i><i style="background:#66697F"></i></div>
<p style="margin:0">papel #F4F1EA · navy #142A3D (13,0:1) · oro #D9A21B solo acento · gold-700 #856000 (5,1:1) · subtle #66697F (4,8:1)</p>
<p class="eyebrow" style="margin-top:14px">Verticales · marcador</p>{''.join(f'<span class="vtag" style="margin-right:10px"><span class="marker" style="background:{v["light"]}"></span>{VN[k]}</span>' for k,v in T['vertical'].items())}
<p class="eyebrow" style="margin-top:14px">Tipografía</p><p class="serif" style="font-size:28px;margin:0">Fraunces</p><p style="margin:0">IBM Plex Sans · <span class="mono">Plex Mono</span></p>
<p class="eyebrow" style="margin-top:14px">ΔE2000 navy / oro</p><p style="margin:0">vs OpositaTest: 11,3 / 25,1<br>vs MAD: 10,9 / 40,8</p>
<img src="app-icon/master-1024.png" style="width:96px;margin-top:14px;border-radius:22px"></div>
{''.join(f'<img src="screens/{k}.png">' for k in ['home','explanation','result','simulacro','home-dark'])}</div>
<div style="display:grid;grid-template-columns:1.5fr 1fr 1fr;gap:18px;margin-top:18px"></div></body></html>'''
open('board.html','w').write(B)
print('ok')
