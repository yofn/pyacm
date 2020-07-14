#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/1307/B
#欧式距离.
#三角形.多边形?

t   = int(input())
for i in range(t):
    n,x = list(map(int,input().split())) 
    al  = list(map(int,input().split()))
    al.sort(reverse=True)
    s   = 0
    for i in range(n):
        s += al[i]
        if s>=x:
            i += 2 if (i==0 and s>x) else 1
            break
    print(i)
