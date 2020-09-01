#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/633/A

def f(l):
    a,b,c = l   #100,100,1e4
    if a<b:
        a,b=b,a #let a = bigger
    aa = 0
    while aa<=c:
        if (c-aa)%b==0:
            return True
        aa += a
    return False

l = list(map(int,input().split()))
print('Yes' if f(l) else 'No')
