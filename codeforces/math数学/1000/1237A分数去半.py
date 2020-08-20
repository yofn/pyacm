#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1237/A

def f(l):
    dl = [-1,1]
    ii = 0
    for i in range(len(l)):
        if l[i]%2>0:
            l[i] += dl[ii]
            ii    = (ii+1)%2
        l[i] = l[i]//2
    return l

n =  int(input())
l = [int(input()) for _ in range(n)]
[print(r) for r in f(l)]
