#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/721/B

def f(l,k,p):
    n  = len(l)
    ll = [len(s) for s in l]
    ll.sort()
    cl = len(p)
    fi = ll.index(cl)
    li = fi
    while li<n and ll[li]==cl:
        li += 1
    li = li-1
    return [1+i+5*(i//k) for i in [fi,li]]

n,k =  list(map(int,input().split()))
l   = [input() for _ in range(n)]
p   = input()
print(*f(l,k,p))
