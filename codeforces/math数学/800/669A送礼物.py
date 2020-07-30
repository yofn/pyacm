#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/669/A

n = int(input())
print((n//3)*2 if n%3==0 else (n//3)*2+1)
