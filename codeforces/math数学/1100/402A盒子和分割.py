#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/402/A

def f(l):
    k,a,b,v = l
    ns = (a+v-1)//v
    return max(ns-b,(ns+k-1)//k) 

l = list(map(int,input().split()))
print(f(l))
