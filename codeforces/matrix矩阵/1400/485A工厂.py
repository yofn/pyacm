#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/485/A

def f(l):
    a,m = l
    for i in range(m):
        x  = a%m
        if x==0:
            return 'Yes'
        a += x
    return 'No'

l = list(map(int,input().split()))
print(f(l))

