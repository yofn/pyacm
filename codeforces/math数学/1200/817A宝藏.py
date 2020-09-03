#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/817/A

def f(l1,l2):
    x1,y1,x2,y2 = l1
    x,y         = l2
    if (x2-x1)%x>0 or (y2-y1)%y>0:
        return False
    sx = (x2-x1)//x
    sy = (y2-y1)//y
    return (sx-sy)%2==0

l1 = list(map(int,input().split()))
l2 = list(map(int,input().split()))
print('YES' if f(l1,l2) else 'NO')
