#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/1033/A
#王:3x3-1内移动; 后:对角/行/列
#用BFS来做!?

from queue import Queue as Q
n   = int(input())  #1000
qq  = [int(s)-1 for s in input().split()]
kk  = [int(s)-1 for s in input().split()] 
tt  = [int(s)-1 for s in input().split()]
gd  = [True]*(n*n)
ir  = lambda f,t:max(abs(f[0]-t[0]),abs(f[1]-t[1]))<=1
for i in range(n*n):
    r,c = i//n,i%n
    if r==qq[0] or c==qq[1] or r+c==qq[0]+qq[1]:
        gd[i] = False
# Q for BFS/bfs
q   = Q()
q.put(kk)
ok  = False
while not q.empty():
    r,c = q.get()
    gd[r*n+c] = False   #avoid revisit
    if ir((r,c),tt):
        ok  = True
        break
    uu,dd   = max(0,r-1),min(n-1,r+1)
    ll,rr   = max(0,c-1),min(n-1,c+1)
    [q.put([r,c]) for r in range(uu,dd+1) for c in range(ll,rr+1) if gd[r*n+c]]
print('YES' if ok else 'NO')

