#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/476/A
# n个台阶,1或2; m乘除(最小)
# 10,2 => 6

def f(l):
    n,m = l
    ms  = (n+1)//2
    ds  = ((ms+m-1)//m)*m
    return -1 if ds>n else ds

l = list(map(int,input().split()))
print(f(l))
