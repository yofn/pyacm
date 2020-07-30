#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/851/A

n,k,t   = list(map(int,input().split()))
print(min(t,n+k-t,k))
