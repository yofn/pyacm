#!/usr/bin/env python3
#ccpc20qhd-g

def f(n,k):
    if k==1:
        return n
    i  = 1
    c  = 0
    while True:
        m1 = i**k
        m2 = min((i+1)**k-1,n)
        if m2<=m1:
            break
        c += m2//i - m1//i + (1 if m1%i==0 else 0)
        i += 1
    return c

t = int(input())
for i in range(t):
    n,k =  list(map(int,input().split()))
    print('Case #%d: %d'%((i+1), f(n,k)))

