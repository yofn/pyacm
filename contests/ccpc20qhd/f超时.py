#!/usr/bin/env python3
'''
#ccpc20qhd-f => 最大联通子图
#如果都是联通的,所有节点都要放进去,
#友好值=联通子图中边的个数-点的个数
#应该所有(友好值>0)联通子图加起来?
#DFS搜索,或者是并查集? 数一数有多少联通块?
#最短路用广搜，全部解用深搜

连通图的复杂度是O(V+E)..
为什么会Runtime Error?

分析:
    解法1: DFS做联通块
    解法2: 看不包含哪些人，相当于走个捷径!

'''

def f(n,l):
    el  = [[] for _ in range(n)]
    for x,y in l:
        if x>y:
            x,y=y,x
        el[x-1].append(y-1)     #make sure edge is from small to BIG!
    uzd = [False]*n     #uzed node
    st  = [0]*n         #stack!
    fv  =  0
    print(el)
    for i in range(n):
        if uzd[i]:
            continue
        sp      = 0
        st[sp]  = i     #PUSH
        nn      = 0
        ne      = 0
        while sp>-1:
            ii         = st[sp]     #POP a node as source node
            sp        -= 1
            if uzd[ii]:
                continue
            nn        += 1
            uzd[ii]    = True
            for j in el[ii]:
                ne    += 1          #ii=>j
                if not uzd[j]:      #make sure edges are checked and counted ONCE!
                    sp    += 1
                    st[sp] = j
        fv += max(0,ne-nn)
    return fv

t = int(input())
for i in range(t):
    n,m =  list(map(int,input().split()))
    l   = [list(map(int,input().split())) for _ in range(m)]
    print('Case #%d: %s'%((i+1), f(n,l)))

