#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/1033/A
#王:3x3-1内移动; 后:对角/行/列
#用BFS来做!?

def q4bfs(gd,kk,tt):
    tr,tc   = tt
    tnrl    = range(tr-1,tr+2)
    tncl    = range(tc-1,tc+2)
    from queue import Queue as Q
    q       = Q()
    q.put(kk)
    gd[kk[0]*n+kk[1]] = -1
    while not q.empty():
        rr,cc = q.get()
        if (rr in tnrl) and (cc in tncl):
            return True
        cl = [(r,c) for r in range(rr-1,rr+2) for c in range(cc-1,cc+2) if (r>=0 and c>=0 and r<n and c<n and gd[r*n+c]>0)]
        for r,c in cl:
            q.put([r,c])
            gd[r*n+c]=False     #avoid revisit
    return False

n   = int(input())  #1000
qq  = [int(s)-1 for s in input().split()]
kk  = [int(s)-1 for s in input().split()] 
tt  = [int(s)-1 for s in input().split()]
gd  = [1]*(n*n)
for ii in range(n*n):
    if (ii//n)==qq[0] or (ii%n)==qq[1] or (ii//n)+(ii%n)==qq[0]+qq[1]:
        gd[ii] = 0
print('YES' if q4bfs(gd,kk,tt) else 'NO')

