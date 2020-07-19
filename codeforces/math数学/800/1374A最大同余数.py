#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1385/A

xynl = [list(map(int,input().split())) for _ in range(int(input()))]
for xyn in xynl:
    x,y,n = xyn
    print(n-n%x+y if n%x>=y else n-n%x+y-x) 
