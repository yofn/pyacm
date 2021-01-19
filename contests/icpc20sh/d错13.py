#!/usr/bin/python3
'''
不止三个区域,
+ t1-3t1-t2-3t2
+ t1-t2-3t1-3t2
+ x0=t1, tt=t2
'''

def f(l):
    n,p1,v1,p2,v2 = l
    # change coordinate!
    if p1>p2:
        p1 = n-p1
    else:
        p2 = n-p2
    t1  = p1/v1
    t2  = p2/v2
    q1  = (t1<=t2)
    tt  = max(t1,t2)

    #region0: [0-x0]
    x0  = t1 if q1 else t2
    y0  = p1 if q1 else p2
    if n<=y0:
        return x0

    qv  = v1 if q1 else v2
    sv  = v2 if q1 else v1
    tv  = v1+v2

    #region1: [x0-x1]
    k1  = qv/2
    x1  = min(x0*3,tt)
    y1  = y0 + k1*(x1-x0)
    if n<=y1:
        return x0 + (n-y0)/k1
    y1  = y1 if x1!=tt else p1+p2+k1*(x1-x0)    #might JUMP!

    #region2: [x1-x2]
    k2  = tv/2 if x1==tt else qv
    x2  = max(x0*3,tt)
    y2  = y1 + k2*(x2-x1)
    if n<=y2:
        return x1 + (n-y1)/k2
    y2  = y2 if x2!=tt else p1+p2+k1*(x1-x0)+k2*(x2-x1)
    
    #region3:  [x2-x3]
    k3  = qv + sv/2
    x3  = tt*3
    y3  = y2 + k3*(x3-x2)
    if n<=y3:
        return x2 + (n-y2)/k3
    else:
        return x3 + (n-y3)/tv  #region4
        #return (n+p1+p2)/tv

T  = int(input())
for _ in range(T):
    l = list(map(float,input().split()))
    print(f(l))

