#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/1315/B

for _ in range(int(input())):               #1e4
    a,b,p = list(map(int,input().split()))  #1e5
    s     = input()                         #1e5
    d     = {'A':a,'B':b}
    nw    = len(s) 
    i     = nw-2
    c     = 0
    while i>=0:
        pt   = s[i]  #'A' or 'B'
        while s[i]==pt and i>0:
            i -= 1
        c   += d[pt] #leading of 'A' or 'B' print(s,a,b,p,c,i)
        if c>p:
            break
        nw   = i+1 if s[i]==pt else i+2
    print(nw)

