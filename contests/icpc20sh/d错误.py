#!/usr/bin/python3

def f(l):
    n,p1,v1,p2,v2 = l
    # change coordinate!
    if p1>p2:
        p1 = n-p1
    else:
        p2 = n-p2
    t1 = p1/v1
    t2 = p2/v2
    
    x0  = max(t1,t2)
    y0  = p1 + p2 + ((t2-t1)*v1/2 if t2>t1 else (t1-t2)*v2/2)
    if n<=y0:
        return x0

    #region1:   [max(t1,t2) ~ min(t1,t2)*3]
    k   = (v1+v2)/2
    x1  = min(t1,t2)*3
    y1  = y0 + (x1-x0)*k
    if n<=y1:
        return x0 + (n-y0)/k

    #region2:   [min(t1,t2)*3 ~ max(t1,t2)*3]
    k   = (v1+v2/2) if t1<t2 else (v1/2+v2)
    x2  = max(t1,t2)*3
    y2  = y1 + (x2-x1)*k
    if n<=y2:
        return x1 + (n-y1)/k

    #region3:   [max(t1,t2)*3 ~ ]
    k   = (v1+v2)
    return x2 + (n-y2)/k

T  = int(input())
for _ in range(T):
    l = list(map(float,input().split()))
    print(f(l))

