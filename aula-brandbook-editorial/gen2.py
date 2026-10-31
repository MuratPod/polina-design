import json,pathlib,functools,re
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.boundsPen import BoundsPen
T=json.load(open('tokens/_t.json'));B=T['brand'];N=T['neutral'];V=T['vertical'];D=T['dark']
NV,GD,PP=B['navy'],B['gold'],B['paper']
FF={'serif':'fonts/fraunces-latin-wght.woff2','sans':'fonts/ibm-plex-sans-latin-wght.woff2'}
@functools.lru_cache(None)
def font(k,w): return instantiateVariableFont(TTFont(FF[k]),{'wght':w})
def tp(text,size,k='serif',w=600,x=0,y=0,track=0):
  f=font(k,w);gs=f.getGlyphSet();cm=f.getBestCmap();s=size/f['head'].unitsPerEm;pen=SVGPathPen(gs);cx=0
  for ch in text:
    g=cm[ord(ch)];gs[g].draw(TransformPen(pen,(s,0,0,-s,x+cx,y)));cx+=gs[g].width*s+track
  return pen.getCommands(),cx-track
def P(d,c): return f'<path d="{d}" fill="{c}"/>'
def wordmark(c,dot,x,y,size):
  d,w=tp('Aula',size,x=x,y=y,track=-size*0.01);d2,w2=tp('.',size,x=x+w+size*0.005,y=y);return P(d,c)+P(d2,dot),w+w2
def mark(bg,fg,dot,x,y,s,rx=0.2):
  d,w=tp('A',s*0.66,w=600);d2,w2=tp('.',s*0.66,w=600);tot=w+w2;ox=x+(s-tot)/2;oy=y+s*0.70
  da,_=tp('A',s*0.66,x=ox,y=oy);db,_=tp('.',s*0.66,x=ox+w,y=oy)
  r=f'<rect x="{x}" y="{y}" width="{s}" height="{s}" rx="{s*rx}" fill="{bg}"/>' if bg else ''
  return r+P(da,fg)+P(db,dot)
def save(n,w,h,body,bg=None):
  r=f'<rect width="{w}" height="{h}" fill="{bg}"/>' if bg else ''
  open(f'logo/{n}.svg','w').write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {int(w)} {int(h)}" width="{int(w)}" height="{int(h)}">{r}{body}</svg>')
NAMES={'museos':'Museos','justicia':'Justicia','policia':'Policía','educacion':'Educación'}
LOG=[]
VARS=[('horizontal',NV,GD,N['muted'],None),('on-dark',PP,GD,D['muted'],'d'),('mono','#000000','#000000','#000000','m')]
for key in ['umbrella']+list(V):
  for var,c,dot,sub,mode in VARS:
    wm,ww=wordmark(c,dot,16,76,72);body=wm;W=ww+32
    if key!='umbrella':
      mc=('#000000' if mode=='m' else V[key]['dark' if mode=='d' else 'light']);x0=16+ww+22
      lab,lw=tp(NAMES[key],30,'sans',500,x0+20,74)
      body+=f'<rect x="{x0}" y="52" width="12" height="12" rx="2" fill="{mc}"/>'+P(lab,sub);W=x0+20+lw+20
    save(f'aula-{key}-{var}',W,100,body);LOG.append(f'aula-{key}-{var}')
# stacked + mark
for var,bg,fg,dot,wc in [('light',NV,PP,GD,NV),('dark',PP,NV,GD,PP),('mono','#000','#fff','#fff','#000')]:
  wm,ww=wordmark(wc,dot if var!='mono' else '#000',0,0,56)
  wm,ww=wordmark(wc,dot if var!='mono' else '#000',(220-ww)/2,190,56)
  save(f'aula-stacked-{var}',220,214,mark(bg,fg,dot,60,10,100)+wm);LOG.append(f'aula-stacked-{var}')
  save(f'aula-mark-{var}',96,96,mark(bg,fg,dot,8,8,80));LOG.append(f'aula-mark-{var}')
# clear space: x = cap height ~ 0.7*size
wm,ww=wordmark(NV,GD,70,126,72)
cs=f'<rect x="20" y="20" width="{ww+100}" height="150" fill="none" stroke="#3A566B" stroke-dasharray="5 5"/><rect x="70" y="72" width="{ww}" height="56" fill="none" stroke="#D9A21B" stroke-width="1"/>'+P(tp('zona de respeto = x (altura de la «A»)',13,'sans',500,24,196)[0],'#4A5068')
save('aula-clearspace',ww+140,210,cs+wm,PP)
json.dump(LOG,open('logo/_list.json','w'))
# app icon / favicon / adaptive
open('app-icon/aula-app-icon.svg','w').write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024"><rect width="1024" height="1024" fill="{NV}"/>{mark(None,PP,GD,112,100,800)}</svg>')
open('favicon/favicon.svg','w').write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">{mark(NV,PP,GD,0,0,64,0.22)}</svg>')
open('app-icon/android-adaptive-foreground.svg','w').write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 108 108">{mark(None,PP,GD,24,23,60)}</svg>')
open('app-icon/android-adaptive-background.svg','w').write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 108 108"><rect width="108" height="108" fill="{NV}"/></svg>')
open('app-icon/android-adaptive-monochrome.svg','w').write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 108 108">{mark(None,"#000","#000",24,23,60)}</svg>')
open('app-icon/ic_launcher.xml','w').write('<?xml version="1.0" encoding="utf-8"?>\n<!-- res/mipmap-anydpi-v26/ic_launcher.xml -->\n<adaptive-icon xmlns:android="http://schemas.android.com/apk/res/android">\n  <background android:drawable="@drawable/ic_launcher_background"/>\n  <foreground android:drawable="@drawable/ic_launcher_foreground"/>\n  <monochrome android:drawable="@drawable/ic_launcher_monochrome"/>\n</adaptive-icon>\n')
# icons: same 24px grid, thinner 1.5 stroke for editorial calm
src=pathlib.Path('../design/icons');L=json.load(open(src/'_list.json'))
for k in L: (pathlib.Path('icons')/f'{k}.svg').write_text((src/f'{k}.svg').read_text().replace('stroke-width="2"','stroke-width="1.5"'))
json.dump(L,open('icons/_list.json','w'))
print(len(LOG),'logos',len(L),'icons')
