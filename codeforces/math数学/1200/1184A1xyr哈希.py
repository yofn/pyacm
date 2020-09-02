#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/1184/A1

def f(n):
    return ['NO'] if (n%2==0 or n<5) else [1,((n-3)//2)]

n = int(input())
print(*f(n))
