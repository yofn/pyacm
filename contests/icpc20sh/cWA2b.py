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
'''

def fix2(lx,ly):
    nx  = len(lx)
    ny  = len(ly)
    c   = 0
    zx = [1-lx[0]]*nx
    zy = [1-ly[0]]*ny
    for i in range(1,nx): zx[i] = zx[i-1]+(lx[i]==0)
    for i in range(1,ny): zy[i] = zy[i-1]+(ly[i]==0)
    fit = [True]*nx
    for i in range(ny-1,-1,-1):
        fit[i] = False if (lx[i]==1 and ly[i]==1) else fit[i+1]
    for i in range(nx-1):
        for j in range(ny-1):
            if lx[i]==0 or ly[j]==0 or fit[max(j,i)+1]==False:
                continue
            if j>i:
                c += (3**i)*(2**(zx[j-1]-zx[i]+1))
            else:
                c += (3**j)*(2**(zy[min(i-1,ny-2)]-zy[j]+1))
    return c*nx

def fix1(lx,ly):
    nx = len(lx)
    ny = len(ly)
    zx = [1-lx[0]]*nx
    zy = [1-ly[0]]*ny
    for i in range(1,nx): zx[i] = zx[i-1]+(lx[i]==0)
    for i in range(1,ny): zy[i] = zy[i-1]+(ly[i]==0)
    cx = sum([(3**i)*(2**(zx[ny-2]-zx[i]+1)) for i in range(nx-1) if lx[i]==1])
    cy = sum([(3**i)*(2**(zy[ny-2]-zy[i]+1)) for i in range(ny-1) if ly[i]==1])
    return nx*cx + ny*cy

def countOneSuffix(l):
    zs = [l[0]]
    for i in l[1:]:
        zs.append(zs[-1]+i)
    return zs

def fix(lx,ly):
    nx  = len(lx)
    ny  = len(ly)
    zx  = countOneSuffix(lx)
    zy  = countOneSuffix(ly)
    zy  = zy + [zy[-1]]*(nx-ny)
    wx  = []
    wy  = []
    cfl = [False]*nx        #used to check conflict of suffix 
    for i in range(ny-1,-1,-1):
        cfl[i] = (lx[i]==1 and ly[i]==1) or cfl[i+1]
    for i in range(nx):
        if lx[i]==0: continue
        fx,sx = i,(nx-i if i<nx-1 else 0)       #DS(i)=suffix(i~nx-1)+freeblock(0-i-1)
        for j in range(ny):
            if ly[j]==0: continue
            fy,sy = j,(ny-j if j<ny-1 else 0)   #DS(j)=suffix(j~ny-1)+freeblock(0-j-1)
            if sx+sy==0: continue   #double free blocks, already dealed in ff()
            cb = max(fx,fy)+1       #the bit to check confliction!
            if cb<nx and cfl[cb]: continue
            tb = min(fx,fy)         #bit positions of 3-free, form (0-min(fx,fy)-1)
            db = (fy-fx)-(zx[fy-1]-zx[fx]) if fx<fy else (min(fx,ny)-fy)-(zy[fx-1]-zy[fy])
            print(lx[i:],ly[j:])
            if sx>0:
                wx.append((3**tb)*(2**db))
            else:
                wy.append((3**tb)*(2**db))
    print(wx,wy)
    return nx*sum(wx) + ny*sum(wy)
    

def ff(lx,ly):  #xl>=yl
    fb = lambda n: ((2*n-1)*(3**n)+1)>>2
    return fb(len(lx)-1) + fb(len(ly)-1)

def f(x,y):     #x>=y
    x += 1
    y += 1
    lx = []
    ly = []
    while x>0:
        lx.append(x%2)
        x >>= 1
    while y>0:
        ly.append(y%2)
        y >>= 1
    print(lx,ly,ff(lx,ly))
    return ff(lx,ly) + fix(lx,ly)
    #print(lx,ly,ff(lx,ly),fix1(lx,ly),fix2(lx,ly))
    #return int(ff(lx,ly) + fix1(lx,ly) + fix2(lx,ly))

T   = int(input())
for _ in range(T):
    x,y = map(int,input().split())
    print(f(x,y) if x>y else f(y,x))
