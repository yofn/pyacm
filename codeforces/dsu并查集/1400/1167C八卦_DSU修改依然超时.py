#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1167/C
# PyPy超时@4, Py超时@6
# 不用dsu, 用tree会不会快点?
# union的时候用tree来union会不会快点??
# NOTE: 修改了DisjointSet的实现, find的时候compress的厉害些! (结果4都过不了..原来能到6)

class DisjointSet:      #only support query, NO construction supported
    def __init__(self, n):
        self.num_sets   = n         #--@union
        self.parents    = list(range(n))
        self.ranks      = [0] * n
        self.sizes      = [1] * n   #used@union: size of set@root! 0 if NOT repsentive
 
    def find(self,j):
        jl  = [j]   #compress hard! NOTE
        while self.parents[j]!=j:
            j   = self.parents[j] 
            jl.append(j)
        for i in jl[:-1]:
            self.parents[i]  = j
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
 
n,m = list(map(int,input().split())) #5e5, 5e5
dsu = DisjointSet(n)
for _ in range(m):
    g = list(map(int,input().split()))
    for i in range(2,g[0]+1):
        dsu.union(g[i]-1,g[i-1]-1)
print(*[dsu.sizes[dsu.find(i)] for i in range(n)])
