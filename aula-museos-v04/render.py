import pathlib
from playwright.sync_api import sync_playwright
H=pathlib.Path(__file__).parent.resolve(); out=H/'png'; out.mkdir(exist_ok=True)
with sync_playwright() as p:
    b=p.chromium.launch()
    pg=b.new_page(viewport={'width':390,'height':844},device_scale_factor=2)
    for n in range(1,12):
        pg.goto((H/f'screen-{n:02d}.html').as_uri()); pg.wait_for_load_state('networkidle'); pg.evaluate('document.fonts.ready')
        pg.screenshot(path=str(out/f'screen-{n:02d}.png'))
    for f,w in [('board-simulacro',2300),('board-leccion',1900),('board-oficial-ajustes',1100)]:
        pg=b.new_page(viewport={'width':w,'height':900},device_scale_factor=1.5)
        pg.goto((H/f'{f}.html').as_uri()); pg.wait_for_load_state('networkidle'); pg.evaluate('document.fonts.ready')
        pg.screenshot(path=str(out/f'{f}.png'),full_page=True)
    pg=b.new_page(viewport={'width':1440,'height':900},device_scale_factor=1.5)
    pg.goto((H/'desktop-simulacro.html').as_uri()); pg.wait_for_load_state('networkidle'); pg.evaluate('document.fonts.ready')
    pg.screenshot(path=str(out/'desktop-simulacro.png'))
    b.close()
print('rendered')
