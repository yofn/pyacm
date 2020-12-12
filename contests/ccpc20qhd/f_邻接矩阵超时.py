#!/usr/bin/env python3
#ccpc20qhd-f => 最大联通子图
#如果都是联通的,所有节点都要放进去,
#友好值=联通子图中边的个数-点的个数
#应该所有(友好值>0)联通子图加起来?
#DFS搜索,或者是并查集? 数一数有多少联通块?

def f(n,l):
    m   = [False]*(n*n)
    for x,y in l:
        m[(x-1)*n+(y-1)] = True
        m[(y-1)*n+(x-1)] = True
    uzd = [False]*n
    ccl = []    # list of components costs
    st  = [0]*n
    for i in range(n):
        if uzd[i]:
            continue
        sp      = 0
        st[sp]  = i       #stack
        nn      = 1
        ne      = 0
        while sp>-1:
            ii  = st[sp]    #pop top as FROM node
            sp -= 1         #pop is MUST!
            for j in range(n):
                if not m[ii*n+j]:
                    continue
                ne       += 1
                m[ii*n+j] = False    #use edge ONLY once!
                m[j*n+ii] = False
                if uzd[j]:  #visited through other nodes before
                    continue
                sp    += 1
                nn    += 1
                st[sp] = j
                uzd[j] = True
        ccl.append(max(0,ne-nn))
    return sum(ccl)

t = int(input())
for i in range(t):
    n,m =  list(map(int,input().split()))
    l   = [list(map(int,input().split())) for _ in range(m)]
    print('Case #%d: %s'%((i+1), f(n,l)))

