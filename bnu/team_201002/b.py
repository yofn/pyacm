#!/usr/bin/env python3
#https://codeforces.com/group/H9K9zY8tcT/contest/297258/problem/B
#heap?

from queue import PriorityQueue

n = int(input())
g = {}
c = {str(i):0 for i in range(1,n+1)}    #children count
for i in range(1,n+1):
    k    = str(i)
    g[k] = input().split() # l[0]=weight; l[1]=no use; l[2:] parents;
    for p in g[k][2:]:
        c[p] += 1
q = PriorityQueue()
[q.put((int(g[k][0]),k)) for k in c if c[k]==0]
m = 0
i = n-1
while not q.empty():
    w,k = q.get()
    l   = i + w
    i  -= 1
    if l>m:
        m = l
    for p in g[k][2:]:
        c[p] -= 1
        if c[p]==0:
            q.put((int(g[p][0]),p))
print(m)

