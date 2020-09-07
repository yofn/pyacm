#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/344/B

def f(l):
    a,b,c = l
    if sum(l)%2>0:
        return ['Impossible']
    ab = (a+b-c)//2
    ac = (a+c-b)//2
    bc = (b+c-a)//2
    l  = [ab,bc,ac]
    if sum([i==0 for i in l])>1 or sum([i<0 for i in l])>0:
        return ['Impossible']
    return l

l = list(map(int,input().split()))
print(*f(l))
