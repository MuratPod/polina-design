# Aula Museos · CHANGELOG

## Web v0.1 (31 oct 2026) — `app/index.html`
App web funcional (un solo HTML, sin dependencias) publicada en GitHub Pages: https://muratpod.github.io/polina-design/app/
- Flujo completo: bienvenida/inicio → elegir tema (3 bloques + «Todos») → modo prueba o examen → resultado → revisión.
- **Modo prueba:** sin nota; tras cada respuesta (o «No lo sé»), explicación didáctica, fuente oficial con nivel en la jerarquía (8 niveles, BNE enlazada) y repaso final.
- **Modo examen:** cronómetro (1 min/pregunta), recuento en vivo respondidas / en blanco / pendientes, leyenda +1 · 0 · −1/3, botón «Dejar en blanco» con estado propio (discontinuo), mapa de preguntas, sin feedback hasta entregar.
- **Resultado:** aciertos/errores/blancos, barra tricolor, fórmula aplicada, netos y nota sobre 10 (orientativa), revisión pregunta a pregunta con chip +1 / −1/3 / 0, «Practicar fallos y blancos» en modo prueba.
- **Contenido IA (placeholder RAG):** bloque etiquetado «✦ Contenido IA» con texto + citas `{ text, citations:[{title,url,boeId,sourceLevel}] }`; `fetchAiAnswer()` y `AI_ENDPOINT` listos para conectar la API.
- 12 preguntas de ejemplo con fuentes BOE verificadas (Ley 16/1985, RD 620/1987, CE, Ley 39/2015, TREBEP, Ley 46/2003).
- El prototipo de concepto v0.3 (`index.html`) y el brandbook quedan como referencia; sin cambios.

## Brandbook v1 (30 oct 2026)
- `brandbook/index.html` (+ PDF): logotipo principal/apilado/mono/inverso, monograma AM, paleta, tipografía, voz y tono, principios UI, componentes, pantallas de ejemplo, nota de dominios (OEPM/EUIPO pendiente).
- SVG en `brandbook/logos/` (texto aún sin convertir a contornos).

## v0.3 — brand lock (30 oct 2026)
- Nombre de producto aprobado: **Aula Museos** (sustituye al nombre de trabajo «Sala»).
- `index.html`: `<title>`, meta description/og, eyebrow de cabecera, H1 e intro → Aula Museos. Inicio: etiqueta «Mi aula · jueves…» y botón principal «Continuar en el aula».
- Docs actualizados: README, CONCEPTO, RESUMEN-MURAT, encabezado de CHANGELOG-v0.2.
- Sin cambios: la palabra «sala» cuando significa sala de museo (p. ej. «la calma de una sala de museo», color «Verde sala», moodboard «Sala en penumbra», noticia «Reapertura de la sala de orfebrería»); referencias a Polina como persona/revisora y el saludo de ejemplo «Buenas tardes, Polina».
- Repo y URL siguen como `polina-design` por ahora. 
- RU: бренд зафиксирован — «Sala» → **Aula Museos** в прототипе и документах; брендбук ждёт брифа.

## v0.2
Ver `CHANGELOG-v0.2.md`.
