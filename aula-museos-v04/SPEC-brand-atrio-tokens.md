# SPEC · PR «brand: Atrio tokens» para MuratPod/aula-museos-web

Base: `main` @ `4e16c74`. Números de línea según ese commit. Fuente de verdad: `aula-tokens.css` → `[data-vertical="museos"]` (polina-design).
**Fuera de alcance** (PR de cumplimiento aparte): fuentes (CDN de Google Fonts en `index.html:12-14`), etiqueta «Contenido generado por IA» y pie legal.

## 1. Tokens en `src/index.css` (`:root`)

| file:line | actual | nuevo (token) |
|---|---|---|
| src/index.css:2 | `--ink-900:#0F2A30` | `#102B2F` (`--ink-900`) |
| src/index.css:2 | `--ink-800:#15393F` | sin cambio |
| src/index.css:2 | `--ink-700:#1D4D55` | `#36555A` (`--ink-700`) |
| src/index.css:2 | `--ink-600:#28646D` | `#577075` (`--ink-600`) |
| src/index.css:2 | `--ink-100:#DCE9E8` | `#DEE3E4` (`--ink-100`) |
| src/index.css:2 | `--ink-50:#EEF5F4` | `#EFF1F2` (`--ink-50`) |
| src/index.css:4 | `--terra-600:#A84B2A` | `#A55636` (`--terra-600` = museos acc-600) |
| src/index.css:4 | `--terra-500:#C0643F` | sin cambio |
| src/index.css:4 | `--terra-100:#F6E3D9` | `#F5E6E0` (`--terra-100`) |
| src/index.css:3,4,5 | paper, paper-2, surface, line, text, muted, subtle, gold-500, gold-100, ok, err, ai | sin cambio (ya coinciden) |
| src/index.css:4 (nuevo) | — | añadir `--gold-700:#7A5A17` (texto sobre gold-100, solo XP) |
| src/index.css:5 (nuevo) | — | añadir `--ok-300:#B9D8C4; --err-300:#E6BFB2; --ai-900:#2A2450; --ai-300:#CFC8EE; --ai-200:#DDD8F2; --ai-50:#F3F1FB; --on-dark:#FFFFFF` |
| src/index.css:7 | `--r:14px` | sustituir por escala `--r-sm:10px; --r-md:16px; --r-lg:22px; --r-pill:999px` |
| src/index.css:7 (nuevo) | — | `--s-1:4px … --s-7:48px` (4/8/12/16/24/32/48), `--sh-1:0 1px 0 rgba(21,57,63,.04)`, `--focus:0 0 0 3px var(--gold-500)` (anillo de foco, no decorativo) |

## 2. Oro solo para XP / racha

| file:line | actual | nuevo |
|---|---|---|
| src/index.css:21 | `.pill{background:var(--gold-100);color:#7a5a17;border-radius:99px;padding:4px 10px}` | `.pill{background:var(--paper-2);color:var(--ink-700);border-radius:var(--r-pill);padding:var(--s-1) 10px}` (neutro) |
| src/index.css:21 (nuevo) | — | `.pill--xp{background:var(--gold-100);color:var(--gold-700)}` |
| src/App.tsx:50 | `<span className="pill">v0.1</span>` | sin cambio de clase → queda neutro |
| src/App.tsx:202 | `<span className="pill">+{xp} XP</span>` | `className="pill pill--xp"` |
| src/index.css:48 | `.note{background:var(--gold-100);…;color:#5b4512}` | `.note{background:var(--ink-50);border:1px solid var(--ink-100);border-radius:var(--r-md);color:var(--ink-800)}` |
| src/index.css:53 | `.bar div{background:var(--gold-500)}` (progreso del test) | `var(--ink-800)` — progreso no es XP |
| src/App.tsx:23 | logo: `stroke="#C49A45"` (línea base) | `stroke="var(--terra-500)"` (logo Museos: base teja) |
| public/logo.svg | `#C49A45` (base), `#28646D` | `#C0643F`, `#577075` |
| public/favicon.svg | `#C49A45` | `#C0643F` |

## 3. Hex sueltos → tokens

| file:line | actual | nuevo |
|---|---|---|
| src/index.css:33 | `box-shadow:0 1px 0 rgba(21,57,63,.04)` | `var(--sh-1)` |
| src/index.css:41 | `.chip.on{color:#fff}` | `var(--on-dark)` |
| src/index.css:43 | `.btn--primary{color:#fff}` | `var(--on-dark)` |
| src/index.css:60,61,62 | `.l{color:#fff}` | `var(--on-dark)` |
| src/index.css:69 | `.exp--ok{border-color:#b9d8c4}` | `var(--ok-300)` |
| src/index.css:70 | `.exp--err{border-color:#e6bfb2}` | `var(--err-300)` |
| src/index.css:73 | `.aula{color:#2a2450}` | `var(--ai-900)` |
| src/index.css:76 | `.aula__beta{background:#fff}` | `var(--surface)` |
| src/index.css:79 | `.cite__chip{border:1px solid #cfc8ee;background:#fff}` | `var(--ai-300)`, `var(--surface)` |
| src/index.css:80 | `.cite blockquote{background:#fff}` | `var(--surface)` |
| src/index.css:82 | `linear-gradient(90deg,#ddd8f2,#f3f1fb,#ddd8f2)` | `var(--ai-200), var(--ai-50), var(--ai-200)` |
| src/index.css:92 | `.dot{color:#fff}` | `var(--on-dark)` |
| index.html:7 / public/manifest.webmanifest | `#15393F`, `#F6F1E8` | sin cambio (meta/manifest no admiten var(); valores = ink-800 y paper) |

## 4. Radios y espaciado

| file:line | actual | nuevo |
|---|---|---|
| src/index.css:21,40 | `border-radius:99px` | `var(--r-pill)` |
| src/index.css:52,53 | `border-radius:99px` (barra) | `var(--r-pill)` |
| src/index.css:29,48 | `var(--r)` (14px) | `var(--r-md)` |
| src/index.css:33 | `.card{border-radius:18px;padding:18px;margin-bottom:16px}` | `var(--r-lg)`, `var(--s-4)`, `var(--s-4)` |
| src/index.css:35,42,57,73 | `border-radius:12px` | `var(--r-sm)` |
| src/index.css:66 | `.exp{border-radius:16px;padding:16px}` | `var(--r-md)`, `var(--s-4)` |
| src/index.css:91 | `border-radius:10px` | `var(--r-sm)` |
| src/index.css:58,79 / 80 | `8px` / `6px` (insignias, cita) | `var(--s-2)` como radio pequeño (aceptado) |
| src/index.css:28,34,39,78 | `gap:8px` / `6px` | `var(--s-2)` |
| src/index.css:56 | `margin:18px 0;gap:10px` | `var(--s-4) 0`, `var(--s-3)` |
| src/index.css:14,47,50 | `margin-bottom:22px`, `margin-top:20px`, `margin-top:24px` | `var(--s-5)` |

Tamaños de letra fuera de alcance.

## 5. Criterios de aceptación (grep, desde la raíz)

```sh
# 1) Ningún hex fuera del bloque :root (líneas de definición de tokens)
grep -nE '#[0-9A-Fa-f]{3,8}\b' src/index.css | grep -vE '^[0-9]+:\s*--' ; test $? -eq 1
# 2) Ningún hex en componentes
! grep -nE '#[0-9A-Fa-f]{3,8}\b' src/*.tsx
# 3) Valores antiguos eliminados
! grep -rniE '0F2A30|1D4D55|28646D|DCE9E8|EEF5F4|A84B2A|F6E3D9|7a5a17|5b4512' src public
# 4) Oro solo en XP/racha y foco
grep -nE 'gold-(500|100|700)' src/index.css | grep -vE '^[0-9]+:\s*--|\.pill--xp|--focus' ; test $? -eq 1
grep -n 'pill--xp' src/App.tsx   # solo la línea del «+{xp} XP»
# 5) Sin radios/rgba sueltos
! grep -nE 'border-radius:[0-9]+px|rgba\(' src/index.css | grep -vE '^[0-9]+:\s*--'
# 6) Build
npm run build
```
Revisión visual: inicio, pregunta (sel/ok/err), resultado; la «v0.1» ya no es dorada, «+N XP» sí.

## 6. Tokens de bloque (neutros) + letra L/M/P

Decisión: bloques en neutros + letra; teja (`--terra-500`) solo para «Marcada»; oro solo XP.

| token | hex | uso | vs paper #F6F1E8 | vs surface #FFFDF8 | vs blanco | texto ≥4.5 | tira ≥3 |
|---|---|---|---|---|---|---|---|
| `--block-1` (L · Legislación) | `#15393F` (= ink-800) | texto, letra, tira | 11.05 | 12.23 | 12.43 | sí | sí |
| `--block-2` (M · Museología) | `#577075` (= ink-600) | texto, letra, tira | 4.69 | 5.19 | 5.28 | sí | sí |
| `--block-3` (P · Patrimonio) | `#8A7F70` | **solo tira / relleno no textual** | 3.49 | 3.86 | 3.92 | no | sí |
| `--block-3-text` | `#766D60` (mismo tono, más oscuro) | texto y fondo de la letra P | 4.52 | 5.01 | 5.09 | sí | sí |

Letra blanca sobre relleno: L 12.43, M 5.28, P (`--block-3-text`) 5.09 → todas ≥4.5. Sobre paper-2 #EFE8DB: block-2 4.33 y block-3-text 4.18 → no usar texto de bloque sobre paper-2.

Reglas:
- Nunca solo color: siempre letra L/M/P (insignia 18×18, radio 5, letra blanca) junto al nombre o filtro.
- Tira bajo celda de rejilla: `--block-1/2/3`. Texto o insignia: `--block-1`, `--block-2`, `--block-3-text`.
- `--terra-*` no se usa para bloques (reservado a «Marcada» y CTA); `--gold-*` no se usa para bloques.
- Orden fijo L → M → P en filtros, leyendas y resultados.

Añadir en `src/index.css:5` (`:root`):
`--block-1:#15393F; --block-2:#577075; --block-3:#8A7F70; --block-3-text:#766D60;`

Criterio de aceptación adicional:
```sh
! grep -nE 'block-3\)' src/index.css | grep -E '(^|[^-])color:'   # block-3 nunca como color de texto
```
