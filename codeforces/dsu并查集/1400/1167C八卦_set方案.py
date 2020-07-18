#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1167/C
# PyPy超时@4, Py超时@6
# 不用dsu, 用tree会不会快点?
# union的时候用tree来union会不会快点??
# NOTE: 修改了DisjointSet的实现, find的时候compress的厉害些! (结果4都过不了..原来能到6)
# 不用压缩,反而过了Case4; ..但还是没过Case6(5e5,5e5)
'''
'''

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

    def find2(self,j):
        jl  = [j]   #compress HARD
        while self.parents[j]!=j:
            j   = self.parents[j] 
            jl.append(j)
        for i in jl[:-1]:
            self.parents[i] = j
        return j
 
    def union(self,i,j):
        r0  = self.find(i)
        r1  = self.find(j)
        #print(i,j,r0,r1,self.parents)
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

    def _sizes(self):   #this is for final COPIED sizes; will distroy sizes (changes in place)
        for i,s in enumerate(self.sizes):
            if s>0:
                continue
            j   = i
            jl  = [j] 
            while self.parents[j]!=j:
                j = self.parents[j]
                jl.append(j)
            s   = self.sizes[j]
            for j in jl[:-1]:
                self.sizes[j] = s
        return self.sizes
 
def main():
    n,m = list(map(int,input().split())) #5e5, 5e5
    dsu = DisjointSet(n)
    for _ in range(m):
        g  = list(map(int,input().split()))
        if g[0]==0:
            continue
        #rl  = list(set([dsu.find(i-1) for i in g[1:]]))
        rl  = [0]*g[0]
        for i,j in enumerate(g[1:]):
            while dsu.parents[j]!=j:
                j   = dsu.parents[j]
            rl[i] = j
        rl  = list(set(rl))
        [dsu.union(rl[i],rl[i+1]) for i in range(len(rl)-1)]
        '''
        rs  = len(rl)   #groups to merge;
        rl  = g[1:]
        rs  = g[0]
        pi,ss = 1,2     #pair interval and step size
        while pi < rs:
            for i in range(0,rs-pi,ss):
                dsu.union(rl[i],rl[i+pi])
            pi = ss
            ss = ss<<1
        '''
    print(*dsu._sizes())    #final sizes

#main()

import cProfile
cProfile.run("main()")
