#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/1055/B
#n,m,l
#a[n], 实际就是以>l的区域个数!
#考虑到n和m的大小,每次查询应该是要求<O(n)复杂度,所以必须上好的数据结构!
#真的需要实现一个正经的并查集了??
#https://en.wikipedia.org/wiki/Disjoint-set_data_structure
#https://www.nayuki.io/res/disjoint-set-data-structure/disjointset.py
#TODO 在上面链接上修改的.由多个列表组成,没有使用指针.适合py; 改动:减少行数!面向竞赛而非工程
#https://github.com/mrapacz/disjoint-set/blob/master/disjoint_set/main.py
#实现细节: <=l的不能合并;只有>l的才能合并..
#需要这么复杂吗? 计数和一个列表不能搞定?? TODO 试试标准DSU和定制版的

class DisjointSet:      #only support query, NO construction supported
    def __init__(self, numelems):
	self.num_sets   = numelems          #-- if merge
        self.num_cuts   = 0                 #NOTE: ADDED for this problem!
	self.parents    = list(range(numelems))
	self.ranks      = [0] * numelems
        self.sizes      = [1] * numelems    #size of set maintained by representives! 0 if NOT repsentive
	
    def find(self, j): #j=elemindex
        while self.parents[j]!=j:
            jj              = self.parents[j] 
            self.parents[j] = self.parents[jj]   #partial compression
            j               = jj
        return j
	
    def union(self, i, j):
        r0  = self.find(i)
	r1  = self.find(j)
        if r0 == r1:
	    return False
        rd  = self.ranks[r0] - self.ranks[r1]
        if rd == 0:     # Increment repr0's rank if both nodes have same rank
            self.ranks[r0] += 1
	elif rd < 0:    # Swap to ensure that repr0's rank >= repr1's rank
            r0, r1 = r1, r0
	self.parents[r1] = r0   #merge
	self.sizes[r0] += self.sizes[r1]
	self.sizes[r1] = 0
	self.num_sets -= 1
	return True
	
def cuts(q):        #each query should be < O(n)
    global al,dsu,l
    if q[0]==1:
        i = q[1]-1
        if a[i]>l:  #  already LONG enough
            continue
        al[i] += q[2]
        if a[i]<=l: #still NOT LONG enough
            continue
        mleft  = (i>0)  and (al[ii-1])>l    #merge left condition
        mright = (i<n-1)and (al[ii+1])>r    #merge right condition
        if mleft:
            self.union(ii,i)
         
    return dsu.num_cuts

n,m,l   = list(map(int,input().split()))    #1e5,1e5,1e9
al      = list(map(int,input().split()))    #1e9

[print(cuts(al,list(map(int,input().split())))) for _ in range(m)]
