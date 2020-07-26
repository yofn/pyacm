#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/92/A

n,m = list(map(int,input().split()))    #50,1e4
cc  = (n*(n+1))//2
m   = m%cc
cl  = [((i+1)*(i+2))//2 for i in range(n)]
for i in range(1,n+1):
    if  m >= i:
        m -= i
    else:
        print(m)
        break
