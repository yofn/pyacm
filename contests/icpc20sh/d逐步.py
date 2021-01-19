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
    
    t  = max(t1,t2)
    h1 = p1 + p2 + ((t2-t1)*v1/2 if t2>t1 else (t1-t2)*v2/2)
    #print('h1',h1)
    if h1>=n:
        #print('maxt1t2')
        return t

    s1 = (v1+v2)/2
    t  = max(t1,t2) + (n-h1)/s1
    t3 = min(t1,t2)*3
    if t<=t3:
        #print('region1')
        return t
    h2 = h1 + s1*(t3-max(t1,t2))
    #print('h2,s1',h2,s1)

    s2 = (v1+v2/2) if t1<t2 else (v1/2+v2)
    t  = t3 + (n-h2)/s2
    t4 = max(t1,t2)*3
    if t<=t4:
        #print('region2')
        return t
    h3 = h2 + s2*(t4-t3)
    #print('h3,s2',h3,s2)

    s3 = (v1+v2)
    t  = t4 + (n-h3)/s3
    #print('region3')
    #print('s3',s3)
    return t

T  = int(input())
for _ in range(T):
    l = list(map(float,input().split()))
    print(f(l))

