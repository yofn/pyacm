#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1185/A
# 中间不动! 比看起来的难一些!

a,b,c,d = list(map(int,input().split()))
aa  = min([a,b,c])
cc  = max([a,b,c])
bb  = a+b+c-aa-cc
print(max(0,d-cc+bb)+max(0,d-bb+aa))

