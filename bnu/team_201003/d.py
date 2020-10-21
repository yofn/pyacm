#!/usr/bin/env python3

#https://codeforces.com/group/H9K9zY8tcT/contest/297617

def f(l):
    a,b = l
    c = 0
    while a>b:
        c += 1 + (a%2)
        a  = (a+1)//2
    c += (b-a)
    return c

l = list(map(int,input().split()))
print(f(l))
