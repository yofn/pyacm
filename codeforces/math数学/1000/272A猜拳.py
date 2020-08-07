#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/272/A

def f(l):
    n  = len(l)
    s  = sum(l)
    rl = [(s+i)%(n+1)!=1 for i in range(1,6)]
    return sum(rl)

_ = input()
l = list(map(int,input().split()))
print(f(l))
