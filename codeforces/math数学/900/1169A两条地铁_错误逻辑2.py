#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1169/A
# (n+1)余数和保持不变,然后求相等点,再检查相等点是否在两者之间

def f(l):
    n,a,x,b,y = l
    if (a+b)%2!=0:
        return False
    m = (a+b)//2
    return (m>=a or m<=x) and (m<=b or m>=y)

l   = list(map(int,input().split()))
print('YES' if f(l) else 'NO')

