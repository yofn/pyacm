#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1182/A
n   =   int(input())
print(2**(n//2) if n%2==0 else 0)
