#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/44/E
#https://codeforces.com/blog/entry/833 

def split(s,k,a,b):
    n   = len(s)
    if a*k > n or b*k < n:
        return ['No solution']
    rl  = []
    ii  = 0
    for i in range(k-1):
        l   = (n-ii) // (k-i)
        r   = (n-ii)  % (k-i)
        jj  = ii+l if r < (k-i+1)//2 else ii+l+1 
        rl.append(s[ii:jj])
        #print(l,r,s[ii:jj])
        ii  = jj
    rl.append(s[ii:])
    return rl

k,a,b   = list(map(int,input().split()))
s       = input()
[print(r) for r in split(s,k,a,b)]

