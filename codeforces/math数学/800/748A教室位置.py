#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/748/A

n,m,k   = list(map(int,input().split()))
print((k+(m<<1)-1)//(m<<1), ((k-1)//2)%m+1, ['R','L'][k%2])
