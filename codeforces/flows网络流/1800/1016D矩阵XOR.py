#!/usr/bin/env python3


def f(a,b):
    n = len(a)
    m = len(b)
    r = 0
    for i in a+b:
        r = r^i
    if r>0:
        return [['NO']]
    mt = [[0]*m for _ in range(n)]
    for i in range(min(m,n)-1):
        mt[i][i+1]=a[i]
        mt[i+1][i]=b[i]
        b[i+1] ^= a[i]
        a[i+1] ^= b[i]
    for j in range(n-1,m):
        mt[n-1][j] = b[j]
    for i in range(m-1,n):
        mt[i][m-1] = a[i]
    print('YES')
    return mt

_ = input()
a = list(map(int,input().split()))
b = list(map(int,input().split()))
[print(*s) for s in f(a,b)]
