#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/789/A

def f(l1,l2):
    n,k = l1
    ps  = sum([(w+k-1)//k for w in l2])
    return (ps+1)//2

l1 = list(map(int,input().split()))
l2 = list(map(int,input().split()))
print(f(l1,l2))
