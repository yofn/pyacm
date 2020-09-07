#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/304/A
#a,b,c #1e4 满足勾股定理
#c>b>a
#这是数学,不是暴力?
#错误逻辑, 不一定是k,k*i*i, 也可以是k*k, i*i
#https://en.wikipedia.org/wiki/Pythagorean_triple#Generating_a_triple
#好像实现的比较ugly

def f(n):
    l = []
    for k in range(1,n):
        rr = range(n+n+1) if k%2==0 else range(1,n+n+1,2)
        for i in rr:
            a = i*k
            c = ((i*i+1)*k)//2
            b = c-k
            if c>n:
                break
            if b>=a:
                l.append([a,b,c])
    for i in range(2,n):
        for j in range(i+2,n,2):
            a = i*j
            c = (j*j+i*i)//2
            b = (j*j-i*i)//2
            if c>n:
                break
            if b>=a:
                l.append([a,b,c])
    l.sort(key=lambda x:x[2])
    [print(*r) for r in l]
    return len(l)

n = int(input())  #1e4
print(f(n))
