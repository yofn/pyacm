#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1169/A
# 站点和总是(n+1), 所以相遇首先n是奇数,其次(n+1)/2在[a,x][b,y]之间

def f(l):
    n,a,x,b,y = l
    if n%2==0:
        return False
    m = (n+1)//2
    return (m>=a or m<=x) and (m<=b or m>=y)

l   = list(map(int,input().split()))
print('YES' if f(l) else 'NO')

