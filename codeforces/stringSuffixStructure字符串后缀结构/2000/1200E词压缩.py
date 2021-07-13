#!/usr/bin/env python3

#ref: book_DG!

def maxBorder(s):    #maxBorder based on Z algo
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
        if z[k]+k==n:
            return z[k]
    return 0

def f(l):
    s  = l[0]
    for p in l[1:]:
        n  = min(len(s),len(p))
        s += p[maxBorder(p[:n]+"$"+s[-n:]):]
    return s

_ = input()
print(f(input().split()))
