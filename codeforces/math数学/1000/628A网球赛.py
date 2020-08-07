#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/628/A
# 之前想复杂了,每场比赛淘汰一位,所以场次=n-1

def f(l):
    n,b,p = l   #500
    return [(n-1)*(b+b+1),n*p]

l = list(map(int,input().split()))
print(*f(l))
