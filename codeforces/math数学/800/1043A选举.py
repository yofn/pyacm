#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1043/A

n   = int(input())
al  = list(map(int,input().split()))
print(max(max(al),((sum(al)<<1)+n)//n))
