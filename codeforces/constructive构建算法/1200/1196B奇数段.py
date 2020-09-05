#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/1196/B
#贪心构建..
#比想象的复杂...可能是逻辑不够简练..
#tc2错了好多次
#tc3又超时, 不能用sum?? python的问题? 换成python3就好了,因为PyPy处理输入太慢!

def f(l1,l):
    n,k = l1
    if sum(l)%2!=k%2:
        return [['NO']]
    dl  = []
    s   = 0
    for i in range(n):
        s += l[i]
        if s%2>0:
            if len(dl)==k-1:
                break
            dl.append(i+1)
            s = 0
    if len(dl)==0 or dl[-1]<n:  #avoid runtime error
        dl.append(n)
    return [['NO']] if len(dl)<k else [['YES'],dl]

q = int(input())    #2e5
for _ in range(q):
    l1 = list(map(int,input().split())) #2e5
    l2 = list(map(int,input().split())) #1e9
    [print(*r) for r in f(l1,l2)]
