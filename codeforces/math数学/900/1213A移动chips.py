#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1213/A
# 分为奇偶两类,较小的cnt就是答案

def f(l):
    no = sum([a%2==1 for a in l])
    ne = sum([a%2==0 for a in l]) 
    return min(no,ne)

n = input()
l = list(map(int,input().split()))
print(f(l))

