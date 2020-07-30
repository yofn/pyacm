#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/747/A

n  = int(input())
l  = [2]*(n//2)
l[-1] += n%2
print(n//2)
print(*l)
