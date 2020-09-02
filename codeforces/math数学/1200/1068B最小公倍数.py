#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/1068/B
#lcm(a,b)/a = b/gcd(a,b)
#有多少种可能=>gcd(a,b)有多少种可能,也就是b有多少种因子
#对b先做质因子分解?
#gcd = lambda a,b: a if b==0 else gcd(b,a%b) #a>=b

import math

b = int(input())        #1e10
s = int(math.sqrt(b))   #1-s ..
c = 0 if b%s>0 else (1 if b//s==s else 2)
for i in range(1,s):
    if b%i==0:
        c += 2
print(c)
