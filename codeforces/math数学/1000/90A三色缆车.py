#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/90/A
# 注意不能先求max, 例如90,89情况

def f(l):
    l  = [(i-1)//2 for i in l]
    mx = 0
    mp = 0
    for i in range(3):
        if l[i] >= mx:
            mx   = l[i]
            mp   = i
    return 30 + mx*3 + mp

l = list(map(int,input().split()))
print(f(l))
