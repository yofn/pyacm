#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/486/A
# 找规律, 奇偶分别考虑

n = int(input()) 
print( n//2 if n%2==0 else -(n+1)//2)

