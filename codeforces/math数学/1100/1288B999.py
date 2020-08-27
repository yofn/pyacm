#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1288/B

def f(l):
    A,B = l
    i   = 0
    mx  = 9
    while B>=mx:
        mx = mx*10 + 9
        i += 1
    return i*A

q = int(input())
for _ in range(q):
    l = list(map(int,input().split()))
    print(f(l))
