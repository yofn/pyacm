#!/usr/bin/env python3

def f(s,x):
    n = len(s)
    i,j= 0,n-1
    w = [None]*n
    while i<=j:
        if s[i]==1:
            if i<x or w[i-x]==0:
                if w[i+x]==0: return -1
                w[i+x]=1
        else:
            if i<x or w[i-x]==0:
                if w[i+x]==1: return -1
                w[i+x]=0
            elif w[i-x]==1:
                return -1
        if s[j]==1:
            if j+x>=n or w[j+x]==0:
                if w[j-x]==0: return -1
                w[j-x]=1
        else:
            if j+x>=n or w[j+x]==0:
                if w[j-x]==1: return -1
                w[j-x]=0
            elif w[j+x]==1:
                return -1
        i,j  = i+1,j-1
    return ''.join(w)

for i in range(int(input())):
    s = input().split()
    x = int(input())
    print(f(s,x))

