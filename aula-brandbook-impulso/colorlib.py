import math,colorsys
def rgb(h): return [int(h[i:i+2],16)/255 for i in (1,3,5)]
def lum(h):
    c=[x/12.92 if x<=.04045 else ((x+.055)/1.055)**2.4 for x in rgb(h)];return .2126*c[0]+.7152*c[1]+.0722*c[2]
def cr(a,b):
    x,y=sorted([lum(a),lum(b)],reverse=True);return round((x+.05)/(y+.05),2)
def hue(h):
    return round(colorsys.rgb_to_hsv(*rgb(h))[0]*360,1)
def lab(h):
    c=[x/12.92 if x<=.04045 else ((x+.055)/1.055)**2.4 for x in rgb(h)]
    X=(c[0]*.4124+c[1]*.3576+c[2]*.1805)/.95047;Y=c[0]*.2126+c[1]*.7152+c[2]*.0722;Z=(c[0]*.0193+c[1]*.1192+c[2]*.9505)/1.08883
    f=lambda t:t**(1/3) if t>.008856 else 7.787*t+16/116
    return 116*f(Y)-16,500*(f(X)-f(Y)),200*(f(Y)-f(Z))
def de2000(a,b):
    L1,a1,b1=lab(a);L2,a2,b2=lab(b)
    C1=math.hypot(a1,b1);C2=math.hypot(a2,b2);Cb=(C1+C2)/2
    G=.5*(1-math.sqrt(Cb**7/(Cb**7+25**7)));a1p=(1+G)*a1;a2p=(1+G)*a2
    C1p=math.hypot(a1p,b1);C2p=math.hypot(a2p,b2)
    h1=math.degrees(math.atan2(b1,a1p))%360;h2=math.degrees(math.atan2(b2,a2p))%360
    dL=L2-L1;dC=C2p-C1p;dh=h2-h1
    if abs(dh)>180: dh-=360*math.copysign(1,dh)
    dH=2*math.sqrt(C1p*C2p)*math.sin(math.radians(dh/2))
    Lb=(L1+L2)/2;Cbp=(C1p+C2p)/2;hb=(h1+h2)/2 if abs(h1-h2)<=180 else (h1+h2+360)/2
    T=1-.17*math.cos(math.radians(hb-30))+.24*math.cos(math.radians(2*hb))+.32*math.cos(math.radians(3*hb+6))-.2*math.cos(math.radians(4*hb-63))
    Sl=1+.015*(Lb-50)**2/math.sqrt(20+(Lb-50)**2);Sc=1+.045*Cbp;Sh=1+.015*Cbp*T
    Rt=-2*math.sqrt(Cbp**7/(Cbp**7+25**7))*math.sin(math.radians(60*math.exp(-((hb-275)/25)**2)))
    return round(math.sqrt((dL/Sl)**2+(dC/Sc)**2+(dH/Sh)**2+Rt*(dC/Sc)*(dH/Sh)),1)
