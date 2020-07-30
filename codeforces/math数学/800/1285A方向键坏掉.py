#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1294/A

_ = input()
s = input()
l = sum([c=='L' for c in s])
r = sum([c=='R' for c in s])
print(l+r+1)
