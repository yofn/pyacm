#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/115/A
#公司聚会, 每一组里不能有上下级关系

n   = int(input())
el  = [[] for i in range(n+1)]    #*n NOT work!
for i in range(n):
    s = int(input())
    s = max(s,0)
    el[s].append(i+1)   # s=(i+1)'s supervisor
# DFS by stack
vs  = [0]*(n+1)
vl  = [0]*(n+1) #layer of vertices
sp  = 0
while sp>-1:
    p   = vs[sp]
    sp -= 1 #POP to p
    for v in el[p]: # push all children
        sp    += 1
        vs[sp] = v
        vl[v]  = vl[p]+1
print(max(vl))
