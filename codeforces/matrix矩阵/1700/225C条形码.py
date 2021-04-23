#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/225/C

inf = 9999999999

def f(ll,n,m,x,y):
    W   = [0]*m #White
    for i in range(n):
        for j in range(m):
            if ll[i][j]=='.':
                W[j] += 1
    B     = [n-c for c in W]  #Black
    Bw    = [inf]*(y+1)
    Ww    = [inf]*(y+1)
    Bw[1] = B[0]
    Ww[1] = W[0]
    Bv    = B[0] if x==1 else inf
    Wv    = W[0] if x==1 else inf
    for i in range(1,m):
        for j in range(y,0,-1):
            Bw[j] = Bw[j-1]+B[i]
            Ww[j] = Ww[j-1]+W[i]
        if Bv < inf:    #if valid!
            Ww[1] = Bv + W[i]
            Bw[1] = Wv + B[i]
        Bv = min(Bw[x:y+1])
        Wv = min(Ww[x:y+1])
    return min(Bv,Wv)

n,m,x,y = list(map(int,input().split()))
ll = [input() for _ in range(n)]
print(f(ll,n,m,x,y))

