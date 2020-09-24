#!/usr/bin/env python3

# 2020暑期训练1

def nor(ps):
    n = len(ps)
    hasMet = [None]*(n+1)
    numRom = list(range(n+1,1,-1))
    rr = n
    for i in range(n-1,-1,-1):
        c = ps[i]
        if c>0:
            hasMet[c]=i
        if c<0: 
            r = hasMet[-c]
            if r is not None and r < rr:
                rr = r
        numRom[i] = rr-i
    return numRom

'''
assert(nor([1,-1,-1,1,-1,1])==[3,2,1,2,1,1])
assert(nor([2,-1,-2,-3,1,3,2])==[4,3,3,2,3,2,1])
'''
n  = int(input())
sl = input().split()
il = [int(s) for s in sl]
print(*nor(il))

