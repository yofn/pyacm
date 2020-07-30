#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1296/A

def odd(a,n):
    odd1 = a[0]%2
    if odd1==1 and n%2==1:
        return 'YES'
    for i in range(1,n):
        if a[i]%2 != odd1:
            return 'YES'
    return 'NO'

t = int(input())
for _ in range(t):
    n   = int(input())
    al  = list(map(int,input().split()))
    print(odd(al,n))
