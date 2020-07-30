#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1270/A

t = int(input())
for _ in range(t):
    n,k1,k2 = list(map(int,input().split()))
    al  = list(map(int,input().split()))
    bl  = list(map(int,input().split()))
    print('YES' if max(al)>max(bl) else 'NO')
