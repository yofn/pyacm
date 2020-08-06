#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1256/A
# a,b,n,S

def f(l):
    a,b,n,s = l
    if s>a*n+b:
        return False
    if n<=b:
        return True
    return s%n<=b

t = int(input())
for _ in range(t):
    l = list(map(int,input().split()))
    print('YES' if f(l) else 'NO')
