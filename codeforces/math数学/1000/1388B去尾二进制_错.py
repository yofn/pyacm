#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1388/B

t = int(input())
for _ in range(t):
    n   = int(input())
    nz  = n//4
    n8  = 1 if n%4>0 else 0
    n9  = n-n8-nz
    print(''.join(['9']*n9+['8']*n8+['0']*nz))
