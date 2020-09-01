#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/483/A
# 要a,c不是互质

def f(ll):
    l,r =ll
    if r-l<2 or (r-l==2 and l%2>0):
        return [-1]
    return [l,l+1,l+2] if l%2==0 else [l+1,l+2,l+3]

l = list(map(int,input().split()))
print(*f(l))
