#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1355/B

def groups(a):
    a.sort()
    nog = 0
    i   = len(a)-1
    while True:
        i    = i-a[i]
        if i<-1:    #-1 is allowed
            break
        nog += 1
    return nog

rl  = []
for i in range(int(input())):
    _ = int(input())
    a = list(map(int,input().split()))
    rl.append(groups(a))
[print(r) for r in rl]
