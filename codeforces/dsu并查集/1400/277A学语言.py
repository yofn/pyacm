#!/usr/bin/env python3

# https://codeforces.com/contest/277/problem/A
# 误操作导致这个题的笔记都丢失了~~~

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
 
n,m = list(map(int,input().split()))
lll = [list(map(int,input().split())) for _ in range(n)]
dsu = DisjointSet(n)    #tricky, choose n or m?
rep = [None]*(m+1)      #one representive for each language
cnt = 0
hl  = False             #in case every one speak NONE(case 4)
for i,ll in enumerate(lll):
    for l in ll[1:]:
        hl  = True
        if rep[l] is None:
            rep[l] = i
        else:
            dsu.union(i,rep[l])
print(dsu.num_sets-1 if hl else dsu.num_sets)
