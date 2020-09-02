#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/456/B

def f(n):
    r2 = [1,2,4,3]
    r3 = [1,3,4,2]
    r4 = [1,4]
    return (1+r2[n%4]+r3[n%4]+r4[n%2])%5

n = int(input()[-2:])   #multipler of 4
print(f(n))
