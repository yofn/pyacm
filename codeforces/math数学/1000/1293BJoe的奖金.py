#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1293/B
# 1/2 +... + 1/n = ? 没有求和公式! 直接算..

n   = int(input())  #1e5
print(sum([1/i for i in range(1,n+1)]))
