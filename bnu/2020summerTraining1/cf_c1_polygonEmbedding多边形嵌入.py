#!/usr/bin/env python3

#https://codeforces.com/group/H9K9zY8tcT/contest/283972/problem/C1

import math

def square(i):
    return 1.0/math.tan(math.pi/(2*i))

n  = int(input())
ll = []
for i in range(n):
    ll.append(int(input()))
for i in ll:
    print(square(i))


