#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1102/A
# 奇数也不是1: print(int(input())%2)是错误的

n = int(input())
print(1 if n%4 in [1,2] else 0)
