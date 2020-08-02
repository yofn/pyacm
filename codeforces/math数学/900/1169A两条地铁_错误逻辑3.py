#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1169/A
# (n+1)余数和保持不变,然后求相等点,再检查相等点是否在两者之间
# (a+b)不够,可能是出现(a+b+n)或(a+b-n)的情况
# 逻辑一大堆,好像还没有暴力法方便?

def f(l):
    n,a,x,b,y = l
    r   = (a+b)%(n+1)
    ml  = [s//2 for s in [r-n, r, r+n] if s>0 and s%2==0]
    ta  = [m-a if m>=a else m+n-a for m in ml]
    tb  = [b-m if m<=b else b+n-m for m in ml]
    tma = x-a if x>=a else x+n-a
    tmb = b-y if y<=b else b+n-y
    mt  = [(ta[i]==tb[i] and ta[i]<=tma and tb[i]<=tmb) for i in range(len(ml))]
    return sum(mt)

l   = list(map(int,input().split()))
print('YES' if f(l) else 'NO')

