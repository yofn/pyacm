#!/usr/bin/env python3
'''
    print('Case #%d: %s'%((i+1), f(a,b)))
'''

def f(a,b):
    n  = len(a)
    for i in range(n):
        if b[i]>a[i]*3:
            return i+1
    return -1

t = int(input())
for i in range(t):
    _   = input()
    a   =  list(map(int,input().split()))
    b   =  list(map(int,input().split()))
    print(f(a,b))

