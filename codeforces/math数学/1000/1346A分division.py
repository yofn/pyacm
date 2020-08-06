#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1346/A

t = int(input())
for _ in range(t):
    n,k = list(map(int,input().split()))
    f   = n//(1+k+k*k+k*k*k)
    print(f,f*k,f*k*k,f*k*k*k)
