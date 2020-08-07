#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/389/A
# 最大公约数?
# 只要有两个互质的话就可以减到1, 那所有的也都可以减到1!
# 问题=求n个数的最大公约数!!

def gcd(a,b):
    if a<b:
        a,b=b,a
    if b==0:
        return a
    return gcd(b,a%b)

def f(l):
    n = len(l)
    g = l[0]
    for i in range(1,n):
        g = gcd(l[i],g)
    return g*n

_ = input()
l = list(map(int,input().split()))
print(f(l))




