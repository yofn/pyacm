#!/usr/bin/env python3
#ccpc20qhda

gcd = lambda a,b: b if a==0 else gcd(b%a,a)

t = int(input())
for i in range(t):
    m,n = list(map(int,input().split()))
    aa  = m*(m-1)
    bb  = (m+n)*(m+n-1)
    c   = gcd(aa,bb)
    print('Case #%d: %d/%d'%(i+1,aa//c,bb//c))
