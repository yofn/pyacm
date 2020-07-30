#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1209/A

n   = int(input())  #100
al  = list(map(int,input().split()))
al.sort()
c   = 0
for i,d in enumerate(al):
    if d is None:
        continue
    c += 1
    for j in range(i+1,n):
        if al[j] is not None and al[j]%d==0:
            al[j] = None
print(c)
