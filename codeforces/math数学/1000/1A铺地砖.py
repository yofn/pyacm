#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1/A

n,m,a = list(map(int,input().split()))
print( ((n+a-1)//a) * ((m+a-1)//a) ) #NOTE: *op > //op!
