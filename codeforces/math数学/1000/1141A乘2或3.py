#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1141/A

def f(l):
    if l[1]%l[0]>0:
        return -1
    m = l[1]//l[0]
    c = 0
    while m%2==0:
        m  = m//2
        c += 1
    while m%3==0:
        m  = m//3
        c += 1
    return -1 if m>1 else c

l = list(map(int,input().split()))
print(f(l))
