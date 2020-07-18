#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/755/C
#每个tree=kV,(k-1)E, 给出#tree
#双头的并查集? 或取较小的作为一头? 总是用最小的作为代表??
#之前总是想用正经dsu,奈何没机会,这次试试
#真正发挥了DSU/dsu并查集的威力;
#之前的问题用并查集也许也很方便,但要多写一个类..这个例题中写dsu类的开销很值.

class DisjointSet:      #only support query, NO construction supported
    def __init__(self, n):
        self.num_sets   = n         #--@union
        self.parents    = list(range(n))
        self.ranks      = [0] * n
        self.sizes      = [1] * n   #used@union: size of set@root! 0 if NOT repsentive

    def find(self,j):
        while self.parents[j]!=j:
            jj              = self.parents[j]
            self.parents[j] = self.parents[jj]   #partial compression
            j               = jj
        return j

    def union(self,i,j):
        r0  = self.find(i)
        r1  = self.find(j)
        if r0 == r1:
            return False
        rd  = self.ranks[r0] - self.ranks[r1]
        if   rd == 0:       # Increment repr0's rank if both nodes have same rank
            self.ranks[r0] += 1
        elif rd <  0:       # Swap to ensure that repr0's rank >= repr1's rank
            r0, r1 = r1, r0
        self.parents[r1] = r0   #merge
        self.sizes[r0]  += self.sizes[r1]
        self.sizes[r1]   = 0
        self.num_sets   -= 1
        return True

n   = int(input())  #1e4
tl  = list(map(int,input().split()))
dsu = DisjointSet(n)
for i,t in enumerate(tl):
    dsu.union(i,t-1)
print(dsu.num_sets)

