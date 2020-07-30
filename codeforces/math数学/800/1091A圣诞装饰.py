#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1091/A

l     = list(map(int,input().split()))
l[0] += 1
l[2] -= 1
print(3*min(l))
