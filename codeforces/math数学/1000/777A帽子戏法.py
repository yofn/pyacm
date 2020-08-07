#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/777/A

def f(l):
    n,x = l
    h0  = [0,1,1,2,2,0]
    h1  = [1,0,2,1,0,2]
    h2  = [2,2,0,0,1,1]
    hs  = [h0,h1,h2]
    return hs[x][n%6]

l = [int(input()) for _ in range(2)]
print(f(l))
