#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/1249/B1

class QuickFind(object):
    c2f   = []  #=multiple trees?
    count = 0   #count of trees(disjoint sets)

    def __init__(self,n):
        self.count = n
        self.c2f   = [i in range(n)]
            
    def connected(self,p,q):
        return self.find(p) == self.find(q)
    
    def find(self,p): #aka. root
        while p!=self.c2f[p]:
            p = self.c2f[p]
        return p
         
    def union(self,p,q):
        qroot = self.find(q)
        proot = self.find(p)
        if not self.connected(qroot,proot):
            self.c2f[proot]  = qroot
            self.count      -= 1

q = int(input())        #200
for _ in range(q):
    n  = int(input())   #200
    pl = list(map(int,input().split()))


