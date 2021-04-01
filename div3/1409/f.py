#!/usr/bin/python3
#https://codeforces.com/contest/1409/problem/F
#比初步看起来难一点!
#DP? modify k times = modify k-1 times + ..

def f(s,t,n,k):
    x2a = lambda a_,_b: _b
    b2a = lambda a_,_b: _b-a_
    x2b = lambda a_,_b: a_
    a2b = lambda a_,_b: a_-_b
    a,b      = t
    ct       = 0
    al,bl    = [0]*n,[0]*n  #how many a before and how many b after!
    for i in range(n-1):
        al[i+1]=a[i]+(s[i]==a)
    for i in range(n-1,0,-1):
        bl[i-1]=b[i]+(s[i]==b)
    for i in range(n):
        if s[i]==b:
            ct += al[i]
    i  = 0
    j  = n-1
    while k>0:
        while i<n  and s[i]==a:
            i += 1
        while j>=0 and s[j]==b:
            j -= 1
        # now i,j points to exchangable or OutOfBound
        if i<n:
            leftgain = b2a(al[i],bl[i]) if s[i]==b
    return ct


n,k = map(int,input().split())
s   = list(input())
t   = list(input())
print(f(s,t,n,k))
