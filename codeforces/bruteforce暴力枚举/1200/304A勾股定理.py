#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/304/A
#a,b,c #1e4 满足勾股定理
#c>b>a
#这是数学,不是暴力?
#错误逻辑, 不一定是k,k*i*i, 也可以是k*k, i*i
#https://en.wikipedia.org/wiki/Pythagorean_triple#Generating_a_triple
#好像实现的比较ugly
#要么用wiki方法,要么暴力!

import math

def f(n):
    c = 0
    for i in range(2,n):
        for j in range(i,n):
            s = i*i+j*j
            r = int(math.sqrt(s))
            if r*r == s and r<=n:
                c+=1
    return c

n = int(input())  #1e4
print(f(n))
