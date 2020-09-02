#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/630/B
#直接乘有点太多?
#24个月double => 24*30*24*60*60= 
#想多了,编程语言的power已经足够优化? 快速幂?
#https://codeforces.com/blog/entry/24160?locale=en

def f(l):
    n,t = l #1e3-1e4; 2e9;
    return n*(1.000000011**t) 

l = list(map(int,input().split()))
print(f(l))
