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
    if n==1: return "Just a legend" 
    z    = preZ(s)
    maxm = max(preZ(s[:-1])[1:],default=0)
    ans  = max([z[i] for i in range(n) if z[i]<=maxm and i+z[i]==n],default=0)
    if ans==0: return "Just a legend"
    return s[:ans]

print(f(input()))
