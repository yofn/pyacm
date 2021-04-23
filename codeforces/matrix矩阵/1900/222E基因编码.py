#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/222/E

q   = int(1e9)+7
mul=lambda A,B,r:[[sum([(A[i][k]*B[k][j])%q for k in r]) for j in r] for i in r]

def binpower(A,e):
    r  = range(len(A))
    B  = A
    e -= 1
    while True:
        if e &1: B = mul(B,A,r)
        e =e>>1
        if e==0: break
        A =mul(A,A,r)
    return B

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

