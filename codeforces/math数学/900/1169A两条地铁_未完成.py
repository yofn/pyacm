#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1169/A
# (n+1)余数和保持不变,然后求相等点,再检查相等点是否在两者之间
# (a+b)不够,可能是出现(a+b+n)或(a+b-n)的情况
# 逻辑一大堆,好像还没有暴力法方便?
# 重新整理逻辑..之前修修补补太多次了.. 
# 先算ta和tb; 或者直接算list(暴力法)
# 再试试之前的余数法..

def f(l):
    n,a,x,b,y = l
    ta  = (x-a)%n
    tb  = (b-y)%n 
    t   = min(ta,tb)
    return d<=(t<<1)

l   = list(map(int,input().split()))
print('YES' if f(l) else 'NO')

