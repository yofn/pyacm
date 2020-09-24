#!/usr/bin/env python3

# 2020暑期排位5C_套娃
# https://codeforces.com/group/H9K9zY8tcT/contest/286081/problem/C

s,x = list(map(int,input().split()))
n   = 0
while s > 0:
    n  += 1
    s   = s//x
print(n)

