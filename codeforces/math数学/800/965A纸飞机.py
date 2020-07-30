#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/965/A

k,n,s,p = list(map(int,input().split()))
print((k*((n+s-1)//s)+p-1)//p)
