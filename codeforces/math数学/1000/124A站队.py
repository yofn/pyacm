#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/124/B

n,a,b = list(map(int,input().split()))
print(min(b+1,n-a))
