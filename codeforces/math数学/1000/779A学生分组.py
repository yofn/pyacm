#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/779/A

def f(a,b):
    n = 6       #1-5
    d = [0]*n
    for i in range(len(a)):
        d[a[i]] += 1
        d[b[i]] -= 1
    if sum([d[i]%2>0 for i in range(n)]) > 0:
        return -1   #d[i] must be all even
    return sum([d[i]>>1 for i in range(n) if d[i]>0])

_ = input() #100
a = list(map(int,input().split()))
b = list(map(int,input().split()))
print(f(a,b))
