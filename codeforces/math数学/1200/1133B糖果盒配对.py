#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/1133/B

def f(l1,l2):
    n,k = l1
    cl  = [0]*k
    for i in l2:
        cl[i%k] += 1
    p   = cl[0]//2
    p  += sum([min(cl[i],cl[k-i]) for i in range(1,k) if i<k-i])
    p  += 0 if k%2>0 else cl[k//2]//2
    return p<<1

l1 = list(map(int,input().split()))
l2 = list(map(int,input().split()))
print(f(l1,l2))
