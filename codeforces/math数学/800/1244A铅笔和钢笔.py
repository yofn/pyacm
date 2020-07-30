#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1244/A

t = int(input())
for _ in range(t):
    a,b,c,d,k   = list(map(int,input().split()))
    pen = (a+c-1)//c
    pcl = (b+d-1)//d
    r   = [pen,pcl] if pen+pcl<=k else [-1]
    print(*r)
