#!/usr/bin/env python3

# 2020暑期排位5B_primes
# https://codeforces.com/group/H9K9zY8tcT/contest/286081/problem/B
import math

def isPrime(x):
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0: return False
    return True

def splitPrimes(x):
    for i in range(2,x//2+1):
        if isPrime(i) and isPrime(x-i):
            return [i,x-i]
    return [-1]

n = int(input())
print(*splitPrimes(n))

