#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1073/B

def f(a,b):
    n  = len(a)
    al = [(a[i],i+1) for i in range(n)]
    al.sort(key=lambda a:a[0])  #a[0]=number of books
    p  = 0
    for i in range(n):
        t   = al[b[i]-1][1]
        if t>p:
            b[i]=t-p
            p   =t
        else:
            b[i]=0
    return b

n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
print(*f(a,b))
