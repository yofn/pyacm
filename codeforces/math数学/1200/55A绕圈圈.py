#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/55/A
#需要推导一下

def f(n):
    rl = [True]*n   #True = nonvisited
    nn = (n*(n-1))//2
    for k in range(n):
        kk = (k*(k+1))//2
        rl[kk%n] = False
        if n%2==0:
            rl[(kk+nn)%n] = False
    return sum(rl)==0

n = int(input())
print('YES' if f(n) else 'NO')
