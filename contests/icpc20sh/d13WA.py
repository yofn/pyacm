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
'''

def ff(v1,v2,p1,p2,n):  #t1<t2
    # ASSERT (p1/v1 < p2/v2)
    # SLOW-MODE:     t*v/2 + p/2  (p/v ~ 3*p/v)
    # FAST-MODE:     t*v   - p    (3*p/v +)
    
    # CASE1: DOUBLE-FAST (if n > 3*(p2/v2)*(v1+v2) - p1 - p2) [3t2+]
    if v2*(n+p1+p2) >=  3*p2*(v1+v2):
        return (n+p1+p2)/(v1+v2)

    pvfs = max(p2*v1,3*p1*v2)   # max(t2,3*t1)*(v1*v2)
    # CASE2: FAST-SLOW (1=FAST, 2=SLOW)     [max(t2,3t1), 3t2]
    # if n >=  tfs*v1 - p1 + 1/2* tfs*v2 + p2/2
    # if n >= pvfs/v2 - p1 + 1/2*pvfs/v1 + p2/2
    if v1*v2*(2*n+2*p1-p2) >= pvfs*(2*v1+v2):
        return (2*n+2*p1-p2)/(2*v1+v2)

    # CASE3: SLOW-SLOW [t2, 3t1]
    # if n >= (p2/v2)*(v1+v2)/2 + (p1+p2)/2
    if 3*p1*v2>=p2*v1 and v2*(2*n-p1-p2) >= p2*(v1+v2):
        return (2*n-p1-p2)/(v1+v2)

    # CASE4: FAST-ZERO [3t1, t2]
    # if n >= 3*(p1/v1)*v1 - p1
    if 3*p1*v2< p2*v1 and n>=2*p1:
        return (n+p1)/v1

    # CASE5: SLOW-ZERO [t1, min(3t1,t2)]
    # if n >= (p1/v1)*v1/2 + p1/2 
    if n >= p1:
        return (2*n-p1)/v1
    # THERE is no other CASES!

def f(l):
    n,p1,v1,p2,v2 = l
    # IDEA 1
    if p1>p2:
        p1 = n-p1
    else:
        p2 = n-p2
    # IDEA 2
    if p1*v2 == p2*v1:  #aka. t1==t2
        y0 = (p1+p2)
        y1 = (p1+p2)*2
        if   n<=y0:
            return     (p1+p2)/(v1+v2)  #CASE: DOUBLE-TOUCH
        elif n<=y1:
            return (2*n-p1-p2)/(v1+v2)  #y=x*(v1+v2)/2 + (p1+p2)/2  CASE: DOUBLE-SLOW
        else:
            return   (n+p1+p2)/(v1+v2)  #y=x*(v1+v2)   - (p1+p2)    CASE: DOUBLE-FAST
    elif p1*v2 < p2*v1: #aka. t1<t2
        return ff(v1,v2,p1,p2,n)
    else:
        return ff(v2,v1,p2,p1,n)

# IDEA 0
myint = lambda s: int(0.5 + float(s)*1000)
T  = int(input())
for _ in range(T):
    l = list(map(myint,input().split()))
    print(f(l))

