#!/usr/bin/python3

def fp(l):
    k,n =l
    p1  = 1-pow((k-1)/k,n)
    p2  = n+1-2*k+(n+2*k-1)*pow((k-1)/k,n)
    kn  = pow(k,n)
    return p1*kn,p2*kn

def f(l):
    k,n=l
    n1 = pow(k,n)-pow(k-1,n)
    n2 = ..

l = list(map(int,input().split()))
print(f(l))
