#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/222/E

q   = int(1e9)+7
def binpower(A,e):
    r   = range(len(A))
    C   = [[1 if i==j else 0 for j in r] for i in r]
    while True:
        if e &1:
            C = [[sum([A[i][k]*C[k][j] for k in r])%q for j in r] for i in r]
        e = e>>1
        if e==0: return C
        A     = [[sum([A[i][k]*A[k][j] for k in r])%q for j in r] for i in r]

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

