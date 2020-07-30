#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/758/A

n   = int(input())
al  = list(map(int,input().split()))
print(max(al)*n-sum(al))

