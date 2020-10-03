#!/usr/bin/env python3

#https://codeforces.com/group/H9K9zY8tcT/contest/297258/problem/K


c2i = lambda c: ord(c)-ord('a')
i2c = lambda i: chr(ord('a')+i)
sub = lambda a,b: (a-b)%26

def f(l1,l2):
    n  = len(l1)
    m  = len(l2)
    t  = [None]*(m-n) + list(map(c2i,l1))   #full unencrypted text! (m-n) + n
    c  = list(map(c2i,l2))                  #full encrypted text    m
    for i in range(m-1,n-1,-1):
        t[i-n] = sub(c[i],t[i])
    return ''.join(list(map(i2c,t)))

_  = input()
l1 = list(input())
l2 = list(input())
print(f(l1,l2))
