#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/463B

def f(l):
    return max(l)

_ = input()
l = list(map(int,input().split()))
print(f(l))
