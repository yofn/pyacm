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

超时怎么办?
+ 先做一个01背包，再做一个分组背包?
'''

import math

def primes(b):
    #3245 primes for b=3e4!
    l = [2]
    i =  2
    while(i<=b):
        i      += 1
        isPrime = True
        for j in range(2,1+math.floor(math.sqrt(i))):
            if i%j==0:
                isPrime = False
                break
        if isPrime:
            l.append(i)
    return l

def primePower(b):
    #3320 prime power for b=3e4!
    l1 = []
    l2 = []
    pl = primes(b) 
    group = True
    for i in pl:
        li = math.log(i)
        l  = [(i,li)]
        j  = 2
        while group and i**j < b:
            l.append((i**j,j*li))
            j = j+1
        if j==2:
            group = False
        if group:
            l1.append(l)
        else:
            l2.append((i,li))
    return {'single':l2,'multiple':l1}

def f(b):
    ns      = [0]*(b+1)
    ppl     = primePower(b) #l2 for 01 backpack, l1 for multiple backpack!
    n       = len(ppl)

    print('single',len(ppl['single']))
    rg      = range(b,-1,-1)
    for t in ppl['single']:
        for i in rg:
            if i<t[0]:
                break
            #ns[i] = max(ns[i],ns[i-t[0]]+t[1])
            x  = ns[i-t[0]]+t[1]
            if x>ns[i]:
                ns[i] = x
    return ns

    print('single',len(ppl['single']))
    for t in ppl['single']:
        i = b
        while i>=t[0]:
            x  = ns[i-t[0]]+t[1]
            if x>ns[i]:
                ns[i] = x
            i -= 1

    return ns
    print('multiple',len(ppl['multiple']))
    for pl in ppl['multiple']:
        for i in range(b,pl[0][0]-1,-1):#for each budget
            for p in pl:    #for each prime-power
                if p[0]>i:
                    break
                x  = ns[i-t[0]]+t[1]
                if x>ns[i]:
                    ns[i] = x
    return ns   #[math.log(i) for i in ns]
    
l = f(30000)
T = int(input())        #3e4
for i in range(T):
    b = int(input())    #3e4   nlogn?
    print(l[b])

