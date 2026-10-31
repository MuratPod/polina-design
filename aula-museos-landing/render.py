import pathlib
from playwright.sync_api import sync_playwright
H=pathlib.Path(__file__).parent.resolve()
with sync_playwright() as p:
    b=p.chromium.launch()
    for name,w,h in [('landing-desktop-1280',1280,800),('landing-mobile-390',390,844)]:
        pg=b.new_page(viewport={'width':w,'height':h},device_scale_factor=1.5 if w>400 else 2)
        pg.goto((H/'index.html').as_uri()); pg.wait_for_load_state('networkidle'); pg.evaluate('document.fonts.ready')
        pg.screenshot(path=str(H/'png'/f'{name}.png'),full_page=True)
    b.close()
with sync_playwright() as p:
    b=p.chromium.launch()
    pg=b.new_page(viewport={'width':1280,'height':800},device_scale_factor=1.5)
    pg.goto((H/'index.html').as_uri()); pg.wait_for_load_state('networkidle'); pg.evaluate('document.fonts.ready')
    pg.locator('#ia-ejemplo').screenshot(path=str(H/'png'/'crop-ia-ejemplo.png'))
    pg.locator('#faq').screenshot(path=str(H/'png'/'crop-faq.png'))
    b.close()
