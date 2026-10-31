# tokens, contrast, competitor dE
import json,pathlib
from colorlib import *
for d in ['logo/png','icons','app-icon','favicon','tokens','png','screens','web','templates','ui']: pathlib.Path(d).mkdir(parents=True,exist_ok=True)
T={'brand':{'navy':'#142A3D','navy-800':'#1E3A52','navy-600':'#3A566B','gold':'#D9A21B','gold-700':'#856000','gold-100':'#F6EBCB','paper':'#F4F1EA'},
 'neutral':{'bg':'#F4F1EA','surface':'#FFFFFF','surface-2':'#EFEBE3','line':'#DCD5C6','ink':'#142A3D','muted':'#4A5068','subtle':'#66697F'},
 'semantic':{'success':'#0E7A6E','success-100':'#E6F5F2','error':'#B42318','error-100':'#FBE6E3','warning':'#8F5300','warning-100':'#FBEFD9','ai':'#5B3FC4','ai-100':'#EEEAFB'},
 'dark':{'bg':'#0E1C27','surface':'#172A38','surface-2':'#213848','line':'#34505F','ink':'#F4F1EA','muted':'#B9BCC8','subtle':'#9A9EAE','gold':'#E3B341','success':'#4CC2B0','error':'#FF8F84','warning':'#E8B160','ai':'#B7A6FF'},
 'vertical':{'museos':{'light':'#94502F','dark':'#E7A07C'},'justicia':{'light':'#8E2C7A','dark':'#E58BD3'},'policia':{'light':'#00728F','dark':'#4FC3E0'},'educacion':{'light':'#4F7A1F','dark':'#A7D46B'}},
 'radius':{'sm':'6px','md':'10px','lg':'16px','pill':'999px'},'space':{'1':'4px','2':'8px','3':'12px','4':'16px','5':'24px','6':'32px','7':'48px','8':'64px'},
 'font':{'serif':"'Fraunces', Georgia, serif",'sans':"'IBM Plex Sans', system-ui, sans-serif",'mono':"'IBM Plex Mono', ui-monospace, monospace"},
 'type':{'display':'Fraunces 48/1.08 600 −0.01em','h1':'Fraunces 34/1.15 600','h2':'Fraunces 26/1.2 600','h3':'Plex Sans 19/1.3 600','body':'Plex Sans 16/1.55 400','small':'Plex Sans 14/1.5 400','caption':'Plex Sans 12/1.4 500 · 0.04em','mono':'Plex Mono 14/1.6 500'},
 'shadow':{'1':'0 1px 0 rgba(20,42,61,.06),0 2px 8px rgba(20,42,61,.05)'}}
json.dump(T,open('tokens/aula-tokens.json','w'),ensure_ascii=False,indent=2);json.dump(T,open('tokens/_t.json','w'))
css=[':root{']
for g in ['brand','neutral','semantic']:
  css+= [f'  --{k}:{v};' for k,v in T[g].items()]
css+=[f'  --r-{k}:{v};' for k,v in T['radius'].items()]+[f'  --s-{k}:{v};' for k,v in T['space'].items()]+[f'  --font-{k}:{v};' for k,v in T['font'].items()]+[f'  --sh-1:{T["shadow"]["1"]};']
css+=[f'  --v-{k}:{v["light"]};' for k,v in T['vertical'].items()]+['  --primary:var(--navy);--on-primary:var(--paper);--gold-text:var(--gold-700);','}']
css.append('[data-theme="dark"]{'+''.join(f'--{k}:{v};' for k,v in T['dark'].items())+'--primary:#F4F1EA;--on-primary:#142A3D;--gold-text:#E3B341;--gold-100:#3A3220;--success-100:#123A37;--error-100:#45201E;--warning-100:#3E2E14;--ai-100:#2A2550;--surface-2:#213848;'+''.join(f'--v-{k}:{v["dark"]};' for k,v in T['vertical'].items())+'}')
css+=[f'[data-vertical="{k}"]{{--accent-v:var(--v-{k});}}' for k in T['vertical']]
open('tokens/aula-tokens.css','w').write('\n'.join(css)+'\n')
rows=[];N=T['neutral'];B=T['brand'];S=T['semantic'];D=T['dark'];bg=N['bg'];W='#FFFFFF'
def add(n,f,b,use):
  r=cr(f,b);rows.append(dict(name=n,fg=f,bg=b,ratio=r,AA=r>=4.5,AA_large=r>=3,use=use))
add('ink sobre papel',N['ink'],bg,'texto');add('ink sobre blanco',N['ink'],W,'texto en tarjeta');add('muted sobre papel',N['muted'],bg,'secundario');add('subtle sobre papel',N['subtle'],bg,'captions (corregido)');add('subtle sobre blanco',N['subtle'],W,'captions en tarjeta');add('subtle sobre surface-2',N['subtle'],N['surface-2'],'captions en gris')
add('papel sobre navy',B['paper'],B['navy'],'botón primario');add('gold sobre papel',B['gold'],bg,'solo marcador/relleno, nunca texto');add('navy sobre gold',B['navy'],B['gold'],'chip/botón dorado');add('gold-700 sobre papel',B['gold-700'],bg,'texto dorado');add('gold-700 sobre blanco',B['gold-700'],W,'texto dorado en tarjeta');add('gold-700 sobre gold-100',B['gold-700'],B['gold-100'],'chip XP');add('gold sobre navy',B['gold'],B['navy'],'acento en navy')
for k in ['success','error','warning','ai']: add(f'{k} sobre papel',S[k],bg,'texto/icono');add(f'{k} sobre {k}-100',S[k],S[k+'-100'],'badge/aviso')
for k in ['ink','muted','subtle','gold','success','error','warning','ai']: add(f'oscuro {k} sobre bg',D[k],D['bg'],'modo oscuro');add(f'oscuro {k} sobre surface',D[k],D['surface'],'tarjeta oscura')
for k,v in T['vertical'].items(): add(f'{k} sobre papel',v['light'],bg,'marcador/texto');add(f'{k} oscuro sobre bg oscuro',v['dark'],D['bg'],'marcador oscuro')
REF={'OpositaTest navy':'#253B80','OpositaTest naranja':'#EF7746','MAD navy':'#11184A','MAD rojo':'#EC4249'}
comp=[dict(ours=n,hex=h,ref=rn,refhex=rh,dE2000=de2000(h,rh)) for n,h in [('navy','#142A3D'),('gold','#D9A21B'),('gold-700','#856000')] for rn,rh in REF.items()]
alt=dict(hex='#142A3D',vs_MAD=de2000('#142A3D','#11184A'),vs_OT=de2000('#142A3D','#253B80'),on_paper=cr('#142A3D',bg))
json.dump(dict(contrast=rows,competitors=comp,navy_alternative=alt),open('tokens/contrast.json','w'),ensure_ascii=False,indent=1)
print([(r['name'],r['ratio']) for r in rows if not r['AA']]);print([(c['ours'],c['ref'],c['dE2000']) for c in comp]);print(alt)
