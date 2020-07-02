#!/usr/bin/env python3

# 2020暑期训练1

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
    #print tt-fa, nap, non
    return fa + non*t2a

n  = int(input())
ll = []
for i in range(n):
    sl = input().split()
    #print(sl)
    il = [int(s) for s in sl]
    #print(il)
    ll.append(il)
for il in ll:
    print(getup(il))



'''
print getup(10,3,6,4)
print getup(11,3,6,4)
print getup(5,9,4,10)
print getup(6,5,2,3)
print getup(1,1,1,1)
print getup(3947465,47342,338129,123123)
print getup(234123843,13,361451236,361451000)
'''

