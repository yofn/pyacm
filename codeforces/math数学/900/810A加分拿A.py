#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/810/A
# k*(n+m)-(n+m)/2 < sum(l)

n,k = list(map(int,input().split()))
l   = list(map(int,input().split()))
print(max(0,(k*n-sum(l))*2-n))

