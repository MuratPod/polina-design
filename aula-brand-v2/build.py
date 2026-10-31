import json,pathlib
H=pathlib.Path(__file__).parent
def L(h):
    c=[int(h[i:i+2],16)/255 for i in (1,3,5)];c=[x/12.92 if x<=.03928 else ((x+.055)/1.055)**2.4 for x in c];return .2126*c[0]+.7152*c[1]+.0722*c[2]
def cr(a,b):
    x,y=sorted([L(a),L(b)],reverse=True);return round((x+.05)/(y+.05),2)
D={
'a':dict(name='Noche de estudio',display='Fraunces',dfile='fraunces',ui='Public Sans',ufile='public-sans',
 navy=['#0A1730','#132A4F','#1E3D6B'],gold='#E2BE72',goldDeep='#8A6420',surface='#FBF7EE',surface2='#F2EADB',line='#E2D7C2',ink='#16213A',muted='#4E5868',
 success='#2E6B4A',error='#A63A2C',ai='#5A4AA8',aiBg='#ECE8F8',museos='#E0906A',museosDeep='#A5583A',justicia='#D98A97',justiciaDeep='#8E3445',angle='160deg'),
'b':dict(name='Constelación',display='Outfit',dfile='outfit',ui='IBM Plex Sans',ufile='ibm-plex-sans',
 navy=['#080F2A','#141E52','#2A2E7C'],gold='#F2C94C',goldDeep='#8C6A00',surface='#F4F5FA',surface2='#E8EAF4',line='#D6DAEA',ink='#0F1633',muted='#4A5070',
 success='#1E6E57',error='#B4322A',ai='#5B3FD1',aiBg='#ECE7FF',museos='#E07B53',museosDeep='#A94E2C',justicia='#6FA8DC',justiciaDeep='#2F6AA3',angle='145deg'),
}
rep={}
for k,p in D.items():
    c={}
    for s in p['navy']: c[f'gold {p["gold"]} on navy {s}']=cr(p['gold'],s)
    c[f'goldDeep {p["goldDeep"]} on surface {p["surface"]}']=cr(p['goldDeep'],p['surface'])
    for t in ['ink','muted','success','error','ai']: c[f'{t} {p[t]} on surface']=cr(p[t],p['surface'])
    c[f'ai on aiBg']=cr(p['ai'],p['aiBg'])
    for v in ['museos','justicia']:
        for s in (p['navy'][0],p['navy'][2]): c[f'{v} {p[v]} on navy {s}']=cr(p[v],s)
        c[f'white on {v}Deep {p[v+"Deep"]}']=cr('#FFFFFF',p[v+'Deep']); c[f'{v}Deep on surface']=cr(p[v+'Deep'],p['surface'])
    c[f'navy0 text on gold (CTA)']=cr(p['navy'][0],p['gold'])
    rep[k]=c
    (H/f'direction-{k}'/'palette.json').write_text(json.dumps({**p,'contrast':c},ensure_ascii=False,indent=2))
print(json.dumps(rep,indent=1,ensure_ascii=False))
