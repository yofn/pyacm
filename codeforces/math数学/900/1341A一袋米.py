#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1341/A

def f(l):
    n,a,b,c,d = l
    return (n*(a-b))<=(c+d) and (n*(a+b))>=(c-d)

t  = int(input())
for _ in range(t):
    l   = list(map(int,input().split()))
    print('Yes' if f(l) else 'No')

