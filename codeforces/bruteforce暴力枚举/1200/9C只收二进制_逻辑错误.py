#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/9/C
#failed @ 100

def f(n):
    m = n
    k = 0
    s = 0
    while m>0:
        m  = m//10
        k += 1
        s  = s*10 + 1
    return (2**k)-(1 if n>=s else 2)

n = int(input())
print(f(n))
