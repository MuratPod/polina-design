import pathlib
from playwright.sync_api import sync_playwright
CHK='''()=>{const W=document.documentElement.clientWidth,o=[];for(const e of document.querySelectorAll('body *')){const r=e.getBoundingClientRect();if(r.width&&(r.right>W+1||r.left<-1)&&!e.closest('[data-ovok]'))o.push(e.tagName+'.'+e.className+':'+Math.round(r.right));if(e.scrollWidth>e.clientWidth+1&&getComputedStyle(e).overflowX!='visible'&&!e.closest('[data-ovok]')&&e.clientWidth>0)o.push('scroll:'+e.tagName+'.'+e.className)}return o.slice(0,5)}'''
def shots(jobs):
  bad=[]
  with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/usr/bin/google-chrome')
    for src,out,w,h,d,full in jobs:
      pg=b.new_page(viewport={'width':w,'height':h},device_scale_factor=d)
      pg.goto(pathlib.Path(src).resolve().as_uri());pg.wait_for_load_state('networkidle');pg.evaluate('document.fonts.ready');pg.wait_for_timeout(150)
      if w>1: 
        o=pg.evaluate(CHK)
        if o: bad.append((src,o))
      pathlib.Path(out).parent.mkdir(parents=True,exist_ok=True);pg.screenshot(path=out,full_page=full,omit_background=True);pg.close()
    b.close()
  for x in bad: print('OVERFLOW',x)
  return bad
