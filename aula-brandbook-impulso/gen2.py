import json,pathlib,functools
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
T=json.load(open('tokens/_t.json'));B=T['brand'];N=T['neutral'];V=T['vertical']
@functools.lru_cache(None)
def font(w):
  f=TTFont('fonts/nunito-latin-ext-wght.woff2') if False else TTFont('fonts/nunito-latin-wght.woff2');return instantiateVariableFont(f,{'wght':w})
def tp(text,size,w=900,x=0,y=0,track=0):
  f=font(w);gs=f.getGlyphSet();cmap=f.getBestCmap();upm=f['head'].unitsPerEm;s=size/upm;pen=SVGPathPen(gs);cx=0
  for ch in text:
    g=cmap[ord(ch)];tpen=TransformPen(pen,(s,0,0,-s,x+cx,y));gs[g].draw(tpen);cx+=gs[g].width*s+track
  return pen.getCommands(),cx-track
NAMES={'museos':'museos','justicia':'justicia','policia':'policía','educacion':'educación'}
def symbol(fill,fg,x=0,y=0,s=64,dot=None):
  d,w=tp('a',s*0.78,900);d2,w2=tp('!',s*0.78,900)
  # center 'a!' combined
  tot=w+w2-s*0.03;ox=x+(s-tot)/2;oy=y+s*0.70
  da,_=tp('a',s*0.78,900,ox,oy);db,_=tp('!',s*0.78,900,ox+w-s*0.03,oy)
  return f'<rect x="{x}" y="{y}" width="{s}" height="{s}" rx="{s*0.28}" fill="{fill}"/><path d="{da}" fill="{fg}"/><path d="{db}" fill="{dot or fg}"/>'
def wordmark(c,bang,x,y,size):
  d,w=tp('aula',size,900,x,y);d2,w2=tp('!',size,900,x+w+size*0.02,y);return f'<path d="{d}" fill="{c}"/><path d="{d2}" fill="{bang}"/>',w+w2+size*0.02
def save(name,w,h,body,bg=None):
  r=f'<rect width="{w}" height="{h}" fill="{bg}"/>' if bg else ''
  open(f'logo/{name}.svg','w').write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">{r}{body}</svg>')
LOG=[]
def set_for(key,label,acc_l,acc_d):
  sub=lambda c,x: (lambda p:(f'<path d="{p[0]}" fill="{c}"/>',p[1]))(tp(label,30,800,x,82)) if label else ('',0)
  # horizontal light
  for var,bg,sym,symfg,wm,bang,subc,dot in [('horizontal',None,acc_l,'#FFFFFF',N['ink'],B['coral'],acc_l,None),
      ('on-dark',None,B['gold'],B['navy-900'],B['gold'],B['coral'] if not label else acc_d,acc_d,None),
      ('mono',None,'#000000','#FFFFFF','#000000','#000000','#000000',None)]:
    s=symbol(sym,symfg,16,16,72);wmb,ww=wordmark(wm,bang,104,74,60);sb,sw=sub(subc,104+ww+12)
    W=int(104+ww+12+sw+20);save(f'aula-{key}-{var}',W,104,s+wmb+sb,bg);LOG.append(f'aula-{key}-{var}')
  for var,f,fg,bg in [('symbol',acc_l,'#FFFFFF',None),('symbol-dark',B['gold'],B['navy-900'],None),('symbol-mono','#000000','#FFFFFF',None)]:
    save(f'aula-{key}-{var}',96,96,symbol(f,fg,8,8,80),bg);LOG.append(f'aula-{key}-{var}')
set_for('umbrella','',B['coral'],B['coral'])
for k,v in V.items(): set_for(k,NAMES[k],v['light'],v['dark'])
# umbrella wordmark only (light / dark) + clear space diagram
wmb,ww=wordmark(N['ink'],B['coral'],20,80,80);save('aula-wordmark',int(ww+40),110,wmb);
wmb,ww=wordmark(B['gold'],B['coral'],20,80,80);save('aula-wordmark-dark',int(ww+40),110,wmb,B['navy-900'])
s=symbol(B['coral'],'#FFFFFF',60,60,72);wmb,ww=wordmark(N['ink'],B['coral'],148,118,60)
cs=f'<rect x="30" y="30" width="{ww+148-30+30}" height="132" fill="none" stroke="#2E5BFF" stroke-dasharray="6 5"/><text x="34" y="24" font-family="Nunito,sans-serif" font-size="13" fill="#2449D8">zona de respeto = x (altura de la «a»)</text>'
save('aula-clearspace',int(ww+148+60),200,cs+s+wmb,'#FFF8EC')
json.dump(LOG,open('logo/_list.json','w'))
# app icon master + favicon svg
open('app-icon/aula-app-icon.svg','w').write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024"><defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#FF4250"/><stop offset="1" stop-color="#E5233F"/></linearGradient></defs><rect width="1024" height="1024" fill="url(#g)"/>{symbol("none","#FFFFFF",112,112,800,B["gold"]).replace(chr(60)+"rect","<rect opacity=\"0\"",1)}</svg>')
open('favicon/favicon.svg','w').write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">{symbol(B["coral"],"#FFFFFF",0,0,64)}</svg>')
# icons 24, stroke 2
I={'home':'<path d="M3 11l9-7 9 7v9a1 1 0 0 1-1 1h-5v-6H9v6H4a1 1 0 0 1-1-1z"/>','book':'<path d="M4 5a2 2 0 0 1 2-2h13v16H6a2 2 0 0 0-2 2z"/><path d="M4 21V5M8 7h7"/>','flame':'<path d="M12 3c1 4 6 6 6 11a6 6 0 0 1-12 0c0-3 2-4 2-7 2 1 3 2 3 4 1-2 1-5 1-8z"/>',
'star':'<path d="M12 3l2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1L3.2 9.5l6.1-.9z"/>','timer':'<circle cx="12" cy="13" r="8"/><path d="M12 9v4l3 2M9 2h6"/>','check':'<path d="M5 12l5 5 9-10"/>','x':'<path d="M6 6l12 12M18 6L6 18"/>',
'flag':'<path d="M5 21V4h11l-2 4 2 4H5"/>','chart':'<path d="M4 20V10M10 20V4M16 20v-7M22 20H2"/>','target':'<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1"/>','calendar':'<rect x="3" y="5" width="18" height="16" rx="3"/><path d="M3 10h18M8 3v4M16 3v4"/>',
'user':'<circle cx="12" cy="8" r="4"/><path d="M4 21a8 8 0 0 1 16 0"/>','settings':'<circle cx="12" cy="12" r="3"/><path d="M12 2v3M12 19v3M2 12h3M19 12h3M4.9 4.9l2.1 2.1M17 17l2.1 2.1M4.9 19.1L7 17M17 7l2.1-2.1"/>','bell':'<path d="M6 16V11a6 6 0 0 1 12 0v5l2 2H4z"/><path d="M10 21h4"/>',
'sparkle':'<path d="M12 3l1.8 5.2L19 10l-5.2 1.8L12 17l-1.8-5.2L5 10l5.2-1.8zM19 16l.8 2.2L22 19l-2.2.8L19 22l-.8-2.2L16 19l2.2-.8z"/>','source':'<path d="M10 14a4 4 0 0 0 6 0l3-3a4 4 0 0 0-6-6l-1 1"/><path d="M14 10a4 4 0 0 0-6 0l-3 3a4 4 0 0 0 6 6l1-1"/>','grid':'<rect x="3" y="3" width="7" height="7" rx="2"/><rect x="14" y="3" width="7" height="7" rx="2"/><rect x="3" y="14" width="7" height="7" rx="2"/><rect x="14" y="14" width="7" height="7" rx="2"/>',
'arrow-right':'<path d="M4 12h16M14 6l6 6-6 6"/>','arrow-left':'<path d="M20 12H4M10 6l-6 6 6 6"/>','refresh':'<path d="M20 11a8 8 0 1 0-2.3 5.7M20 4v7h-7"/>','lightbulb':'<path d="M9 18h6M10 21h4M12 3a6 6 0 0 0-4 10.5c.7.7 1 1.5 1 2.5h6c0-1 .3-1.8 1-2.5A6 6 0 0 0 12 3z"/>',
'trophy':'<path d="M7 4h10v5a5 5 0 0 1-10 0zM7 6H4a3 3 0 0 0 3 4M17 6h3a3 3 0 0 1-3 4M12 14v4M8 21h8"/>','museum':'<path d="M3 9l9-5 9 5M5 9v9M9.5 9v9M14.5 9v9M19 9v9M3 21h18"/>','scale':'<path d="M12 3v18M6 21h12M4 7h16M7 7l-3 7a3 3 0 0 0 6 0zM17 7l-3 7a3 3 0 0 0 6 0z"/>',
'shield':'<path d="M12 3l8 3v6c0 5-4 8-8 9-4-1-8-4-8-9V6z"/>','school':'<path d="M2 9l10-5 10 5-10 5zM6 11v5c3 2 9 2 12 0v-5"/>','pause':'<path d="M9 5v14M15 5v14"/>','bookmark':'<path d="M6 3h12v18l-6-4-6 4z"/>'}
for k,p in I.items(): open(f'icons/{k}.svg','w').write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">{p}</svg>')
json.dump(list(I),open('icons/_list.json','w'))
# illustrations (flat spot, no mascots)
C=B['coral'];BL=B['blue'];G=B['gold'];NV=B['navy-900'];CR='#FFE3E5'
IL={'racha':f'<circle cx="120" cy="120" r="100" fill="{B["gold-100"]}"/><path d="M120 40c8 30 48 46 48 86a48 48 0 0 1-96 0c0-24 16-32 16-56 16 8 24 16 24 32 8-16 8-40 8-62z" fill="{C}"/><path d="M120 110c4 14 22 20 22 38a22 22 0 0 1-44 0c0-10 8-16 10-26 6 4 10 8 12 14z" fill="{G}"/>',
'temario':f'<circle cx="120" cy="120" r="100" fill="#E3E9FF"/><rect x="60" y="140" width="120" height="26" rx="6" fill="{BL}"/><rect x="70" y="112" width="104" height="26" rx="6" fill="{C}"/><rect x="56" y="84" width="112" height="26" rx="6" fill="{NV}"/><rect x="70" y="92" width="60" height="6" rx="3" fill="{G}"/><circle cx="176" cy="70" r="12" fill="{G}"/>',
'simulacro':f'<circle cx="120" cy="120" r="100" fill="{CR}"/><rect x="66" y="50" width="108" height="140" rx="14" fill="#fff" stroke="{NV}" stroke-width="6"/>'+''.join(f'<rect x="84" y="{78+i*26}" width="16" height="16" rx="4" fill="{[C,BL,"#0E7A6E",G][i]}"/><rect x="108" y="{82+i*26}" width="48" height="8" rx="4" fill="#D9D3C6"/>' for i in range(4)),
'meta':f'<circle cx="120" cy="120" r="100" fill="#DDF2EE"/><circle cx="120" cy="124" r="62" fill="#fff" stroke="{NV}" stroke-width="6"/><circle cx="120" cy="124" r="38" fill="{C}"/><circle cx="120" cy="124" r="16" fill="#fff"/><path d="M120 124l52-52" stroke="{NV}" stroke-width="6" stroke-linecap="round"/><path d="M164 64l16-4-4 16z" fill="{G}"/>'}
for k,b in IL.items(): open(f'illustrations/{k}.svg','w').write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 240 240" width="240" height="240">{b}</svg>')
print(len(LOG),'logos',len(I),'icons')
# Android adaptive icon layers (108dp canvas, safe zone = central 66dp circle)
g=lambda col,dot=None: symbol('none',col,24,24,60,dot).replace('fill="none"/>','fill="none" opacity="0"/>',1)
open('app-icon/android-adaptive-foreground.svg','w').write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 108 108">{g("#FFFFFF",B["gold"])}</svg>')
open('app-icon/android-adaptive-background.svg','w').write('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 108 108"><defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#FF4250"/><stop offset="1" stop-color="#E5233F"/></linearGradient></defs><rect width="108" height="108" fill="url(#g)"/></svg>')
open('app-icon/android-adaptive-monochrome.svg','w').write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 108 108">{g("#000000")}</svg>')
open('app-icon/ic_launcher.xml','w').write('<?xml version="1.0" encoding="utf-8"?>\n<!-- res/mipmap-anydpi-v26/ic_launcher.xml · convertir los SVG a VectorDrawable (Android Studio > Vector Asset) -->\n<adaptive-icon xmlns:android="http://schemas.android.com/apk/res/android">\n  <background android:drawable="@drawable/ic_launcher_background"/>\n  <foreground android:drawable="@drawable/ic_launcher_foreground"/>\n  <monochrome android:drawable="@drawable/ic_launcher_monochrome"/>\n</adaptive-icon>\n')
