#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/659/A

def f(l):
    n,a,b = l   #n=circle, a=start, b=steps
    return 1+(a+b-1)%n

l = list(map(int,input().split()))
print(f(l))
