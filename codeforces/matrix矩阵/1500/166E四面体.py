#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/166/E
#是一个对角为0的矩阵的快速幂,用线性的递推更快!?还是用log的矩阵快速幂更快?
#矩阵可以从4x4[0 1 1 1;1 0 1 1;..]简化到2x2[0 3;1 2]
#大数值的乘法和加法依然比较慢..

m2 = lambda A,B:(A[0]*B[0]+A[1]*B[2], A[0]*B[1]+A[1]*B[3], A[2]*B[0]+A[3]*B[2], A[2]*B[1]+A[3]*B[3])
def fast_matrix_power(n):
    m = (0,3,1,2)
    if   n==1:
        return m
    t = fast_matrix_power(n//2) 
    p = int(1e9+7)
    t = t[0]%p,t[1]%p,t[2]%p,t[3]%p #IMPORTANT
    r = m2(t,t)
    return r if n%2==0 else m2(r,m)

def f(n):
    return fast_matrix_power(n)[0]

n = int(input())
print(f(n)%(int(1e9+7)))

