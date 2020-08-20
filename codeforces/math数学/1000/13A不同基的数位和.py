#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/13/A
# 还得约成最简

gcd = lambda a,b: a if b==0 else gcd(b,a%b)

def f(n):
    s = 0
    for i in range(2,n):
        j = n
        while j>0:
            s += j%i
            j  = j//i
    g = gcd(s,n-2)
    return '%d/%d'%(s//g,(n-2)//g)

n = int(input())    #1000
print(f(n))
