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

pp = int(1e9)+7
def binpow(b,e):
    r = 1
    while True:
        if e &1: r=(r*b)%pp
        e = e>>1
        if e==0: break
        b = (b*b)%pp
    return r

def f(p,l,n):  #pattern, match list, size of text
    m  = len(p)
    if len(l)==0:
        return binpow(26,n)
    z  = preZ(p)
    s  = set([i for i in range(m) if z[i]+i==m])
    fc = l[0]-1
    for i in range(1,len(l)):
        r  = l[i-1]+m
        if l[i]>r:
            fc += l[i]-r
            continue
        if l[i]<r and l[i]-l[i-1] not in s:
            return 0
    fc += n-(l[-1]+m-1)
    return binpow(26,fc)

n,m = list(map(int,input().split()))
p   = input()
l   = list(map(int,input().split())) if m>0 else []
print(f(p,l,n))
