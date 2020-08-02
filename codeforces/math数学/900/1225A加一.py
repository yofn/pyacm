#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1225/B
# 太简单了?
# 没考虑9+1=10的情况..

def f(l):
    a,b = l
    if a != b and a != b-1 and (a!=9 or b!=1):
        return [-1]
    return [b*10,b*10+1] if a==b else [b*10-1,b*10]

l = list(map(int,input().split()))
print(*f(l))

