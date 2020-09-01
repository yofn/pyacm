#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/682/A

def f(l):
    n,m = l
    c1  = [(n+5-i)//5 for i in range(5)]
    c2  = [(m+5-i)//5 for i in range(5)]
    return (c1[0]-1)*(c2[0]-1)+sum([c1[i]*c2[5-i] for i in range(1,5)])

l = list(map(int,input().split()))
print(f(l))
