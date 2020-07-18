#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/445/B

class DisjointSet:      #only support query, NO construction supported
    def __init__(self, n):
        self.num_sets   = n         #--@union
        self.parents    = list(range(n))
        self.ranks      = [0] * n
        self.sizes      = [1] * n   #used@union: size of set@root! 0 if NOT repsentive

    def find(self,j): #no compress
        while self.parents[j]!=j:
            j   = self.parents[j]
        return j

    def union(self,i,j):
        i   = self.find(i)
        j   = self.find(j)
        if i == j:
            return False
        rd  = self.ranks[i] - self.ranks[j]
        if   rd == 0:       # Increment repr0's rank if both nodes have same rank
            self.ranks[i] += 1
        elif rd <  0:       # Swap to ensure that repr0's rank >= repr1's rank
            i, j = j, i
        self.parents[j]  = i   #merge
        self.sizes[i]   += self.sizes[j]
        self.sizes[j]    = 0
        self.num_sets   -= 1
        return True

def main():
    n,m =  list(map(int,input().split())) #100,100
    cl  = [list(map(int,input().split())) for _ in range(m)]
    ds  = DisjointSet(n)
    for a,b in cl:
        ds.union(a-1,b-1)
    print(2**(sum([max(0,s-1) for s in ds.sizes])))

main()
