#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/932/A

         
s  = list(input())
r  = s.copy()
r.reverse()
print(''.join(s+r[1:]))

