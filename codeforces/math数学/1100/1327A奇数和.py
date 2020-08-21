#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1327/A

def f(l):
    n,k = l
    return n>=k*k and n%2==k%2 

q = int(input())
[print('YES' if f(list(map(int,input().split()))) else 'NO') for _ in range(q)]
