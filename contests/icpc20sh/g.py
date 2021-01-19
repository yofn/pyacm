#!/usr/bin/python3

def f(n):
    e = n//3
    o = n-e
    return n*(n-1)//2 - o*(o-1)//2 

n  = int(input())
print(f(n))
