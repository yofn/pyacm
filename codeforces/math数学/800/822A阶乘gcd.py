#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/822/A

import math
a,b = list(map(int,input().split()))
m   = min(a,b)
print(math.factorial(m))

