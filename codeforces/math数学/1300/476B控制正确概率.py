#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/476/B
#概率题. Binomial分布?

from math import factorial as f

s1 = input()    #length<10
s2 = input()

cp = s1.count('+')-s1.count('-')
wp = s2.count('+')-s2.count('-') 
qc = s2.count('?')
dp = max(cp-wp,wp-cp)  #absolute pos diff
if dp>qc or dp%2!=qc%2:
    print(0)
else:
    k1 = (qc+dp)//2
    k2 = (qc-dp)//2
    print(f(qc)/f(k1)/f(k2)/(1<<qc))
