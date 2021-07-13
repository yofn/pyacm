#!/usr/bin/python3

def f(n):
    l1 = [0]*(n+1)
    l2 = [0]*(n+1)
    l3 = [0]*(n+1)
    for i in range(1,n):
        for j in range(1,n):
            for k in range(1,n):
                if i+j+k<=n:
                    l1[i+j+k]+=1
                    l2[i+j]  +=1
                    l3[i]    +=1
    print(n)
    print(l1)
    print(l2)
    print(l3)
    return None

[f(i) for i in range(3,10)]
