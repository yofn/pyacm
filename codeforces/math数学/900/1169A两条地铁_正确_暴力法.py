#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1169/A
# (n+1)余数和保持不变,然后求相等点,再检查相等点是否在两者之间
# (a+b)不够,可能是出现(a+b+n)或(a+b-n)的情况
# 逻辑一大堆,好像还没有暴力法方便?
# 重新整理逻辑..之前修修补补太多次了.. 
# 先算ta和tb; 或者直接算list(暴力法)

def f(l):
    n,a,x,b,y = l
    al  = list(range(a,x+1,+1)) if x>=a else list(range(a,n+1,+1))+list(range(1,x+1,+1))
    bl  = list(range(b,y-1,-1)) if y<=b else list(range(b,  0,-1))+list(range(n,y-1,-1))
    t   = min(len(al),len(bl))
    return sum([al[i]==bl[i] for i in range(t)])

l   = list(map(int,input().split()))
print('YES' if f(l) else 'NO')

