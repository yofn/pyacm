#!/usr/bin/env python3

#https://codeforces.com/group/H9K9zY8tcT/contest/297258/problem/B

from collections import defaultdict
from queue import PriorityQueue

class DAG:
    def __init__(self,nodeKeys):
        self.childjn    = {k:[] for k in nodeKeys}
        self.parents    = {k:[] for k in nodeKeys}
        self.weights    = {k:[] for k in nodeKeys}
        self.numPrnt    = {k:0  for k in nodeKeys} 
        self.numChld    = {k:0  for k in nodeKeys} 

    def addEdge(self, fm, to):
        self.childjn[fm].append(to)
        self.parents[to].append(fm)
        self.numChld[fm] += 1
        self.numPrnt[to] += 1

    def updNode(self,to,weight):
        self.weights[to]  = weight

    def initLeafs(self):
        self.leafs = PriorityQueue()
        [self.leafs.put((self.weights[k],k)) for k in self.numChld if self.numChld[k]==0]

    def afterGet(self,leaf):
        for fm in self.parents[leaf]:
            self.numChld[fm] -= 1
            if self.numChld[fm] == 0:
                self.leafs.put((self.weights[fm],fm))

    def topoSort(self):
        tslist = []
        while not self.leafs.empty():
            node = self.leafs.get()
            self.afterGet(node[1])
            tslist.append(node)
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
