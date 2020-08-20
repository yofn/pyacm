#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/17/A

def f(l):
    n,k = l
    pl  = [True]*(n+1)  # TRUE=prime or not?
    for i in range(2):
        pl[i] = False
    ll  = n+1
    i   = 2
    while i<ll:
        if pl[i]:               #only for prime
            j  = (i<<1)
            while j<ll:
                pl[j] = False   #non-prime
                j    += i
        i += 1
    pp  = [i for i in range(ll) if pl[i]][1:]   #discard 2 
    nn  = len(pp)
    sl  = [pp[i]+pp[i+1]+1 for i in range(nn-1)]
    l   = [pl[s] for s in sl if s<=n]
    return sum(l)>=k

l = list(map(int,input().split()))  #1e3, 1e3
print('YES' if f(l) else 'NO')
