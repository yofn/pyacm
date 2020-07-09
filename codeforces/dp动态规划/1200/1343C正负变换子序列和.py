#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1343/C
# 可以贪心,可以DP; 但DP似乎优雅些

def msms(a):
    rmax = a[0] 
    ss   = rmax
    for i in range(1,len(a)):
        if a[i]*rmax<0:
            ss  += a[i]
            rmax = a[i]
            continue
        if a[i]>rmax:
            ss  += a[i]-rmax
            rmax = a[i]
    return ss

rl  = []
for i in range(int(input())):
    _ = int(input())
    a = list(map(int,input().split()))
    rl.append(msms(a))
[print(r) for r in rl]
