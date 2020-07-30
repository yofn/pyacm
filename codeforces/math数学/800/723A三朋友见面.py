#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/923/A
# ERROR: 30 20 10; print(sum(l)//2)
# 彻底读错题..

l   = list(map(int,input().split()))
print(max(l)-min(l))
