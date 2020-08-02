#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1208/A
# xor性质~~

def f(l):
    a,b,n   = l
    l[2]    = a^b
    return l[n%3]

t  = int(input())
for _ in range(t):
    l   = list(map(int,input().split()))
    print(f(l))

