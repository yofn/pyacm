#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/479/A

def f(l):
    a,b,c = l
    return max(a+b+c,a*b*c,a*(b+c),(a+b)*c)

l = [int(input()) for _ in range(3)]
print(f(l))
