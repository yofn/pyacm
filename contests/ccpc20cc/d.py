#!/usr/bin/python

def f(l):
    n,c  = l.split() #n is binary representation (2^3000), c is decimal (1e9)
    n    = list(map(int,list(n)))
    n.reverse()
    mod  = int(1e9 + 7)
    c    = int(c)
    cp1  = c+1
    F    = 1
    base = 1
    for b in n:
        if b==1:
            F = (base + c*F) % mod
        base = (base*cp1) % mod
    return F
 
l = input()
print(f(l))
