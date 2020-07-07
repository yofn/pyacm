#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/313/B

s   = input()
m   = int(input())
n   = len(s)
t   = [0]*(n+1)
for i in range(1,n):
    if s[i]==s[i-1]:
        t[i] += 1
    t[i+1]=t[i]
for i in range(m):
    l, r = input().split()
    j    = int(l)-1
    k    = int(r)-1
    print(t[k]-t[j])
