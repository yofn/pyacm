#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/505/B
# 一个颜色一个dsu?

class DisjointSet:      #only support query, NO construction supported
    def __init__(self, n):
        self.num_sets   = n         #--@union
        self.parents    = list(range(n))
        self.ranks      = [0] * n
        self.sizes      = [1] * n   #used@union: size of set@root! 0 if NOT repsentive
 
    def __str__(self):
        return '%s'%self.parents

    def __repr__(self):
        return '%s'%self.parents

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
    el  = [list(map(int,input().split())) for _ in range(m)]
    q   = int(input())
    vl  = [list(map(int,input().split())) for _ in range(q)] 

    dl  = [DisjointSet(n) for _ in range(m)]
    for a,b,c in el:
        dl[c-1].union(a-1,b-1)
    [print(sum([d.find(u-1)==d.find(v-1) for d in dl])) for u,v in vl]

main()

'''
import cProfile
cProfile.run("main()")
'''
