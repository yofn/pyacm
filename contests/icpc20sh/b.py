#!/usr/bin/python3

def f(l1,l2):
    n,m = len(l1),len(l1[0])
    d   = sum([l1[i][j]!=l2[i][j] for i in range(n) for j in range(m)])
    if d*2 > n*m:
        for i in range(n):
            for j in range(m):
                l1[i][j] = 'X' if l1[i][j]=='.' else '.'
    return [''.join(l) for l in l1]

n,m =  list(map(int,input().split())) 
l1  = [list(input()) for i in range(n)]
l2  = [list(input()) for i in range(n)]
[print(l) for l in f(l1,l2)]
