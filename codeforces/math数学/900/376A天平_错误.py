#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/376/A
# 读题不如看图的例子

def f(s):
    isR = False
    w   = 0
    rc  = 1
    for c in s:
        if c=='^':
            isR = True
            continue
        if c=='=':
            if isR:
                rc  += 1
            else:
                w   = (w<<1)
        else:
            i   = int(c)
            w  += -(rc*i) if isR else i
        print(w)
    if w==0:
        return 'balance'
    return 'left' if w>0 else 'right'

s  = list(input())
print(f(s))

