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

def f(a,b):
    an = len(a)
    bn = len(b)
    if bn==1: return an
    d  = [0]*(an+bn-1)
    for i in range(bn-1): d[i]    =b[i+1]-b[i]
    for i in range(an-1): d[bn+i] =a[i+1]-a[i]
    d[bn-1] = int(3e9)
    z  = preZ(d)
    return sum([z[i]==bn-1 for i in range(1,an+bn-1)])

_ = input()
a = list(map(int,input().split()))
b = list(map(int,input().split()))
print(f(a,b))
