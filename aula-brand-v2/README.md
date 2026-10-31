# Aula brand v2 — exploración (кандидат вместо Atrio)

Только исследование. В продукты ничего не вносится. Отправная точка: тёмно-синий градиент + золотые буквы.
- `direction-a/` Noche de estudio · `direction-b/` Constelación (в каждом: `logo-aula.svg`, `palette.json` с контрастом, `mobile.html/png`, `README.md`).
- `compare.png` — сравнение рядом. Сборка: `python3 build.py && python3 mock.py` (Playwright).
- Шрифты: woff2 с Fontsource (latin, wght variable), все по SIL OFL 1.1.
- Контраст: WCAG 2.x. Порог 4.5:1 для текста, 3:1 для крупного. Расчёт в `build.py`.
