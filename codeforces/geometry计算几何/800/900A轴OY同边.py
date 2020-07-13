#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/900/A

xs = [list(map(int,input().split()))[0] for _ in range(int(input()))]
np = sum([x>0 for x in xs])
nn = sum([x<0 for x in xs])
print('NO' if np>1 and nn>1 else 'YES')
