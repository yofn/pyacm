#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/1282/B2
#B2=1600难度
#注意是exactly k,而不是<=k
#test2又报错,肯定还是有考虑不周的地方,决定重构一下,以堵住漏洞

def bestbuy(al,n,p,k):
    if al[0]>p:
        return 0
    cl      = [1]*n
    cl[k-1] = k
    for i in range(1,k-1): #al[k-1] is kept!
        al[i] += al[i-1]
        cl[i]  = i+1
        if al[i] >= al[k-1]:
            al[i] = al[k-1]
            cl[i] = k
        if al[i] > p:
            return cl[i-1]
    if al[k-1]>p:
        return k-1
    for i in range(k,n):
        al[i] += al[i-k]
        cl[i]  = cl[i-k]+k
        if al[i]>p:
            return cl[i-1]
    return n

t   = int(input())  #1e4
for _ in range(t):
    n,p,k   = list(map(int,input().split()))    #2e5,2e9,k=[2,n]
    al      = list(map(int,input().split()))    #1e4
    al.sort()
    print(bestbuy(al,n,p,k))
