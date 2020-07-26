#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1300/A

t = int(input())
for _ in range(t):
    n   = int(input())
    al  = list(map(int,input().split()))
    ss  = sum(al)
    cz  = sum([al[i]==0 for i in range(n)])
    print(cz if ss!=-cz else cz+1)
