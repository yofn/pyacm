#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1263/A
# 直觉: min(max(l),sum(l)-max(l)) <--错误!

def f(l):
    l1,r1,l2,r2,k = l
    l = max(l1,l2)
    r = min(r1,r2)
    if r<l:
        return 0
    return r-l+1 if (k<l or k>r) else r-l

l = list(map(int,input().split()))
print(f(l))
