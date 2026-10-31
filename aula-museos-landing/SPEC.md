# Aula Museos — Landing v1 (aulamuseos.es)

Mock-up estático de diseño (no código de producción). Abrir `index.html`; renders en `png/` (`python3 render.py`, Playwright/Chromium). Fuentes autoalojadas en `fonts/` (OFL), sin CDN. Capturas de app reutilizadas de `aula-museos-v04/png` (PR #2).

## Marca y tokens (Aula · Atrio, vertical museos)
- Tipografía: Source Serif 4 (H1 56/38, H2 36/28, H3 20, peso 600) · Inter (UI, cuerpo 16/1.55, lead 19).
- Color: ink-800 `#15393F` (texto títulos, bloque final), terracota `#C0643F` / hover `#A55636` — **solo CTA**; gold `#C49A45` (fondo `#F5EBD3`) — **solo racha/XP**; paper `#F6F1E8`, surface `#FFFDF8`, line `#E3D9C8`, IA `#4B3F8F` / `#E9E6F7`.
- Bloques: `--block-1 #15393F` L, `--block-2 #577075` M, `--block-3 #8A7F70` (solo barra), `--block-3-text #766D60` (insignia P con texto blanco).
- Radios 10/16/22/pill; espaciado 4–48; sombra `sh-1`; foco `0 0 0 3px gold`.

## Estructura y copy (ES)
1. **Header**: logo Aula Museos · nav (Cómo funciona, Simulacro, Temario, Preguntas) · CTA «Empieza gratis».
2. **Hero**: eyebrow «Escala de Ayudantes de Museos del Estado» · H1 «Estudia como se examina.» · subtítulo «Simulacros con el formato real del examen, lecciones cortas cada día con la explicación al instante y los 79 temas del programa oficial, ordenados por bloques.» · CTA «Empieza gratis» + secundario «Ver cómo funciona» · chips 100 + 10 preguntas / 100 minutos / +1 · 0 · −1/3 / 79 temas · BOE · 2 móviles (screen-01, screen-04).
3. **Cómo funciona**: 1 Lección diaria · 2 Repasa tus errores · 3 Simulacro real · chip racha/XP (metas Ligera/Regular/Intensa).
4. **Simulacro**: «El examen, tal y como será» — 100+10, 100 min, +1/0/−1/3, escala 0–30, BOE-A-2025-26893; tarjeta con fórmula del ejemplo 68/21/11 → 21,64; «nota de corte orientativa».
5. **Temario**: «79 temas, tres bloques» — barra 30/30/40; Legislación 1–16 (30), Museología 17–35 (30), Patrimonio artístico, arqueológico y antropológico 36–79 (40).
6. **IA con fuentes**: ejemplo con etiqueta «Contenido generado por IA» + «Fuente: …» (si no hay: «Sin fuente»).
7. **FAQ** (`<details>`): oposición, cálculo de nota, tiempo al día, ¿es gratis? (**placeholder**), ¿es oficial? (no afiliada).
8. **CTA final** (fondo ink): «Estudia como se examina.» · «Empieza hoy con tu primera lección.» · «Empieza gratis».
9. **Footer**: «© Aula · Atrio» · «Aviso legal · Privacidad · no afiliada al Ministerio de Cultura».

Prohibido: «Duolingo», «garantía de aprobado», sellos/logos del Estado o Ministerio, mascotas/vidas/ligas, estadísticas, testimonios o precios inventados. Placeholders marcados con borde discontinuo terracota `[…]`.

## Breakpoints
- **1280** (desktop): contenedor 1120, hero 2 columnas, grids 3/2 columnas.
- **390** (móvil, ≤820): 1 columna, nav oculta (solo logo; CTA en hero), botones a ancho completo, H1 38.

## Accesibilidad
- Contraste AA (texto ≥4.5:1; `#8A7F70` nunca como texto). `lang="es"`, enlace «Saltar al contenido», landmarks header/nav/main/footer, un solo H1.
- Foco visible (anillo gold 3px), objetivos táctiles ≥44px, FAQ con `<details>` nativo, mockups de móvil `aria-hidden`, barra de bloques con `role="img"` + `aria-label`.
- `font-display: swap`; respetar `prefers-reduced-motion` si se añade animación.

## SEO
- Title: «Aula Museos — Oposiciones Ayudantes de Museos del Estado»
- Description: «Prepara la oposición a la Escala de Ayudantes de Museos del Estado con simulacros en formato real (100 + 10 preguntas, 100 min), lecciones diarias y los 79 temas del BOE. Estudia como se examina.»
- Añadir en prod: canonical `https://aulamuseos.es/`, OG/Twitter (imagen 1200×630 a diseñar), FAQPage JSON-LD.

## Analítica (nombres de eventos)
- `lp_view` · `lp_cta_click` {loc: nav|hero|final} · `lp_secondary_click` · `lp_section_view` {id} · `lp_faq_open` {q} · `lp_footer_click` {link}. Atributos `data-ev`/`data-loc` en el mockup.
