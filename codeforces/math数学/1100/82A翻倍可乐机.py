#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/82/A

def f(n):
    l  = ['Sheldon', 'Leonard', 'Penny', 'Rajesh','Howard']
    pl = [5*(2**i-1) for i in range(1,33)]    #1,3,7,..
    for i in range(33):
        if pl[i]>=n:
            break
    if i==0:
        return l[n-1]
    n -= pl[i-1]
    return l[n//(1<<i)]

n = int(input())
print(f(n))
