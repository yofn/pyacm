#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1328/A

t  = int(input())
rl = []
for i in range(t):
    a,b = list(map(int,input().split()))
    rl.append((b-a%b)%b)
[print(r) for r in rl]
     
