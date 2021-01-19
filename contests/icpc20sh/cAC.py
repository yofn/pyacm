
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
    hhp     = (yt==0) #head-head peace
    c       = [1,1,1] if yt==1 else [0,1,0]  #[bb,bh,hb]
    w       = [0,1,1] if yt==1 else [0,0,0]
    nc,nw   = [0]*3,[0]*3
    for i in range(1,len(lx)):
        xi,yi   = lx[i],ly[i]
        xt,yt   = xt*2+xi, yt*2+yi
        nx2b    = hhp and xi
        ny2b    = hhp and yi
        nxy2b   = hhp and xi and yi
        nc[1]   = c[1]*(2-yi) + nx2b
        nw[1]   = w[1]*(2-yi) + nx2b*i + nc[1] - (yt==0)
        if yt>0:    # they need existence of Y-body
            nc[0]   = c[0]*3 + (xi*c[2]+yi*c[1])*2 + nxy2b #bb = bb + bh + hb + hh
            nw[0]   = w[0]*3 + (xi*w[2]+yi*w[1])*2 + nxy2b*i + nc[0] -1  #don't 00
            nc[2]   = c[2]*(2-xi) + ny2b
            nw[2]   = w[2]*(2-xi) + ny2b*i + nc[2]
        hhp     = hhp and (xi+yi<2)
        tc,tw   =  c, w
        c,w     = nc,nw
        nc,nw   = tc,tw
    return (sum(w)+(hhp*len(lx)))%(10**9+7)
 
T   = int(input())  #t=1e5
for _ in range(T):  #60*60=3600
    x,y = map(int,input().split())
    print(f(x,y) if x>y else f(y,x))
