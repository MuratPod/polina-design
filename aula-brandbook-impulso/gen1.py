# tokens, contrast, logos, icons, illustrations
import json,pathlib
from colorlib import *
H=pathlib.Path('.')
for d in ['logo','logo/png','icons','illustrations','app-icon','favicon','tokens','png','screens','web','templates','ui']: (H/d).mkdir(parents=True,exist_ok=True)
T={
 'brand':{'coral':'#FF4250','coral-700':'#C8162B','coral-100':'#FFE3E5','blue':'#2E5BFF','blue-700':'#2449D8','blue-100':'#E3E9FF',
  'navy-900':'#0B1530','navy-800':'#142350','navy-700':'#1C2E63','gold':'#F2C14E','gold-700':'#7A4F00','gold-100':'#FCEFC9','amber':'#FFB020'},
 'neutral':{'bg':'#FFF8EC','surface':'#FFFFFF','surface-2':'#FBF1DF','line':'#EADFCB','ink':'#1B2140','muted':'#5A5F78','subtle':'#6A6E84'},
 'semantic':{'success':'#0E7A6E','success-100':'#DDF2EE','error':'#B42318','error-100':'#FDE4E1','warning':'#A15C00','warning-100':'#FFF0D1','ai':'#5B3FC4','ai-100':'#ECE7FF'},
 'dark':{'bg':'#0B1530','surface':'#142350','surface-2':'#1C2E63','line':'#2A3D78','ink':'#F3F5FB','muted':'#A9B4D0','gold':'#F2C14E','coral':'#FF7A85','blue':'#7C9BFF','success':'#3CC7B4','error':'#FF8A80','ai':'#B3A2FF'},
 'vertical':{'museos':{'light':'#94502F','dark':'#E7A07C'},'justicia':{'light':'#8E2C7A','dark':'#E58BD3'},'policia':{'light':'#00728F','dark':'#4FC3E0'},'educacion':{'light':'#4F7A1F','dark':'#A7D46B'}},
 'radius':{'sm':'10px','md':'16px','lg':'24px','pill':'999px'},'space':{'1':'4px','2':'8px','3':'12px','4':'16px','5':'24px','6':'32px','7':'48px','8':'64px'},
 'font':{'sans':"'Nunito', system-ui, sans-serif",'mono':"'JetBrains Mono', ui-monospace, monospace"},
 'type':{'display':'40/1.1 800','h1':'32/1.15 800','h2':'24/1.2 800','h3':'20/1.25 700','body':'16/1.5 500','small':'14/1.45 600','caption':'12/1.4 700'},
 'shadow':{'1':'0 1px 2px rgba(27,33,64,.06),0 4px 12px rgba(27,33,64,.06)','pop':'0 4px 0 rgba(27,33,64,.12)'}}
json.dump(T,open('tokens/aula-tokens.json','w'),ensure_ascii=False,indent=2)
css=[':root{']
for g in ['brand','neutral','semantic']:
  for k,v in T[g].items(): css.append(f'  --{k}:{v};')
for g in ['radius','space','shadow']:
  for k,v in T[g].items(): css.append(f'  --{g[0] if g!="shadow" else "sh"}-{k}:{v};'.replace('--r-','--r-').replace('--s-','--s-'))
for k,v in T['font'].items(): css.append(f'  --font-{k}:{v};')
for k,v in T['vertical'].items(): css.append(f'  --v-{k}:{v["light"]};')
css.append('  --accent:var(--coral);--accent-text:var(--coral-700);\n}')
css.append('[data-theme="dark"]{'+''.join(f'--{k if k not in ("gold","coral","blue","success","error","ai") else k}:{v};' for k,v in T['dark'].items())+'--coral-700:#FF7A85;--blue-700:#7C9BFF;--gold-700:#F2C14E;'+''.join(f'--v-{k}:{v["dark"]};' for k,v in T['vertical'].items())+'}')
for k in T['vertical']: css.append(f'[data-vertical="{k}"]{{--accent-v:var(--v-{k});}}')
open('tokens/aula-tokens.css','w').write('\n'.join(css)+'\n')
# contrast table
bg=T['neutral']['bg'];W='#FFFFFF';nv=T['dark']['bg'];ns=T['dark']['surface']
rows=[]
def add(n,f,b,use):
  r=cr(f,b);rows.append(dict(name=n,fg=f,bg=b,ratio=r,AA=r>=4.5,AA_large=r>=3,use=use))
B=T['brand'];N=T['neutral'];S=T['semantic'];D=T['dark']
add('coral sobre bg',B['coral'],bg,'solo relleno/grande');add('blanco sobre coral',W,B['coral'],'botón ≥18px bold');add('coral-700 sobre bg',B['coral-700'],bg,'texto coral');add('blanco sobre coral-700',W,B['coral-700'],'botón texto normal')
add('blue sobre bg',B['blue'],bg,'enlaces');add('blanco sobre blue',W,B['blue'],'botón');add('blue-700 sobre bg',B['blue-700'],bg,'texto pequeño')
add('ink sobre bg',N['ink'],bg,'texto');add('muted sobre bg',N['muted'],bg,'secundario');add('subtle sobre bg',N['subtle'],bg,'captions')
for k in ['success','error','warning','ai']: add(f'{k} sobre bg',S[k],bg,'texto/icono')
add('ai sobre ai-100',S['ai'],S['ai-100'],'badge IA');add('gold-700 sobre gold-100',B['gold-700'],B['gold-100'],'chip XP');add('navy sobre gold',nv,B['gold'],'chip XP/racha oscuro')
for k in ['ink','muted','gold','coral','blue','success','error','ai']: add(f'dark {k} sobre navy-900',D[k],nv,'modo navy');add(f'dark {k} sobre navy-800',D[k],ns,'tarjeta navy')
add('gold sobre navy-700',B['gold'],B['navy-700'],'hero/footer')
for k,v in T['vertical'].items(): add(f'{k} light sobre bg',v['light'],bg,'texto/línea');add(f'blanco sobre {k}',W,v['light'],'badge');add(f'{k} dark sobre navy',v['dark'],nv,'modo navy')
comp=dict(final=B['coral'],ref='#EF7746',hue_final=hue(B['coral']),hue_ref=hue('#EF7746'),hue_diff=round((hue('#EF7746')-hue(B['coral']))%360,1),dE2000=de2000(B['coral'],'#EF7746'),dE2000_old_FF6B3D=de2000('#FF6B3D','#EF7746'),dE_text=de2000(B['coral-700'],'#EF7746'))
json.dump(dict(contrast=rows,coral_vs_reference=comp),open('tokens/contrast.json','w'),ensure_ascii=False,indent=1)
print(comp);print([ (r['name'],r['ratio']) for r in rows if not r['AA']])
json.dump(T,open('tokens/_t.json','w'))
