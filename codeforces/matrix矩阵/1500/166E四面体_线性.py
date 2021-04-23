#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/166/E
#是一个对角为0的矩阵的快速幂,用线性的递推更快!?还是用log的矩阵快速幂更快?
#矩阵可以从4x4[0 1 1 1;1 0 1 1;..]简化到2x2[0 3;1 2]

def linear_solution(n):
    dd,do = 1,0 
    for i in range(n):
        t  = do*3
        do = (do<<1)+dd
        dd = t
    return dd

matrix_mult = lambda A,B:(A[0]*B[0]+A[1]*B[2], A[0]*B[1]+A[1]*B[3], A[2]*B[0]+A[3]*B[2], A[2]*B[1]+A[3]*B[3])
def fast_matrix_power(m,n):
    if   n==1:
        return m
    elif n%2==0:
        t = fast_matrix_power(m,n//2) 
        return matrix_mult(t,t)
    else:
        t = fast_matrix_power(m,n//2) 
        return matrix_mult(matrix_mult(t,t),m)

def f(n):
    #return linear_solution(n)   #WILL TLE!
    return fast_matrix_power((0,3,1,2),n)[0]

n = int(input())
print(f(n)%(int(1e9+7)))

