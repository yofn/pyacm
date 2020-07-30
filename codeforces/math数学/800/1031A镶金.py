#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1031/A
# 

w,h,k   = list(map(int,input().split()))
print(2*k*(w+h+2-4*k))

