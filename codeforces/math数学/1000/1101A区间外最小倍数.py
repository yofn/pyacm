#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1101/A

def f(ll):
    l,r,d = ll
    if l>d:
        return d
    return (r//d+1)*d

t = int(input())
for _ in range(t):
    l = list(map(int,input().split()))
    print(f(l))
