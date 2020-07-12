#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/1033/A
#王:3x3-1内移动; 后:对角/行/列
#用BFS来做!? 用Q太慢? 自己手动实现?? 或者用DFS?
'''
    for ii in range(n*n):   #比qcl慢多了..
        if (ii//n)==qq[0] or (ii%n)==qq[1] or (ii//n)+(ii%n)==qq[0]+qq[1]:
'''

def q4bfs(gd,kr,kc,tr,tc,qr,qc,n):
    tnrl    = range(tr-1,tr+2)
    tncl    = range(tc-1,tc+2)
    from queue import Queue as Q
    q       = Q()
    q.put([kr,kc])
    gd[kr*n+kc] = -1
    while not q.empty():
        rr,cc = q.get()
        if (rr in tnrl) and (cc in tncl):
            return True
        cl = [(r,c) for r in range(rr-1,rr+2) for c in range(cc-1,cc+2) if (r>=0 and c>=0 and r<n and c<n and gd[r*n+c]>0)]
        for r,c in cl:
            q.put([r,c])
            gd[r*n+c]=False     #avoid revisit
    return False

def main():
    #cm = lambda qr,qc,r,c:(qr==r or qc=c or qr+qc=r+c)
    n       = int(input())  #1000
    n2      = n*n
    qr,qc   = [int(s)-1 for s in input().split()]
    kr,kc   = [int(s)-1 for s in input().split()] 
    tr,tc   = [int(s)-1 for s in input().split()] 
    gd      = [1]*n2
    qrc     = qr+qc
    qcl     = list(range(qr*n,(qr+1)*n)) + list(range(qc,n2,n)) + [(r*n+qrc-r) for r in range(n) if qrc>=0 and qrc<n]
    for ii in qcl:
        gd[ii] = 0
    print('YES' if q4bfs(gd,kr,kc,tr,tc,qr,qc,n) else 'NO')

#main()
import cProfile
cProfile.run("main()")
