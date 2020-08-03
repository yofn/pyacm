#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/376/A
# 读题不如看图的例子

def f(s):
    i = s.index('^')
    s = [0 if c=='^' or c=='=' else int(c) for c in s]
    l = s[:i+1] #include ^ for 0
    r = s[i:]   #include ^ for 0
    l.reverse()
    lw  = sum([i*l[i] for i in range(len(l))])
    rw  = sum([i*r[i] for i in range(len(r))])
    if lw==rw:
        return 'balance'
    return 'left' if lw>rw else 'right'

s  = list(input())
print(f(s))

