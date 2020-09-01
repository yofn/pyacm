#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/675/A
# 注意c可以是0或负数!

def f(l):
    a,b,c = l
    if c==0:
        return a==b
    return (b-a)%c==0 and (b-a)//c>=0

l = list(map(int,input().split()))
print('YES' if f(l) else 'NO')
