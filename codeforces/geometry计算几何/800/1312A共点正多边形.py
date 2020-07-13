#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/1312/A

divok = lambda l: l[0]%l[1]==0
[print('YES' if divok(list(map(int,input().split()))) else 'NO') for _ in range(int(input()))]

