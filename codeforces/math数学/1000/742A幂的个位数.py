#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/742/A
# 1378**n的最后一位
# 1,2,3,4,5,6,..
# 8,4,2,6,8,4,..

def f(n):
    l = [6,8,4,2]
    if n==0:
        return 1
    return l[n%4]

n = int(input())
print(f(n))
