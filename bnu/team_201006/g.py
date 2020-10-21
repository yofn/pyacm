#!/usr/bin/env python3
#https://codeforces.com/group/H9K9zY8tcT/contest/297264/problem/G
#最爱构造
#难在N=1e5, 比K小

def f(k):
    l   = []
    m   = ['+','=']
    if  k==1:
        print(2)
        print(1)
        print('1 2')
        return
    while k>1:
        l.append(m[k%2])
        k   = k//2
    n   = len(l)    # n for #2 and #(=/+)
    print(n<<2)     # L1: #nodes

    pl  = list(range(1,n))
    for i in range(n):
        pl.extend([i+1,n+1+i*3,n+1+i*3])
    print(*pl)      # L2: ..

    gw  = [2<<i for i in range(n,-1,-1)]
    wl  = [0]*(n<<2)
    for i in range(n):
        wl[i]  = gw[i]
        wl[i] += 2 if l[i]=='+' else 0
    for i in range(n):
        wl[n+i*3]   = gw[i]//2
        wl[n+i*3+1] = gw[i]//4
        wl[n+i*3+2] = gw[i]//4
    print(*wl)      # L3: ..

k   = int(input())        #1e9
f(k)
