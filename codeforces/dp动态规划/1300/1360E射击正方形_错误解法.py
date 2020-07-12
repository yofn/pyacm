#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/1360/E
#判断射击结果图是真还是假!
#注意confidence的传递次序.

t = int(input())        #1000
for _ in range(t):
    n   = int(input())    #50
    s   = [[int(c) for c in input()] for i in range(n)]
    print(s)
    rl  = [s[i][j] for i in range(n) for j in range(n-1,-1,-1)] #(t-d)(r-l)
    bu  = [s[i][j] for j in range(n) for i in range(n-1,-1,-1)] #(r-l)(d-t)
    for ii in range(n*n):
        if ii%n==0:
            continue
        rl[ii] = rl[ii]*rl[ii-1]
        bu[ii] = bu[ii]*bu[ii-1]
        if rl[ii]==1:   #supports 1 at ii
            s[ii//n][n-1-ii%n] = 0  #no worry about this!
        if bu[ii]==1:   #supports 1 at ii
            s[n-1-ii%n][ii//n] = 0  #no worry about this!
    su  = [(i,j) for i in range(n) for j in range(n) if s[i][j]>0]
    print(su)
    print('YES' if len(su)==0 else 'NO')
