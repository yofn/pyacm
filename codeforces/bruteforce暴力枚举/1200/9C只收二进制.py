#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/9/C
#failed @ 100
#直接暴力吧!

def f(n):
    m = n
    l = [0,1]
    k = 0
    while True:
        m  = m//10
        if m==0:
            break
        k += 1
        l += [10**k+i for i in l]
    for i in range(len(l)):
        if l[i]>n:
            return i-1
    return i

n = int(input())    #1e9
print(f(n))
