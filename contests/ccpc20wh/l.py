#!/usr/bin/env python3
'''
ccpc20wh
https://codeforces.com/gym/102798/problem/L
buget下的max(最小公倍数)!
prime-power-set
变成一个多重背包问题
1. prime list 预处理
2. prime power set building
3. 01 backpack?  (how to avoid same prime problem?) 
4. 如何表示状态, 状态转移方程?
+ 可以贪心吗? 
'''

import math

def f(b):
    p = [0]*(b+1)
    f = p.copy()
    g = p.copy()
    for i in range(2,b+1):
        if p[i]==0:
            for j in range(2,(1+b//i)):
                p[i*j]=1
    for i in range(2,b+1):  #each group
        if p[i]==1:
            continue
        x = 1
        c = math.log(i)
        r = 0
        while b//x>=i:      #each item in group
            x *= i
            r += c
            for j in range(b,x-1,-1):   #each value
                if f[j-x]+r>g[j]:
                    g[j] = f[j-x]+r
        f = g.copy()
    return g
    
l = f(10000)
T = int(input())        #3e4
for i in range(T):
    b = int(input())    #3e4   nlogn?
    print(l[b])

