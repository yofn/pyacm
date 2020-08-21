#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1366/A

def f(l):
    a,b = l
    return min(a,b,(a+b)//3) 

q = int(input())
[print(f(list(map(int,input().split())))) for _ in range(q)]
