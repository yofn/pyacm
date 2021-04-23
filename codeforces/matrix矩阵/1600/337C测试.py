#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/337/C
#放置策略: 让后面的都是+1,即从后向前,每K个放置一个错误答案(假设有w个错误)
#所以所有错误答案放置完毕后,前面的都是对的,而总分=F(n-wk)+w(k-1),其中F(x)是连续x个正确的得分!
#F(x)的计算: 以k为单位: 2k=>6k=>14k=>30k=>..
#G(n)=2G(n-1)+2 => G(n)=2^(n+1)-2

p   = int(1e9+9)

def f2(l):
    n,m,k   = l
    w       = n-m
    cc      = n-w*k
    if cc < k:
        return m
    nkp1    = cc//k   + 1
    f       = w*(k-1) + (cc%k) - (k<<1)
    return f + (k<<nkp1)%p

def f(l):
    n,m,k   = l
    w       = n-m
    cc      = n-w*k
    if cc < k:
        return m
    g       = ((2<<(cc//k))-2)%p
    fcc     = k*g+(cc%k)
    return fcc + w*(k-1)

l = list(map(int,input().split()))
print(f2(l)%p)

