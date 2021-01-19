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
    print(lx,ly,ff(lx,ly),fix1(lx,ly),fix2(lx,ly))
    return int(ff(lx,ly) + fix1(lx,ly) + fix2(lx,ly))

T   = int(input())
for _ in range(T):
    x,y = map(int,input().split())
    print(f(x,y) if x>y else f(y,x))
