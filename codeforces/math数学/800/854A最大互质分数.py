#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/854/A
# 34: print(n-((n+2)//2),(n+2)//2)

n   = int(input())
l   = [-1,0,-1,1]
u   = ((n//4)<<1)+l[n%4] 
print(u,n-u) 
