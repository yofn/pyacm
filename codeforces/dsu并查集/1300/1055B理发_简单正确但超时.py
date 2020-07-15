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
#好像简单的更容易实现!

n,m,l       = list(map(int,input().split()))    #1e5,1e5,1e9
al          = list(map(int,input().split()))    #1e9
num_cuts    = sum([al[0]>l] + [al[i]<=l and al[i+1]>l for i in range(n-1)])
for _ in range(m):  #each query should be < O(n)
    q   = list(map(int,input().split()))
    if q[0]==0:
        print(num_cuts)
        continue
    i = q[1]-1
    if al[i]>l:  #  already LONG enough
        continue 
    al[i] += q[2]
    if al[i]<=l: #still NOT LONG enough
        continue 
    mleft  = i>0   and al[i-1]>l    #merge left condition
    mright = i<n-1 and al[i+1]>l    #merge right condition
    if mleft and mright:
        num_cuts -= 1
    if (not mleft) and (not mright):
        num_cuts += 1

