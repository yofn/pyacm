#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1041/B

def gcd(a,b):
    if a<b:
        a,b=b,a
    if b==0:
        return a
    return gcd(b,a%b)

def f(ll):
    a,b,x,y = ll    #3e5
    g = gcd(x,y)
    x = x // g
    y = y // g
    return min(a//x,b//y)

l = list(map(int,input().split()))
print(f(l))
