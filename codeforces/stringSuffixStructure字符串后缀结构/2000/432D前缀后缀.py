#!/usr/bin/env python3

#ref: book_DG!

def preZ(s):    #preprocessing by Z algo
    n    = len(s)
    z    = [0]*n
    z[0] = n
    r    = 0
    if n==1: return z
    while r+1<n and s[r]==s[r+1]: r+=1
    z[1] = r #note z=length! not 0-indexed
    l    = 1 if r>0 else 0
    for k in range(2,n):
        bl = r+1-k  #|\beta|
        gl = z[k-l] #|\gamma|
        if gl<bl:
            z[k]=z[k-l] #Case2a
        else:
            j=max(0,r-k+1)  #Case1 & 2b
            while k+j<n and s[j]==s[k+j]: j+=1
            z[k]=j
            l,r =k,k+j-1
    return z

def f(s):
    n  = len(s)
    c  = [0]*(n+1)
    b  = [False]*(n+1)  #is suffix
    z  = preZ(s)
    for i in range(n):
        t     = z[i]
        b[t]  = b[t] or (z[i]+i==n)
        c[t] += 1
    for t in range(n-1,0,-1):
        c[t] += c[t+1]
    return '\n'.join(["%d"%sum(b)] + ["%d %d"%(t,c[t]) for t in range(1,n+1) if b[t]])

print(f(input()))
