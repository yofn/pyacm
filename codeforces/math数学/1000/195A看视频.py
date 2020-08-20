#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/195/A

def f(l):
    a,b,c =l
    return (c*(a-b)+b-1)//b

l = list(map(int,input().split()))
print(f(l))
