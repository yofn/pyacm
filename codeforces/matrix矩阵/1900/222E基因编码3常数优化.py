#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/222/E

q   = int(1e9)+7
def binpower(A1,e):
    n   = len(A1)
    r   = range(n)
    A2  = [[0]*n for _ in r]
    C1  = [[0]*n for _ in r]
    C2  = [[0]*n for _ in r]
    for i in r: C1[i][i]=1
    sA1,sC1 = True,True
    while True:
        C = C1 if sC1 else C2
        A = A1 if sA1 else A2
        if e &1:
            T = C2 if sC1 else C1
            for i in r:
                for j in r:
                    T[i][j] = sum([A[i][k]*C[k][j] for k in r])%q
            sC1 = not sC1
        e = e>>1
        if e==0: return T
        S = A2 if sA1 else A1
        for i in r:
            for j in r:
                S[i][j] = sum([A[i][k]*A[k][j] for k in r])%q 
        sA1 = not sA1

c2i = lambda c: ord(c)-ord('a') if c.islower() else ord(c)-ord('A')+26
def f(l1,l2):
    n,m,_ = l1
    if n==1: return m
    M  = [[1]*m for _ in range(m)]
    for s in l2:
        i = c2i(s[0])
        j = c2i(s[1])
        M[i][j]=0
    return sum([sum(l) for l in binpower(M,n-1)])

l1  =  list(map(int,input().split()))
l2  = [input() for _ in range(l1[2])]
print(f(l1,l2)%q)

