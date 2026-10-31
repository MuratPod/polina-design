import pathlib
from playwright.sync_api import sync_playwright
def shots(jobs):
  # jobs: (html_path, out_png, w, h, dpr, full)
  with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/usr/bin/google-chrome')
    for src,out,w,h,d,full in jobs:
      pg=b.new_page(viewport={'width':w,'height':h},device_scale_factor=d)
      pg.goto(pathlib.Path(src).resolve().as_uri());pg.wait_for_load_state('networkidle');pg.evaluate('document.fonts.ready');pg.wait_for_timeout(150)
      pathlib.Path(out).parent.mkdir(parents=True,exist_ok=True);pg.screenshot(path=out,full_page=full,omit_background=True);pg.close()
    b.close()
