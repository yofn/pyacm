#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/157/B


from math import pi
n   = int(input())
tl  = list(map(int,input().split()))
tl.sort()
print(pi*sum([((-1)**((n-i-1)%2))*(tl[i]**2) for i in range(n)]))
