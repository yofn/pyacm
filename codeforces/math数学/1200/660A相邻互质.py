#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/660/A

gcd = lambda a,b: a if b==0 else gcd(b,a%b)

def f(l):
    n  = len(l)
    nl = [l[0]]
    i  = 0
    while i<n-1:
        a,b = l[i],l[i+1]
        g   = gcd(a,b) if a>b else gcd(b,a)
        if g > 1:
            #nl.append((a*b)//g + 1)
            nl.append(1)
        nl.append(l[i+1])
        i  += 1
    return [[len(nl)-n],nl]


_  = int(input())
l  = list(map(int,input().split()))
[print(*r) for r in f(l)]
