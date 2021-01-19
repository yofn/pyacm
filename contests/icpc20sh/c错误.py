#!/usr/bin/python3
'''
在testcase之间复用?
'''

def buildList(x,y):
    lx,ly = [],[]
    while x>0:
        lx.append(x%2)
        ly.append(y%2)
        x >>= 1
        y >>= 1
    lx.reverse(), ly.reverse()
    return lx, ly

def f(x,y): #x>=y
    if x==0 and y==0: return 0
    lx,ly   = buildList(x,y)
    xt,yt   = lx[0],ly[0]
    hhp     = (yt<1) #head-head peace
    ybok    = not hhp
    bb,bh,hb,s  = (1,1,1,2) if ybok else (0,1,0,1)
    print(s,bb,bh,hb)
    for i in range(1,len(lx)):
        xi,yi   = lx[i],ly[i]
        ybok    = ybok or yi
        if ybok:
            bb  *= 3
            if yi:      bb  += (bh<<1)
            if xi:      bb  += (hb<<1)
            if not xi:  hb   = (hb<<1)
        if not yi:
            bh = (bh<<1)
        if hhp:
            if xi and yi:   bb += 1
            if xi:          bh += 1
            if yi:          hb += 1
            hhp = (xi+yi<2)
        s   += bb+bh+hb
        print(s,bb,bh,hb)
    return (s+(hhp*len(lx)))%(1000000007)

T   = int(input())  #t=1e5
for _ in range(T):  #60*60=3600
    x,y = map(int,input().split())
    print(f(x,y) if x>y else f(y,x))
