#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/385/B
#会有冲突的情况..

def f(s):
    n  = len(s)
    c  = 0
    ll = 0
    for i in range(n-3):
        if s[i:i+4] == 'bear':
            l  = i-ll+1
            r  = n-i-3
            c += l*r
            ll = i+1
    return c

s = input()
print(f(s))
