#!/usr/bin/env python3
# 2020暑期排位5D_robotEasy
# https://codeforces.com/group/H9K9zY8tcT/contest/286081/problem/D
# https://www.youtube.com/watch?v=KiCBXu4P-2Y
# 这是一个(迭代式)BFS/bfs的例子
import queue

maxR,maxC   = 12,12
dr,dc,ds    = [1,-1,0,0],[0,0,1,-1],['U','D','L','R']  #NOTE: directed reversed!
rc          = lambda r,c: (r-1)*maxC+c-1

gd  = ['w']*(maxR*maxC)
rq  = queue.Queue()
cq  = queue.Queue()
for r,c in [(3,3),(3,10),(10,3),(10,10)]:
    gd[rc(r,c)]=''
    rq.put(r)
    cq.put(c)
for r,c in [(6,6),(6,7),(7,6),(7,7),(9,2),(9,3),(10,2),(9,10),(9,11),(10,11)]:
    gd[rc(r,c)]='b'
nW = maxR*maxC-14
while nW>0:
    r,c = rq.get(),cq.get()
    for i in range(4):
        rr = r+dr[i]
        cc = c+dc[i]
        if rr<1 or rr>maxR: continue
        if cc<1 or cc>maxC: continue
        ii = rc(rr,cc)
        if gd[ii] != 'w':   continue
        rq.put(rr)
        cq.put(cc)
        gd[ii] = ds[i] + gd[rc(r,c)]
        nW -= 1

n   = int(input())
for i in range(n):
    r,c = list(map(int,input().split()))
    s   = gd[rc(r,c)]
    print(len(s))
    print(s)

