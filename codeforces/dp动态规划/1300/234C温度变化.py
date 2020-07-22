#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/234/C
# input.txt
# output.txt

with open('./input.txt') as f:
    n   = int(f.readline())
    tl  = list(map(int,f.readline().split()))
lp  = [0]*n
rn  = [0]*n
lp[0]   = 0 if tl[0]<0  else 1
rn[-1]  = 0 if tl[-1]>0 else 1
for i in range(1,n):
    lp[i] = lp[i-1] if tl[i]<0 else lp[i-1]+1
for i in range(n-2,-1,-1):
    rn[i] = rn[i+1] if tl[i]>0 else rn[i+1]+1
with open('./output.txt','w') as f:
    f.write('%s'%(min([lp[i]+rn[i+1] for i in range(n-1)])))
