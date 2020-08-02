#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1080/B
# 前缀和?
# -1..+(-n) =?  

fn = lambda n: n//2 if n%2==0 else -(n+1)//2

def f(ll):
    l,r = ll
    return fn(r)-fn(l-1)

t  = int(input())
for _ in range(t):
    l   = list(map(int,input().split()))
    print(f(l))

