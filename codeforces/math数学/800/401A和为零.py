#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/401/A

_,x = list(map(int,input().split()))
cl  = list(map(int,input().split()))
ss  = -sum(cl) 
ss  = ss if ss>0 else -ss
print((ss+x-1)//x)
