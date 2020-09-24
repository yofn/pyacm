#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/875/A
#bound住!

def s(m):
    c = 0
    while m>0:
        c += m%10
        m  = m//10
    return c

def f(n):
    m = n
    k = 0
    while m>0:
        m  = m//10
        k += 1
    i = 0
    b = k*9
    l = []
    for i in range(b+1):
        if s(n-i)==i:
            l.append(n-i)
    l.reverse()
    return [len(l)] + l

n = int(input())
[print(r) for r in f(n)]
