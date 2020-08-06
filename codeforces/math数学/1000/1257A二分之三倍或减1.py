#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1247/A
# 关键是1,2,3这三个数
# 因为4的范围=6的范围=9的范围=8的范围=12的范围=18的范围=....

def f(l):
    x,y = l
    if x>3:
        return True
    return y<4 if x>1 else y<2

t = int(input())
for _ in range(t):
    l = list(map(int,input().split()))
    print('YES' if f(l) else 'NO')
