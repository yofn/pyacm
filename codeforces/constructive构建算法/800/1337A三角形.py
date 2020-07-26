#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1353/A
# 最大的放一个,两边各一个0?

t = int(input())
for _ in range(t):
    a,b,c,d = list(map(int,input().split()))
    print(*[b,c,c])
