import json,pathlib
from shot import shots
from PIL import Image,ImageDraw
L=json.load(open('logo/_list.json'))+['aula-clearspace']
jobs=[]
for n in L:
  pathlib.Path(f'logo/png/_{n}.html').write_text(f'<body style="margin:0"><img src="../{n}.svg" style="display:block">');jobs.append((f'logo/png/_{n}.html',f'logo/png/{n}.png',1,1,3,True))
pathlib.Path('app-icon/_m.html').write_text('<body style="margin:0"><img src="aula-app-icon.svg" width=1024 height=1024 style="display:block">')
jobs.append(('app-icon/_m.html','app-icon/master-1024.png',1024,1024,1,False))
for n in ['foreground','background','monochrome']:
  pathlib.Path(f'app-icon/_{n}.html').write_text(f'<body style="margin:0"><img src="android-adaptive-{n}.svg" width=432 height=432 style="display:block">');jobs.append((f'app-icon/_{n}.html',f'app-icon/android-adaptive-{n}-432.png',432,432,1,False))
pathlib.Path('app-icon/_prev.html').write_text('<body style="margin:0;background:#E6E1D6;display:flex;gap:24px;padding:24px">'+''.join(f'<div style="width:160px;height:160px;{m};overflow:hidden;position:relative"><img src="android-adaptive-background.svg" style="position:absolute;inset:-25%;width:150%"><img src="android-adaptive-foreground.svg" style="position:absolute;inset:-25%;width:150%"></div>' for m in ['border-radius:50%','border-radius:36px','border-radius:50% 50% 50% 12px'])+'<div style="width:160px;height:160px;border-radius:50%;background:#DCE0EA;overflow:hidden;position:relative"><img src="android-adaptive-monochrome.svg" style="position:absolute;inset:-25%;width:150%;opacity:.8"></div></body>')
jobs.append(('app-icon/_prev.html','app-icon/android-adaptive-preview.png',800,210,2,False))
shots(jobs)
for f in list(pathlib.Path('logo/png').glob('_*.html'))+list(pathlib.Path('app-icon').glob('_*.html')): f.unlink()
m=Image.open('app-icon/master-1024.png').convert('RGB')
for s in [20,29,40,58,60,76,80,87,120,152,167,180,1024]: m.resize((s,s),Image.LANCZOS).save(f'app-icon/ios-{s}.png')
for k,s in {'mdpi':48,'hdpi':72,'xhdpi':96,'xxhdpi':144,'xxxhdpi':192,'play-store':512}.items(): m.resize((s,s),Image.LANCZOS).save(f'app-icon/android-{k}-{s}.png')
r=Image.new('L',(1024,1024),0);ImageDraw.Draw(r).rounded_rectangle([0,0,1023,1023],radius=225,fill=255);fm=m.copy();fm.putalpha(r)
for s in [16,32,48,64,96,128,180,192,256,512]: fm.resize((s,s),Image.LANCZOS).save(f'favicon/favicon-{s}.png')
m.resize((180,180),Image.LANCZOS).save('favicon/apple-touch-icon.png');fm.save('favicon/favicon.ico',sizes=[(16,16),(32,32),(48,48)])
pathlib.Path('favicon/site.webmanifest').write_text(json.dumps({"name":"Aula.","short_name":"Aula.","icons":[{"src":"favicon-192.png","sizes":"192x192","type":"image/png"},{"src":"favicon-512.png","sizes":"512x512","type":"image/png"}],"theme_color":"#142A3D","background_color":"#F4F1EA","display":"standalone"},indent=1))
pathlib.Path('favicon/head-snippet.html').write_text('<link rel="icon" href="/favicon.ico" sizes="any">\n<link rel="icon" href="/favicon.svg" type="image/svg+xml">\n<link rel="apple-touch-icon" href="/apple-touch-icon.png">\n<link rel="manifest" href="/site.webmanifest">\n<meta name="theme-color" content="#142A3D">\n')
print('ok')
