#!/usr/bin/python3
#@profile
'''
最优方案一定是单方向转动?
不一定??
但我们可以看两个不同方向下,分别所需要的最大时间...
首先可以先排序..然后就是找分割点的问题..找好分割点就是相当于找好了对应..
怎么证明??  !!!不能存在交叉的边，因为如果有交叉的边，则可以有更好的交替路！
'''

def f(al,bl,n,k):
    al.sort()
    bl.sort()
    al  = [a-n for a in al] + al + [a+n for a in al]
    cst = 1e9
    for i in range(2*k+1):
        t1,t2   = 0,0
        dl  = [al[i+j]-bl[j] for j in range(k)]
        c1  = max(-min(dl),0)
        c2  = max( max(dl),0)
        nc  = min(c1,c2) + c1 + c2
        cst = nc if nc<cst else cst
    return cst

T   = int(input())
for _ in range(T):
    n,k =      map(int,input().split())
    al  = list(map(int,input().split()))
    bl  = list(map(int,input().split()))
    print(f(al,bl,n,k))
