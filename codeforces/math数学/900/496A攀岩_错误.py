#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/496/A

n   = int(input())
l   = list(map(int,input().split()))
mi  = l[-1]-l[0]
for i in range(1,n-1):
    if l[i+1]-l[i-1] < mi:
        mi = l[i+1]-l[i-1]
print(mi)

