import json,pathlib
from shot import shots
from PIL import Image
L=json.load(open('logo/_list.json'))+['aula-wordmark','aula-wordmark-dark','aula-clearspace']
jobs=[]
for n in L:
  pathlib.Path(f'logo/png/_{n}.html').write_text(f'<body style="margin:0"><img src="../{n}.svg" style="display:block">')
  jobs.append((f'logo/png/_{n}.html',f'logo/png/{n}.png',1,1,3,True))
pathlib.Path('app-icon/_m.html').write_text('<body style="margin:0"><img src="aula-app-icon.svg" width=1024 height=1024 style="display:block">')
jobs.append(('app-icon/_m.html','app-icon/master-1024.png',1024,1024,1,False))
shots(jobs)
for f in pathlib.Path('logo/png').glob('_*.html'): f.unlink()
pathlib.Path('app-icon/_m.html').unlink()
m=Image.open('app-icon/master-1024.png').convert('RGB')
ios=[20,29,40,58,60,76,80,87,120,152,167,180,1024];andr={'mdpi':48,'hdpi':72,'xhdpi':96,'xxhdpi':144,'xxxhdpi':192,'play-store':512}
for s in ios: m.resize((s,s),Image.LANCZOS).save(f'app-icon/ios-{s}.png')
for k,s in andr.items(): m.resize((s,s),Image.LANCZOS).save(f'app-icon/android-{k}-{s}.png')
# android adaptive foreground/background
pathlib.Path('app-icon/android-adaptive-background.svg').write_text('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 108 108"><rect width="108" height="108" fill="#FF4250"/></svg>')
# favicon: rounded png from favicon.svg via the master (rounded mask)
r=Image.new('L',(1024,1024),0)
from PIL import ImageDraw
ImageDraw.Draw(r).rounded_rectangle([0,0,1023,1023],radius=287,fill=255)
fm=m.copy();fm.putalpha(r)
for s in [16,32,48,64,96,128,180,192,256,512]: fm.resize((s,s),Image.LANCZOS).save(f'favicon/favicon-{s}.png')
m.resize((180,180),Image.LANCZOS).save('favicon/apple-touch-icon.png')
fm.save('favicon/favicon.ico',sizes=[(16,16),(32,32),(48,48)])
pathlib.Path('favicon/site.webmanifest').write_text(json.dumps({"name":"aula!","short_name":"aula!","icons":[{"src":"favicon-192.png","sizes":"192x192","type":"image/png"},{"src":"favicon-512.png","sizes":"512x512","type":"image/png"}],"theme_color":"#FF4250","background_color":"#FFF8EC","display":"standalone"},indent=1))
pathlib.Path('favicon/head-snippet.html').write_text('<link rel="icon" href="/favicon.ico" sizes="any">\n<link rel="icon" href="/favicon.svg" type="image/svg+xml">\n<link rel="apple-touch-icon" href="/apple-touch-icon.png">\n<link rel="manifest" href="/site.webmanifest">\n<meta name="theme-color" content="#FF4250">\n')
print('ok')
