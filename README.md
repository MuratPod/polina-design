# Sala — prototipo de concepto (v0.1)

Prototipo clicable, mobile-first, para la app de preparación de la oposición
**Escala de Ayudantes de Museos del Estado**. Sin código de producción: es solo un mock para evaluar dirección visual y flujos.

## Archivos
- `index.html` — moodboard (arriba) + prototipo clicable en marco de teléfono (390 px) + notas por pantalla. Un solo archivo, CSS/JS embebidos, sin compilación.
- `CONCEPTO.md` — concepto para Polina (español).
- `RESUMEN-MURAT.md` — resumen breve (ruso).

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
- Lista de pantallas a la izquierda (salto directo a cualquiera de las 12 vistas).
- Enlace directo por hash: `index.html#fb-err`, `#sim-run`, `#ficha-fb`, `#ajustes`…
- Tecla ← o botón atrás para volver.
- En la lección: elige **B** → feedback de acierto; cualquier otra → feedback de error. En la pantalla de feedback hay un selector Acierto/Error.
- En pantallas < 430 px de ancho el teléfono ocupa toda la pantalla (útil para probar en un móvil real).
