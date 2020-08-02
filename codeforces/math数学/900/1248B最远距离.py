#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1248/B
# X和Y的最大平方和

def f(l):
    l.sort()
    h = len(l)//2
    y = sum(l[:h])
    x = sum(l[h:])
    return x*x+y*y

_ = input()
l = list(map(int,input().split()))
print(f(l))

