#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/1249/B2
#和B1(1000难度)唯一的区别是约束,从(200,200)->(1000,2e5)
#直接用B1的代码提交通过了...所以不做改动

def al(pl,n):
    pl  = [0]+pl
    rl  = [0]*(n+1)
    for i in range(1,n+1):
        if  rl[i] > 0:
            continue
        p       = i
        uset    = [i]
        while pl[p]!=i:
            p   = pl[p]
            uset.append(p)  #add new node
        for j in uset:
            rl[j] = len(uset)
    return rl[1:]

q = int(input())        #200
for _ in range(q):
    n  = int(input())   #200
    pl = list(map(int,input().split()))
    print(*al(pl,n))

