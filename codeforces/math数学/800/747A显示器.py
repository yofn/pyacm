#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/747/A

import math
n  = int(input())
r  = int(math.sqrt(n))
while True:
    if n%r==0:
        break
    r -= 1
print(r,n//r)
