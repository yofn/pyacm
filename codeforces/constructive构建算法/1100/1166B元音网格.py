#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1166/B
# 分解成m*n使得两者都>=5!

def f(n):
    if n<25:
        return -1
    c  = 5
    while n%c>0:
        c+= 1
    r = n//c
    if r<5:
        return -1
    v = 'a e i o u'.split()
    l = [v[i%5] for i in range(c)]
    s = []
    for i in range(r):
        [s.append(cc) for cc in l]
        l = l[1:]+[l[0]]
    return ''.join(s) 

n = int(input())
print(f(n))
