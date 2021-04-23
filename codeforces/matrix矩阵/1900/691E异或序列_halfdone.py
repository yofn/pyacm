#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/691/E
#没写完整,怕超时..

mul=lambda A,B,r:[[max([A[i][k]+B[k][j] for k in r if A[i][k] and B[k][j]],default=0) for j in r] for i in r]

def binpower(A,n,e):
    r  = range(n)
    B  = A  #A^0 is invalid, thus start from A^1
    e -= 1
    while True:
        if e &1: B = mul(B,A,r)
        e =e>>1
        if e==0: return B
        A =mul(A,A,r)

def f(l,n,k):
    M = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(i+1,n):
            c = bin(l[i]^l[j]).count('1')
            if c>0 and c%3==0:
                M[i][j]=1
                M[j][i]=1
    return max(max(binpower(M,n,k)))

n,k = list(map(int,input().split()))
l   = list(map(int,input().split()))
print(f(l,n,k))

