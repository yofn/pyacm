#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1110/A
# b=basis

def f(a,b):
    if b%2==0:
        return a[-1]%2==0
    nodd = sum([x%2>0 for x in a])
    return nodd%2==0

b,_ = list(map(int,input().split())) 
a   = list(map(int,input().split()))
print('even' if f(a,b) else 'odd')
