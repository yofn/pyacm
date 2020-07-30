#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1223/A

t = int(input())
for _ in range(t):
    n   = int(input())
    print(n%2 if n>3 else 4-n)
