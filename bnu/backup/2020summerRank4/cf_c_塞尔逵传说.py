#!/usr/bin/env python3
# 2020暑期排位4C (是贪心! 不是DP ..是本回合临时增加!!)
# https://iammao.github.io/2019/04/26/2019BITCPC/

# input phase
n,k,c   = list(map(int,input().split()))
ms      = [None]*n
for i in range(n):
    d,x     = list(map(int,input().split()))
    ms[i]   = (x,(d-1)//k)
# process phase
ms  = sorted(ms,key=lambda m:-m[0])
bc  = 0
for m in ms:
    ate = min(m[1],c)
    c  -= ate
    bc += m[0]*(m[1]-ate)
print(bc)
