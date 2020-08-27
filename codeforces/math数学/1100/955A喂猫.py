#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/955/A
# 只有两个选择: 立刻或等到20点

def f(l1,l2):
    hh,mm   = l1
    h,d,c,n = l2
    m   = hh*60+mm
    if m>1200:
        return 0.8*c*((h+n-1)//n)
    h2  = h + (1200-m)*d
    return min(c*((h+n-1)//n), 0.8*c*((h2+n-1)//n))

l1 = list(map(int,input().split()))
l2 = list(map(int,input().split()))
print(f(l1,l2))
