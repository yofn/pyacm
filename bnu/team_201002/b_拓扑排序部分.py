#!/usr/bin/env python3

#https://codeforces.com/group/H9K9zY8tcT/contest/297258/problem/B
#贪心+拓扑排序
#DAG adapted from https://www.codespeedy.com/topological-sorting-in-python/

from collections import defaultdict

class DAG:
    def __init__(self,keys):
        self.graph  = {k:[] for k in keys}

    def addEdge(self, frm, to):
        self.graph[frm].append(to)

    def _tsVisit(self, s, visited, sortlist):
        visited[s] = True
        for i in self.graph[s]:
            if not visited[i]:
                self._tsVisit(i, visited, sortlist)
        sortlist.insert(0, s)

    def topoSort(self):
        visited  = {i: False for i in self.graph}
        sortlist = []
        for v in self.graph:
            if not visited[v]:
                self._tsVisit(v, visited, sortlist)
        return sortlist

def f(ll):
    n  = len(ll)
    el = [l[0]  for l in ll]
    pl = [[i-1 for i in l[2:]] for l in ll]    # parent topics of topic-i
    g  = DAG(map(str,range(n)))
    for i in range(n):
        for p in pl[i]:
            g.addEdge('%s'%p,'%s'%i)
    print(g.graph)
    return g.topoSort()

t = int(input())
l = [list(map(int,input().split())) for _ in range(t)]
print(f(l))
