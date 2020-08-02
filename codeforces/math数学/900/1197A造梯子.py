#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1197/A

def f(l):
    if len(l)<3:
        return 0
    l.sort()
    return min(l[-2]-1,len(l)-2) 

t  = int(input())
for _ in range(t):
    _   = input()
    l   = list(map(int,input().split()))
    print(f(l))

