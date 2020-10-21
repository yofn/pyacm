#!/usr/bin/env python3

#https://codeforces.com/group/H9K9zY8tcT/contest/297617
#https://oi-wiki.org/graph/shortest-path/#dijkstra
#from queue import PriorityQueue
#overkill? 因为这里的边都没有权重
#注意: 是无向边,所以应该用矩阵更好? (tc3!)
#借助BNUOJ调试才解决的!

def f(n,l):
    g   = [[] for i in range(n)]
    [g[f-1].append(t-1) for f,t in l]
    [g[t-1].append(f-1) for f,t in l]
    dl  = [0] + [None]*(n-1)
    ps  = set([0])
    d   = 1
    while True:
        s  = set()
        for i in ps:
            for j in g[i]:
                if dl[j] is None:
                    if j == n-1:
                        return d-1
                    dl[j] = d
                    s.add(j)
        d += 1
        ps = s
        if len(ps)==0:  #cope with no path (test case #3)
            return 0

n,m =  list(map(int,input().split()))   #both 1e5
l   = [list(map(int,input().split())) for _ in range(m)]
print(f(n,l))
