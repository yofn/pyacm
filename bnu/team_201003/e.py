#!/usr/bin/env python3

#https://codeforces.com/group/H9K9zY8tcT/contest/297617

def f(l):
    c2i = lambda c: ord(c)-ord('a')
    p   = 11092019
    cl  = [1]*26 # 1 for not having this c;
    l   = list(map(c2i,l))
    for i in l:
        cl[i] += 1
    c   = 1
    for i in cl: 
        c *= i
        if c>p:
            c=c%p
    return c

l = list(input())
print(f(l))
