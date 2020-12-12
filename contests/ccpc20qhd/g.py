#!/usr/bin/env python3
#ccpc20qhd-g
'''
10
2313 2
1321432 3
31243423 4
43242423 5
54353455 7
123432245 10
354353554 993244353 <---
432444234 100
888244353 2
926081711 1
'''

def fpower(b,e):
    r = 1
    while e:
        if e & 1:   # bit operation
            r *= base
        b *= b      # b, b2, b4, b8, ...
        e  = e >> 1
    return r

def tfp(b,e,n):     #twisted fast power
    r = 1
    while e:
        if e & 1:   # bit operation
            r *= b
            if r>=n:
                return [n+1, True]  #True=overflow
        b *= b      # b, b2, b4, b8, ...
        e  = e >> 1
    return [r, False]

def f(n,k):
    if k==1:
        return n
    i   = 1
    c   = 0
    l   = 1
    o   = False
    while not o:
        r,o  = tfp(i+1,k,n)
        c   += (r-1)//i - l//i + (l%i==0)
        l    = r
        i   += 1
    return c

t = int(input())
for i in range(t):
    n,k =  list(map(int,input().split()))
    print('Case #%d: %d'%((i+1), f(n,k)))

