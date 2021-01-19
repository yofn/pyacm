#!/usr/bin/python3
'''
用这个公式就有问题! c2.err c2.err c2.err c2.err
fb    = lambda n: ((2*n-1)*(3**n)+1)>>2
s     = fb(wx-1) + fb(wy-1)
#if ctype==2: continue
虽然TLE,但是有优化的空间! 比如
+ 避免每个testCase重新分配内存
+ 避免多次power运算
但是为了学习数位DP,还是先放弃这条路!
'''

def buildList(x,y):
    lx,ly = [],[]
    while x>0:
        lx.append(x%2)
        ly.append(y%2)
        x >>= 1
        y >>= 1
    lx.reverse(), ly.reverse()
    return lx,ly

def buildSetList(l,t):  #t=tag
    n,sl,w = len(l),[],-1
    for i in range(n):
        if l[i]==1:
            sl += [(nz,1,max(0,n-nz-1),t,n-nz) for nz in range(i+1,n+1)] if w<0 else [(i,0,n-i-1,t,w)]
            w   = n-i if w<0 else w #(nz,1,nx)0+1+nx(free); (ns,0,nx)  l[:ns]+0+nx(free)
    return sl,w

def buildConflictList(lx,ly):
    l = [False]*len(lx)
    for i in range(len(lx)):
        l[i]  = (False if i==0 else l[i-1]) or (lx[i]==1 and ly[i]==1) 
    return l

def buildZerocountList(l):
    zc = [0]*len(l)
    for i in range(len(l)):
        zc[i] = (0 if i==0 else zc[i-1]) + (l[i]==0)
    return zc

def f(x,y): #x>=y
    lx,ly = buildList(x,y)
    sx,wx = buildSetList(lx,'x')
    sy,wy = buildSetList(ly,'y')
    lcfl  = buildConflictList(lx,ly)
    zx,zy = buildZerocountList(lx),buildZerocountList(ly)
    s     = 0
    m     = 10**9+7
    for tx in sx:                                       #(nz,1,nx,tag,w)  nz*0  +1+nx(free)
        for ty in sy:                                   #(ns,0,nx,tag,w)  l[:ns]+0+nx(free)
            ctype =    (tx[1]+ty[1])
            c3    = min(tx[2],ty[2])
            w     = max(tx[4],ty[4])
            if tx[0]==ty[0]:
                if ctype==1 or (ctype==0 and (not lcfl[tx[0]-1])):
                    s += w*(3**c3)
                continue
            yb          = tx[0]<ty[0]
            tb,ts,lb,zb = [tx,ty][yb], [ty,tx][yb], [lx,ly][yb], [zx,zy][yb]
            if tb[1]==0:
                if ts[1]==1 and   lb[ts[0]  ]==1: continue
                if ts[1]==0 and lcfl[ts[0]-1]==1: continue
            c2  = tb[0]-ts[0]-1 if tb[1]==1 else zb[tb[0]-1]-zb[ts[0]]+1
            s  += w*(3**c3)*(2**c2)
    return s%m

T   = int(input())  #t=1e5
for _ in range(T):  #60*60=3600
    x,y = map(int,input().split())
    x  += 1
    y  += 1
    print(f(x,y) if x>y else f(y,x))
