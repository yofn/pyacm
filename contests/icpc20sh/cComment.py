#!/usr/bin/python3
'''
定义:
+ free block of length i, starting from 0 to (i-1)
+ its corresponding suffix is reprented by lx[i:] (with 1 subtracted)
分析:
+ bits string set can be seperated into several disjoint sets (DS)
+ the number of disjoint sets = number of 1 in bitstring (x+1)
+ one special DS is the one with no prefix and only (and maximum) free block
+ if we thus think x and y combination as UION of cartesian product of DSs (which is easy to calculate)
坑点
+ freeblock can be longer than fixed block, thus freeblock weight is flexible!
+ total free block can vary its rank, or split into various sets!
继续分析:
+ each suffix defines a probability < 1, thus limits the feasible set
+ to be specific, suffix limits itself and limits opponent's free bits!
+ define bits/blocks as FREE or FIXED.
+ maybe we can pad ZEROs to a suffix or NO-suffix?
+ this way, everyone as a SUFFIX-BLOCK and FREE-BLOCK! aka. STRINGSET = SUFFIX-BLOCK + FREE-BLOCK!
+ however, the trick part is that if SUFFIX is all ZERO, FREE-BLOCK has a flexible RANK!
+ thus, we need to differentiate ZERO-SUFFIX and NONZERO-SUFFIX!
+ SINCE #bits is 30, no big deal to split ZERO-SUFFIXED STRINGSET into 30 Nonzero-SUFFIXED STRINGSET!
def ff(lx,ly):  #xl>=yl
    return fb(len(lx)-1) + fb(len(ly)-1)
    f00   = lambda b,s: 0 if b==s else (2**(b-s))*(3**s)
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

def buildSetList(l):
    n,sl,f1 = len(l),[],True
    for i in range(n):
        if l[i]==1:
            sl += [(nz,1,max(0,n-nz-1) for nz in range(i+1,n+1)] if f1 else [(i,0,n-i-1)]
            f1  = False              #(nz,1,nx)0+1+nx(free); (ns,0,nx)  l[:ns]+0+nx(free)
    return sl

def buildConflictList(lx,ly):
    l = [False]*len(lx)
    for i in range(len(lx)):
        l[i] = (lx[i]==1 and ly[i]==1) or (False if i==0 else l[i-1])
    return l

def buildZerocountList(l):
    zc = [0]*len(l)
    for i in range(len(l)):
        zc[i] = (0 if i==0 else zc[i-1]) + (l[i]==0)
    return zc

def f(x,y): #x>=y
    lx,ly = buildList(x,y)
    sx,sy = buildSetList(lx),buildSetList(ly)
    lcfl  = buildConflictList(lx,ly)
    zx,zy = buildZerocountList(lx),buildZerocountList(ly)
    c     = []
    for t1 in sx:                                       #(nz,1,nx)  nz*0  +1+nx(free)
        for t2 in sy:                                   #(ns,0,nx)  l[:ns]+0+nx(free)
            bht,sht = t1,t2 if t1[0]>t2[0] else t2,t1   #bh=bigger head, sh=smaller head
            if   bht[1]==1 and sht[1]==1:
                if bht[0]==sht[0]: continue
            elif bht[1]==1 and sht[1]==0:
                pass
            elif bht[1]==0 and sht[1]==1:
            
            bfb,sfb = max(fb1,fb2),min(fb1,fb2)
            if t1+t2==0:
                p2  = 2**(bfb-sfb)
            else:
                if (t1+t2==2 and lcfl[n-1-bfb]):
                    continue
                if t1==0 and fb1>fb2 and ly[n-1-fb1]==1:
            ccb     = n-1-bfb
            if t1+t2==1: p2 = 2**
            if t1+t2==2: pass
            p3      = 3**sfb
            c      += p3*p2*max(w1,w2)
    return sx,sy

T   = int(input())
for _ in range(T):
    x,y = map(int,input().split())
    x  += 1
    y  += 1
    print(f(x,y) if x>y else f(y,x))
