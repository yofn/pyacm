#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/500/A
#传送门从i到i+ai


def okay(al,t):
    i = 1
    while i<t:
        i = i+al[i]
    return i==t

n,t = list(map(int,input().split()))        #3e4
al  = [0] + list(map(int,input().split()))  #al
print('YES' if okay(al,t) else 'NO')
