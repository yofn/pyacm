#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/1285/B
#区间求和,用前缀和

def okay(al,n):
    acl = [0]*(n+1)
    for i in range(n):
        acl[i+1] = acl[i] + al[i]
    y        = acl[-1]
    acl[0]   = 1
    acl[-1] -= 1
    b   = max(acl)-min(acl)
    return y>(b+1) #if[0,n],b=y-2

t = int(input())        #1e4
for _ in range(t):
    n   = int(input())  #1e5
    al  = [int(s) for s in input().split()]
    print('YES' if okay(al,n) else 'NO')

