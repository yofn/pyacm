#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1351/B

def f(l):
    return max(l[0])==max(l[1]) and min(l[0])+min(l[1])==max(l[0])

t  = int(input())
for _ in range(t):
    l   = [list(map(int,input().split())) for _ in range(2)]
    print('Yes' if f(l) else 'No')

