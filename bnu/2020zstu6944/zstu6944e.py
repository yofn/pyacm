#!/usr/bin/env python3

n,dx    = [int(s) for s in input().split()]
xs      = [int(s) for s in input().split()]
xs.sort()

m = n // 2 

moved = 0
for i in range(n):
    moved += abs(xs[m]+(i-m)*dx-xs[i])

print(moved)
