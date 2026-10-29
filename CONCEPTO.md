# Sala · Concepto de diseño v0.1
*«Duolingo para opositores» — Escala de Ayudantes de Museos del Estado*

> **Importante:** todas las preguntas, explicaciones, noticias, fichas y puntuaciones del prototipo son **contenido de ejemplo** (placeholders ilustrativos). Lo que simula ser generado por IA lleva siempre la etiqueta **«Contenido IA»** y un enlace a la fuente al lado. «Sala» es un nombre provisional.

## 1. Dirección visual
La app debe sentirse como una sala de museo bien iluminada: calma, orden y una pieza cada vez. El color principal es una **tinta verde azulado profunda** (#15393F) sobre fondos **papel** cálidos (#F6F1E8), con **terracota** y **oro pátina** reservados solo para racha y XP, para que la motivación se note sin gritar. Los títulos y las preguntas van en una serif editorial (**Source Serif 4**), que da seriedad de catálogo; la interfaz y el texto largo en **Inter**, muy legible. Tarjetas con esquinas generosas y sombras suaves; los errores se muestran en tonos cálidos y amables, nunca en rojo alarma. Tres palabras: **Sereno. Riguroso. Cálido.** — «examen sin pánico».

## 2. Mapa de navegación
- **Barra inferior (móvil):** Inicio · Estudiar · Catalogar · Actualidad · Tutor
- **Inicio** → Lección (siguiente paso / nodo del camino) → Feedback (acierto / error) → vuelta al Inicio
- **Inicio** → nodo «Repaso del bloque» → Simulacro (inicio)
- **Inicio / Tutor** → icono de ajustes → Ajustes de convocatoria
- **Estudiar** → Test temático → Lección → Feedback
- **Estudiar** → Simulacro (inicio) → Simulacro en curso (modo foco, sin barra inferior)
- **Catalogar** → Ficha → Revisión campo a campo → Corregir ficha / Ver progreso (Tutor)
- **Actualidad** → filtros → tarjeta → fuente externa (BOE / web del museo)
- **Tutor** → sesión recomendada → Lección; último simulacro → Repetir
- **Escritorio (≥1024 px):** la barra inferior pasa a barra lateral izquierda; contenido central de máx. 680–760 px; panel derecho contextual (explicación, fuente, objetivo semanal).

## 3. Pantallas: para qué, qué tomamos y qué rechazamos

| # | Pantalla | Para qué | Tomamos de los patrones tipo Duolingo | Rechazamos conscientemente |
|---|---|---|---|---|
| 1 | **Inicio / Camino** | Saber en 3 s qué toca hoy y cuánto falta para el objetivo semanal | Camino de nodos por bloques (Legislación, Museología, Patrimonio); un único «siguiente paso»; racha y XP pequeños | Mascota, confeti, sonidos; ligas y rankings; vidas/corazones que bloquean el estudio |
| 2 | **Lección / pregunta** | Responder un test de 4 opciones con calma | Barra de progreso de la lección; «Comprobar» que se activa al elegir; salida «No lo sé» sin castigo | Cronómetro obligatorio en modo estudio (desactivado por defecto, opcional); pérdida de vidas |
| 3 | **Feedback (acierto / error)** | Fijar el porqué y convertir el error en aprendizaje | +XP discreto; coaching suave; la pregunta fallada vuelve en repaso espaciado (1-3-7 días) | Celebración exagerada; rojo agresivo; explicaciones IA sin etiqueta ni fuente (siempre «Contenido IA» + «Abrir fuente» BOE) |
| 4 | **Simulacro** (inicio + en curso) | Reproducir las condiciones reales: 100 + 10 reserva, 100 min, −1/3 por error, en blanco sin penalización (ref. BOE-A-2025-26893) | Pantalla de preparación clara; progreso visible; mapa de preguntas | Cualquier gamificación durante el examen: sin XP, sin racha, sin feedback, sin barra inferior (modo foco) |
| 5 | **Catalogación — ficha** | Practicar el ejercicio práctico con una pieza y campos normalizados (Museo, Inventario, Objeto, Autor, Título, Materia, Técnica, Dimensiones, Datación, Contexto, Descripción) | Tarea corta y concreta (1 pieza); autoguardado | Autocompletado que haga la ficha por ti |
| 6 | **Catalogación — revisión** | Ver campo a campo: **bien / mejorar / falta**, con motivo breve y puntos orientativos; rúbrica; fuente CER.es / normalización documental | Feedback inmediato; siguiente paso claro («Corregir ficha») | Nota única sin explicación; presentar la nota como oficial |
| 7 | **Actualidad** | Estar al día (BOE, museos estatales) y ver qué tema del temario toca cada noticia | Tarjetas breves, filtros por chips | Feed infinito tipo red social; resúmenes sin enlace al original |
| 8 | **Progreso / Tutor** | Saber qué reforzar y qué hacer en la próxima sesión | Objetivo semanal; racha flexible; recomendación personalizada | Comparación con otros usuarios; racha que se pierde por un día de descanso (se permite 1 día de descanso/semana) |
| 9 | **Ajustes de convocatoria** | Elegir convocatoria y ajustar parámetros; aviso de que la puntuación no es oficial | Opción de ocultar XP y racha | Notificaciones culpabilizadoras |

## 4. Prioridad para la prueba de concepto (PoC)
Los **dos primeros flujos** a validar con usuarios reales:
1. **Test temático:** Inicio → Lección → Feedback (acierto/error con IA marcada + fuente BOE) → Inicio.
2. **Una ficha de catalogación:** Catalogar → Ficha → Revisión campo a campo.

Simulacro, Actualidad, Tutor y Ajustes se muestran para dar visión completa, pero pueden llegar después.

## 5. Para validar contigo
- Nombre provisional «Sala» y paleta tinta + papel + terracota/oro.
- Nivel de gamificación: XP y racha visibles por defecto (se pueden ocultar), sin ligas ni vidas.
- Racha con 1 día de descanso semanal sin perderla.
- Campos de la ficha de catalogación y rúbrica orientativa (Identificación 3 · Datos técnicos 3 · Descripción 2 · Terminología 2) — **propuesta nuestra, no oficial**: necesitamos tu criterio o el de un preparador.
- Parámetros del simulacro (100+10, 100 min, −1/3) según BOE-A-2025-26893: confírmalos con las bases.
- Bloques del camino (Legislación · Museología · Patrimonio): estructura de ejemplo, no el temario oficial completo.
- Tono de los textos: tuteo cercano en el estudio; tono más formal en el simulacro.
