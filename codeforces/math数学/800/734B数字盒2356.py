#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/734/B

k2,k3,k5,k6 = list(map(int,input().split()))
b1      = min(k2,k5,k6)
b2      = min(k2-b1,k3)
print((b1<<8) + (b2<<5))
