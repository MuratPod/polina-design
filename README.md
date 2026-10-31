# Aula Museos — prototipo de concepto (v0.3)

Prototipo clicable, mobile-first, para la app de preparación de la oposición
**Escala de Ayudantes de Museos del Estado**. Demo en línea: https://muratpod.github.io/polina-design/ (el repositorio mantiene por ahora el nombre técnico `polina-design`). Sin código de producción: es solo un mock para evaluar dirección visual y flujos.

## Archivos
- `index.html` — moodboard (arriba) + prototipo clicable en marco de teléfono (390 px) + notas por pantalla. Un solo archivo, CSS/JS embebidos, sin compilación.
- `CONCEPTO.md` — concepto para Polina (español).
- `RESUMEN-MURAT.md` — resumen breve (ruso).
- `brandbook/` — manual de marca v1 (HTML + PDF + logotipos SVG). En línea: https://muratpod.github.io/polina-design/brandbook/
- `aula-umbrella/brandbook/` — **manual de marca de la plataforma Aula (dirección C · Atrio, v1)**: logotipo y símbolo, paleta y verticales, tipografía, voz, lockups, iconos, UI tokens (`aula-tokens.css/json`), examen. HTML + PDF + ZIP. En línea: https://muratpod.github.io/polina-design/aula-umbrella/brandbook/
- `aula-umbrella/brandbook-justicia/` — **manual de vertical Aula Justicia v1** (azul toga #14304D + ámbar #B07A2A): lockups y sublockups por cuerpo, color, citación normativa, voz, iconografía, icono/OG, tokens `aula-justicia-tokens.css`, pantallas. En línea: https://muratpod.github.io/polina-design/aula-umbrella/brandbook-justicia/
- `CHANGELOG.md` — historial de versiones (v0.3: nombre Aula Museos).
- `CHANGELOG-v0.2.md` — qué cambió en v0.2 (feedback de Polina).

## Cómo abrirlo
**Opción A — doble clic:** abre `index.html` en Chrome, Safari, Firefox o Edge (`file://…/index.html`).

**Opción B — servidor local** (recomendado para compartir en la red local o abrir en el móvil):
```bash
cd polina-design
python3 -m http.server 8000
# abre http://localhost:8000
```

Las fuentes (Source Serif 4 + Inter) se cargan de Google Fonts; sin conexión se usan Georgia y la fuente del sistema.

## Navegación
- Barra inferior del teléfono: Inicio · Estudiar · Catalogar · Actualidad · Tutor.
- Lista de pantallas a la izquierda (salto directo a cualquiera de las 13 vistas).
- Enlace directo por hash: `index.html#fb-err`, `#sim-run`, `#ficha-fb`, `#sim-res`, `#ajustes`…
- Tecla ← o botón atrás para volver.
- En la lección: elige **B** → feedback de acierto; cualquier otra → feedback de error. En la pantalla de feedback hay un selector Acierto/Error.
- En pantallas < 430 px de ancho el teléfono ocupa toda la pantalla (útil para probar en un móvil real).
- Modo prueba: Estudiar → tarjeta «Modo prueba» → feedback tras cada respuesta. Modo examen: Estudiar → «Modo examen» → Empezar → «Entregar y ver resultados».
