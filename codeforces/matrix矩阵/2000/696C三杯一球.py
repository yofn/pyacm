#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/696/C

p       = int(1e9)+7
inv2    = int(5e8)+4
inv3    = (p+1)//3

def binpower(b,e):
    r = 1
    while e:
        if e&1: r = (r*b)%p
        e = e>>1
        b = (b*b)%p
    return r

def f(l):
    r   = 2   #will=2^n%p
    odd = True
    for a in l:
        odd = odd and a%2
        r   = binpower(r,a%(p-1)) #Fermat's Little Theorem
    fm = (r*inv2)%p
    fz = fm + (-1 if odd else 1)
    fz = (fz*inv3)%p
    return '%d/%d'%(fz,fm)

_   = input()
l   = list(map(int,input().split()))
print(f(l))

