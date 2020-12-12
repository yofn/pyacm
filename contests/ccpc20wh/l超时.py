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
    ll = []
    pl = primes(b) 
    for i in pl:
        j  = 1
        l  = []   
        li = math.log(i)
        while i**j < b:
            l.append((i**j,j*li))
            j = j+1
        ll.append(l)
    return ll

def f(b):
    ns  = [0]*(b+1)
    ppl = primePower(b)
    n   = len(ppl)
    for k in range(n-1,-1,-1):
        pl = ppl[k]
        for i in range(b,pl[0][0]-1,-1):#for each budget
            for p in pl:    #for each prime-power
                if p[0]>i:
                    break
                t = ns[i-p[0]]+p[1]
                if t>ns[i]:
                    ns[i] = t
    return ns   #[math.log(i) for i in ns]
    
l = f(30000)
T = int(input())        #3e4
for i in range(T):
    b = int(input())    #3e4   nlogn?
    print(l[b])

