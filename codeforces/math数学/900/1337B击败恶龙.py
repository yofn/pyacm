#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1351/B
# 30->41->63->107->195
# 20->21->23->..
# f(0)=m*10; f(n+1)=f(n)*2-19

def f(l):
    x,n,m=l
    return x<=((2**n)*(m*10-19)+19) or x<=m*10

t  = int(input())
for _ in range(t):
    l   = list(map(int,input().split()))
    print('YES' if f(l) else 'NO')

