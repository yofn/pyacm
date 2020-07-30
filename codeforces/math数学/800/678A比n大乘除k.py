#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/678/A

n,k = list(map(int,input().split()))
print( k + (n//k)*k )
