#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/180/F
#1e5所以不能一个个比, 否则(N**2)的复杂度
#复杂度的例子!

def f(l1,l2):
    n  = len(l1)
    t1 = [(l1[i],i) for i in range(n)]
    t2 = [(l2[i],i) for i in range(n)]
    t1.sort(key=lambda t:t[0])
    t2.sort(key=lambda t:t[0])
    p  = [0]*n
    for i in range(n):
        p[t2[i][1]]=t1[i][1]+1
    return p

q  = int(input())
l1 = list(map(int,input().split())) #1e5
l2 = list(map(int,input().split())) #1e5
print(*f(l1,l2))
