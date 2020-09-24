#!/usr/bin/env python3

# 2020暑期排位5B_primes (必有一个是2!!)
# https://codeforces.com/group/H9K9zY8tcT/contest/286081/problem/B
import math

def splitPrimes(x):
    if x<5: return [-1]
    b = x-2
    for i in range(2, int(math.sqrt(b))+1):
        if b % i == 0: return [-1]
    return [2,x-2]

x = int(input())
print(*splitPrimes(x))

