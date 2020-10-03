#!/usr/bin/env python3

#https://codeforces.com/group/H9K9zY8tcT/contest/297258/problem/B

from collections import defaultdict
from queue import PriorityQueue

class DAG:
    def __init__(self,nodeKeys):
        self.parents    = {k:[] for k in nodeKeys}
        self.weights    = {k:[] for k in nodeKeys}
        self.numChld    = {k:0  for k in nodeKeys} 
        self.leafs      = PriorityQueue()

    def addEdge(self, fm, to):
        self.parents[to].append(fm)
        self.numChld[fm] += 1

    def updNode(self,to,weight):
        self.weights[to]  = weight

    def initLeafs(self):
        [self.leafs.put((self.weights[k],k)) for k in self.numChld if self.numChld[k]==0]

    def topoSort(self):
        tslist = []
        while not self.leafs.empty():
            w,k = self.leafs.get()
            for p in self.parents[k]:
                self.numChld[p] -= 1
                if self.numChld[p] == 0:
                    self.leafs.put((self.weights[p],p))
            tslist.append([w,k])
        tslist.reverse()
        return tslist

def f(ll):
    n  = len(ll)
    el = [l[0]  for l in ll]
    pl = [[i-1 for i in l[2:]] for l in ll]    # parent topics of topic-i
    g  = DAG(list(map(str,range(n))))
    for i in range(n):
        g.updNode(str(i),el[i])
        for p in pl[i]:
            g.addEdge(str(p),str(i))
    g.initLeafs()
    ts = g.topoSort()
    return max([i+ts[i][0] for i in range(n)])

t = int(input())
l = [list(map(int,input().split())) for _ in range(t)]
print(f(l))
