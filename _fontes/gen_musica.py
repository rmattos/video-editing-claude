import numpy as np, wave, sys
SR=44100
def note(n): return 440.0*2**((n-69)/12)
def env(t,a,d,rel=None):
    e=np.minimum(t/a,1.0)*np.exp(-t/d); return e
def sine(f,t): return np.sin(2*np.pi*f*t)
def tri(f,t): return 2/np.pi*np.arcsin(np.sin(2*np.pi*f*t))
def add(buf,start,sig,gain=1.0):
    i=int(start*SR); 
    if i>=len(buf): return
    j=min(len(buf),i+len(sig)); buf[i:j]+=gain*sig[:j-i]
def kick(dur=0.3):
    t=np.arange(int(dur*SR))/SR; f=45+90*np.exp(-t*28); ph=2*np.pi*np.cumsum(f)/SR
    return np.sin(ph)*np.exp(-t*11)
def hat(dur=0.06,seed=0):
    r=np.random.RandomState(seed); t=np.arange(int(dur*SR))/SR; n=r.randn(len(t)); n=np.diff(n,prepend=0); return n*np.exp(-t*70)*0.5
def snare(dur=0.18,seed=1):
    r=np.random.RandomState(seed); t=np.arange(int(dur*SR))/SR; n=r.randn(len(t)); return (n*0.6+sine(190,t)*0.4)*np.exp(-t*24)
def chord(freqs,dur,gain=1.0,wave_fn=tri,a=0.03,d=1.6,detune=0.0):
    t=np.arange(int(dur*SR))/SR; s=np.zeros_like(t)
    for f in freqs:
        s+=wave_fn(f,t)+ (wave_fn(f*(1+detune),t) if detune else 0)
    s/=max(1,len(freqs)); e=np.minimum(t/a,1)*np.exp(-t/d)*np.minimum((dur-t)/0.08,1)
    return s*e*gain
def pluck(f,dur=0.35):
    t=np.arange(int(dur*SR))/SR; return (sine(f,t)+0.4*sine(2*f,t)+0.2*sine(3*f,t))*np.exp(-t*9)*np.minimum(t/0.004,1)
def finish(buf,name,fade_in=0.3,fade_out=1.2,peak=0.7):
    n=len(buf); t=np.arange(n)/SR
    buf=buf*np.minimum(t/fade_in,1)*np.minimum((n/SR-t)/fade_out,1)
    buf=np.tanh(buf*1.2)
    buf=buf/np.max(np.abs(buf))*peak
    st=np.stack([buf,buf],axis=1)
    # leve largura estéreo
    d=int(0.012*SR); st[d:,1]=0.85*st[d:,1]+0.15*buf[:-d]
    pcm=(np.clip(st,-1,1)*32767).astype('<i2')
    with wave.open(name,'wb') as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes(pcm.tobytes())
    print(name, round(n/SR,2),'s')

def track_app(name):  # 112 bpm, 13 compassos, C-G-Am-F
    bpm=112; beat=60/bpm; bars=13; dur=bars*4*beat; buf=np.zeros(int(dur*SR)+SR)
    prog=[(48,[60,64,67]),(43,[59,62,67]),(45,[60,64,69]),(41,[60,65,69])]
    K=kick(); 
    for b in range(bars):
        r,ch=prog[b%4]; t0=b*4*beat
        add(buf,t0,chord([note(x) for x in ch],4*beat,0.35,tri,d=2.2))
        for q in range(8):  # baixo em colcheias
            add(buf,t0+q*beat/2,sine(note(r),np.arange(int(beat*0.45*SR))/SR)*np.exp(-np.arange(int(beat*0.45*SR))/SR*5)*0.55)
        for q in range(4): add(buf,t0+q*beat,K,0.9)
        for q in range(8): add(buf,t0+q*beat/2+beat/4*0,hat(seed=q+b),0.35 if q%2 else 0.2)
        add(buf,t0+beat,snare(),0.35); add(buf,t0+3*beat,snare(seed=5),0.35)
        arp=[ch[0]+12,ch[1]+12,ch[2]+12,ch[1]+12]
        if b>=2:
            for q in range(8): add(buf,t0+q*beat/2,pluck(note(arp[q%4])),0.32)
    finish(buf[:int(dur*SR)],name,0.4,1.5)

def track_cafe(name):  # 92 bpm lo-fi com swing, Fmaj7-Em7-Dm7-Cmaj7
    bpm=92; beat=60/bpm; bars=6; dur=bars*4*beat; buf=np.zeros(int(dur*SR)+SR)
    prog=[(41,[57,60,64,69]),(40,[55,59,62,67]),(38,[57,60,64,65]),(36,[55,59,64,67])]
    K=kick(0.35); r=np.random.RandomState(3)
    for b in range(bars):
        rt,ch=prog[b%4]; t0=b*4*beat
        add(buf,t0,chord([note(x) for x in ch],4*beat,0.5,tri,a=0.05,d=2.6,detune=0.004))
        add(buf,t0,sine(note(rt),np.arange(int(2*beat*SR))/SR)*np.exp(-np.arange(int(2*beat*SR))/SR*2.2)*0.6)
        add(buf,t0+2*beat,sine(note(rt+7),np.arange(int(2*beat*SR))/SR)*np.exp(-np.arange(int(2*beat*SR))/SR*2.2)*0.45)
        add(buf,t0,K,0.75); add(buf,t0+2.5*beat,K,0.6)
        add(buf,t0+beat,snare(seed=b),0.3); add(buf,t0+3*beat,snare(seed=b+9),0.3)
        for q in range(8):
            sw=beat/2*(1.18 if q%2 else 1.0)*0+q*beat/2+(beat/12 if q%2 else 0)
            add(buf,t0+sw,hat(seed=q),0.22)
    # chiado de vinil
    n=int(dur*SR); crack=np.zeros(len(buf))
    for _ in range(int(dur*9)):
        p=r.randint(0,n-400); crack[p:p+300]+=r.randn(300)*np.exp(-np.arange(300)/40)*0.05
    buf+=crack+r.randn(len(buf))*0.004
    finish(buf[:int(dur*SR)],name,0.5,1.8)

def track_historia(name):  # 72 bpm suave, Am-F-C-G, 24 compassos ~ 80 s
    bpm=72; beat=60/bpm; bars=24; dur=bars*4*beat; buf=np.zeros(int(dur*SR)+SR)
    prog=[(45,[57,60,64]),(41,[57,60,65]),(48,[55,60,64]),(43,[55,59,62])]
    for b in range(bars):
        rt,ch=prog[b%4]; t0=b*4*beat
        add(buf,t0,chord([note(x) for x in ch],4*beat+0.5,0.5,tri,a=0.6,d=6.0,detune=0.003))
        add(buf,t0,sine(note(rt),np.arange(int(4*beat*SR))/SR)*np.exp(-np.arange(int(4*beat*SR))/SR*0.9)*0.5)
        if b>=2:
            pat=[0,1,2,1,2,1,2,1] if b%2 else [0,2,1,2,0,2,1,2]
            for q in range(8): add(buf,t0+q*beat/2,pluck(note(ch[pat[q]]+12),0.6),0.22)
    finish(buf[:int(dur*SR)],name,1.5,4.0)

def track_motion(name):  # 120 bpm, 8 s, batida seca + hits nas entradas
    bpm=120; beat=60/bpm; bars=4; dur=bars*4*beat; buf=np.zeros(int(dur*SR)+SR); K=kick(0.28)
    r=np.random.RandomState(7)
    for b in range(bars):
        t0=b*4*beat
        for q in range(4): add(buf,t0+q*beat,K,0.8)
        for q in range(8): add(buf,t0+q*beat/2+beat/4,hat(seed=q+b),0.25)
        add(buf,t0+beat,snare(),0.3); add(buf,t0+3*beat,snare(seed=3),0.3)
        add(buf,t0,sine(note(36+[0,0,5,7][b]),np.arange(int(4*beat*SR))/SR)*np.exp(-np.arange(int(4*beat*SR))/SR*1.2)*0.5)
        add(buf,t0,chord([note(x) for x in [60+[0,0,5,7][b],64+[0,0,5,7][b],67+[0,0,5,7][b]]],4*beat,0.3,tri,d=2.5))
    # riser no início
    t=np.arange(int(1.0*SR))/SR; ris=r.randn(len(t))*np.linspace(0,1,len(t))**2*0.25; add(buf,0,ris)
    finish(buf[:int(dur*SR)],name,0.05,0.8)

track_app('trilhas/trilha-app.wav'); track_cafe('trilhas/trilha-cafe.wav'); track_historia('trilhas/trilha-historia.wav'); track_motion('trilhas/trilha-motion.wav')
