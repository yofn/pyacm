#!/usr/bin/python3
'''
不止三个区域,
+ t1-3t1-t2-3t2
+ t1-t2-3t1-3t2
+ x0=t1, tt=t2
转成整数!
逆向思维(less travelled by):
+ 浮点到整数!
+ n-p2
+ t?
+ 扫雷!
分类讨论 + 高精度!?
假设一开始就错了.... 小的一定走左边,大的一定走右边? 一开始就错了!
    print(single(p1,v1,n),single(p2,v2,n),cross(l),two(l))
#slow = t*v/2 + p/2
#fast = t*v   - p
    # CASE1: DOUBLE-FAST    [y2=2*p2, t=
    # CASE2: FAST-SLOW 
    # CASE3: SLOW-SLOW
'''

def ff(v1,v2,p1,p2,n):  #t1<t2
    if (n+p1+p2)*v2 >= 3*p2*(v1+v2):
        return (n+p1+p2)/(v1+v2)
    pvfs = max(p2*v1,3*p1*v2)   #pvfs = v1*v2*max(t2,3t1)
    if (2*n+2*p1-p2)*v1*v2 >= pvfs*(2*v1+v2):
        return (2*n+2*p1-p2)/(2*v1+v2)
    if (p2*v1<3*p1*v2) and v2*(2*n-p1-p2) >= p2*(v1+v2):
        return (2*n-p1-p2)/(v1+v2)
    return p2/v2 #other cases covered by single or cross

def cross(l):
    n,p1,v1,p2,v2 = l
    if p1==p2: return min(max(p1/v1,(n-p2)/v2),max((n-p1)/v1,p2/v2))
    return  max(p2/v2,(n-p1)/v1) if p2>p1 else max(p1/v1,(n-p2)/v2)

def f(l):
    n,p1,v1,p2,v2 = l
    single = lambda p,v,n: min(p+n,n-p+n)/v
    return min(single(p1,v1,n),single(p2,v2,n),cross(l),two(l))

def two(l):
    n,p1,v1,p2,v2 = l
    if p1>p2:
        p1 = n-p1
    else:
        p2 = n-p2
    return ff(v1,v2,p1,p2,n) if p1*v2<p2*v1 else ff(v2,v1,p2,p1,n)

myint = lambda s: int(0.5 + float(s)*1000)
T  = int(input())
for _ in range(T):
    l = list(map(myint,input().split()))
    print(f(l))

