#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/914/A
# 因为要找最大,可以先排序
# 方案1. 直接把所有平方算出来,然后一一比对?
# 方案2. 用math.sqrt
# 有很好的教学价值: 1.对比两种方案(理论和实际)

def f(l):
    sl = [i*i for i in range(1000,-1,-1)]
    l.sort()
    n  = len(l)
    j  = 0 
    for i in range(n-1,-1,-1):
        while sl[j]>l[i]:
            j  +=  1
            if j>= 1001:
                return l[i]
        if sl[j]<l[i]:
            return l[i]

_   = input()                           #1e3
l   = list(map(int,input().split()))    #1e6
print(f(l))

