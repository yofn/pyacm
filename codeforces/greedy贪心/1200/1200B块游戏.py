#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/1200/B
#n=列数;m=包里初始块;k=允许向右的非负正数(i->i+1)

def fPass(hl,n,m,k):
    for i in range(n-1):
        m  += hl[i]-max(hl[i+1]-k,0) #NOTE: the lower bound 0!!
        if m<0:
            return False
    return True

tc = int(input())
rl = []
for i in range(tc):
    n,m,k   = list(map(int,input().split()))
    hl      = list(map(int,input().split()))
    rl.append(fPass(hl,n,m,k))
[print('YES' if r else 'NO') for r in rl]
