set -e
python3 gen1.py >/dev/null; python3 gen2.py; python3 gen3.py; python3 gen4.py >/dev/null
python3 -c "
from shot import shots;shots([(f'screens/{k}.html',f'screens/{k}.png',390,844,2,False) for k in ['home','home-dark','question','explanation','result','simulacro']])"
python3 gen5.py >/dev/null
python3 -c "
from shot import shots
J=[('web/site-desktop.html','web/site-desktop-1280.png',1280,800,1,True),('web/site-mobile.html','web/site-mobile-390.png',390,844,2,True),
('templates/instagram-post.html','templates/instagram-post-1080.png',1080,1080,1,False),('templates/instagram-story.html','templates/instagram-story-1080x1920.png',1080,1920,1,False),('templates/og-image.html','templates/og-image-1200x630.png',1200,630,1,False),
('ui/ui-kit.html','ui/ui-kit.png',1280,900,1,True),('ui/ui-kit-dark.html','ui/ui-kit-dark.png',1280,900,1,True),('ui/coral-vs-reference.html','ui/coral-vs-reference.png',1080,520,2,True),('templates/email-signature-preview.html','templates/email-signature.png',520,140,2,True),('ui/logo-sheet.html','ui/logo-sheet.png',1280,800,1,True)]
J+=[(f'templates/appstore-6.7-{i}.html',f'templates/appstore-6.7-{i}-1290x2796.png',430,932,3,False) for i in range(1,5)]
shots(J)"
python3 gen6.py
python3 -c "
from shot import shots;shots([('board.html','png/board-summary.png',1880,1000,1,True)])"
echo BUILD-OK
