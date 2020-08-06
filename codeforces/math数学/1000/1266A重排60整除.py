#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1266/A
# 错误:没考虑0是对应0而不是0000

t = int(input())
for _ in range(t):
    s   = list(input())
    l   = [int(c) for c in s]
    l.sort()
    red = sum(l)%3==0 and l[0]==0 and sum([i%2==0 for i in l[1:]])>0
    print('red' if red else 'cyan')
