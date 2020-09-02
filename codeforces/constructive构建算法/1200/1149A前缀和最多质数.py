#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/1149/A
#构建(n1,n2)
#n1>0,n2>0: (2,1)(..+2..),..(..+1..)    直觉
#n2=0:      (..+1..)
#n1=0:      (..+2..)

def f(l):
    c1 = sum([i==1 for i in l])
    c2 = len(l)-c1
    if c1>0 and c2>0:
        return [2,1] + [2]*(c2-1) + [1]*(c1-1)
    return [2]*c2 + [1]*c1

n = int(input())
l = list(map(int,input().split()))
print(*f(l))
