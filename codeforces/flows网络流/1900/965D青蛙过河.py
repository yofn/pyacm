#!/usr/bin/env python3

def f(n,l):
    m = len(l)
    if n==1: return min(l)
    if n==m: return sum(l)
    ans = sum(l[:n])
    new = ans
    for i in range(1,m-n):
        new = new+l[i-1+n]-l[i-1]
        if new<ans:
            ans=new
    return ans

w,n =  list(map(int,input().split()))
l   =  list(map(int,input().split()))
print(f(n,l))

