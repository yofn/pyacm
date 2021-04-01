#!/usr/bin/python3
#https://codeforces.com/contest/1426/problem/D

def f(l):
    n   = len(l)    #2e5
    pre = [None]*n
    pre[0] = (0,l[0])
    for i in range(1,n):
        pre[i] = (i,pre[i-1][1]+l[i])
    pre.sort(key=lambda t:t[1])
    return pre

_ = input()
l = list(map(int,input().split()))
print(f(l))
