#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1294/A

w1,h1,w2,h2 = list(map(int,input().split()))
print((w1+h1+h2+2)<<1)
