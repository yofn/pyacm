#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/630/A


gcd = lambda b,s: b if s==0 else gcd(s,b%s)
lcm = lambda a,b: (a*b)//gcd(a,b)   #make sure a>=b

def f(n):
    x = 10
    for i in range(9,1,-1):
        x = lcm(x,i)
    return n//x

n = int(input())
print(f(n))
