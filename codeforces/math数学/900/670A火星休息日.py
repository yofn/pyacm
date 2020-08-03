#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/670/A

n   = int(input())
print( 2*(n//7) + max(0,n%7-5), 2*(n//7) + min(2,n%7))

