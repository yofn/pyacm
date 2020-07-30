#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/750/A

import math
n,k = list(map(int,input().split()))
if k>=240:
    print(0)
else:
    i   = math.ceil(math.sqrt(95.75-0.4*k)-0.5)
    if i*(i+1)*5 > ((240-k)<<1):
        i -= 1
    print(min(n,i))
