#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1176/B

def f(l):
    ml = [0,0,0]
    for i in l:
        ml[i%3] += 1
    return ml[0] + min(ml[1:]) + (max(ml[1:])-min(ml[1:]))//3

q = int(input())
for _ in range(q):
    _ = input()
    l = list(map(int,input().split()))
    print(f(l))
