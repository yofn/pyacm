#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1271/A

a,b,c,d,e,f = [int(input()) for _ in range(6)]
d1  = min(d,a)      if e>f else min(d,b,c)
d2  = d-d1
d2  = min(d2,b,c)   if e>f else min(d2,a)
print(d1*e+d2*f     if e>f else d1*f+d2*e)
