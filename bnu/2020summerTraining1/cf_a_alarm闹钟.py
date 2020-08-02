#!/usr/bin/env python3

# 2020暑期训练1
# 更好的代码实现见: 数学/900/1354A

import math

#def getup(tt,fa,t2a,t2s):
def getup(il):
    tt,fa,t2a,t2s = il
    if fa>=tt:
        return fa
    nap = t2a - t2s
    if nap<=0:
        return -1
    non = int(math.ceil(float(tt-fa)/nap))
    return fa + non*t2a

n  = int(input())
ll = []
for i in range(n):
    sl = input().split()
    il = [int(s) for s in sl]
    ll.append(il)
for il in ll:
    print(getup(il))

