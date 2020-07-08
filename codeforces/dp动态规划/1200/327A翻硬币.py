#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/327/A
# n<=100, 可以用暴力
# 也可以用DP?
# 下面的列表用了大量n**2复杂度,如果n大应该优化成线性!

n  = int(input())
a  = list(map(int,input().split()))
# ALL 1 CASE!
if 0 not in a:
    print(len(a)-1)
    exit(0)
# ZERO INSIDE!
lmx = [0]*(n+2)
rmx = [0]*(n+2)
lkg = [0]*(n+2)
rkg = [0]*(n+2)
for i in range(1,n+1):
    lkg[i] = lkg[i-1]+1 if a[i-1]==1 else lkg[i-1]-1
    lmx[i] = max(lmx[i-1],lkg[i])
lkg[n+1] = lkg[n]
lmx[n+1] = lmx[n]
for i in range(n,1,-1):
    rkg[i] = rkg[i+1]+1 if a[i-1]==1 else rkg[i+1]-1 
    rmx[i] = max(rmx[i+1],rkg[i])
rkg[0]   = rkg[1]
rmx[0]   = rmx[1]
kmx = max([lmx[i]+rmx[i] for i in range(n+2)])
print(n-sum(a)+kmx)
