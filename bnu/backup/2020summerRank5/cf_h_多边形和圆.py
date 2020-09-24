#!/usr/bin/env python3

# 2020暑期排位5H_多边形和圆
# https://codeforces.com/group/H9K9zY8tcT/contest/286081/problem/H

import math
v,s = list(map(int,input().split()))
r   = (s/2)/math.sin(math.pi/v)
print(math.pi*r*r)

