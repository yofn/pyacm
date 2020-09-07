#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/304/A
#a,b,c #1e4 满足勾股定理
#c>b>a
#这是数学,不是暴力?
#错误逻辑, 不一定是k,k*i*i, 也可以是k*k, i*i

def f(n):
    l = []
    for k in range(1,n):
        rr = range(n+n+1) if k%2==0 else range(1,n+n+1,2)
        for i in rr:
            c = ((i*i+1)*k)//2
            if c>n:
                break
            if (c-k)>=(i*k):
                l.append([k,i,i*k,c-k,c])
    l.sort(key=lambda x:x[4])
    [print(*r) for r in l]
    return len(l)

n = int(input())  #1e4
print(f(n))
