#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1118/A

t = int(input())
for _ in range(t):
    n,a,b   = list(map(int,input().split()))
    print(n*a if (a<<1)<=b else (n//2)*b+(n%2)*a)
