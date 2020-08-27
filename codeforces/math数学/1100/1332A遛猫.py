#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1332/A

def f(l1,l2):
    a,b,c,d         = l1
    x,y,x1,y1,x2,y2 = l2
    if x1==x2 and (a>0 or b>0):
        return False
    if y1==y2 and (c>0 or d>0):
        return False
    x += b-a
    y += d-c
    return x>=x1 and x<=x2 and y>=y1 and y<=y2

q = int(input())
for _ in range(q):
    l1 = list(map(int,input().split()))
    l2 = list(map(int,input().split()))
    print('Yes' if f(l1,l2) else 'No')
