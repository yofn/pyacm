#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1277/A

def f(lol):
    ll = [l[0] for l in lol]    #left  list
    rl = [l[1] for l in lol]    #right list
    l  = min(rl)
    r  = max(ll)
    return 0 if l>=r else r-l

q = int(input())
for _ in range(q):
    n = int(input())
    l = [list(map(int,input().split())) for _ in range(n)]
    print(f(l))
