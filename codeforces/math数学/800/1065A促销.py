#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1065/A

t = int(input())
for _ in range(t):
    s,a,b,c = list(map(int,input().split()))
    print((s//c//a)*(a+b)+(s//c%a))
