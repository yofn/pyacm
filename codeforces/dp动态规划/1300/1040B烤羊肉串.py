#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/1040/B

n,k = list(map(int,input().split()))
r   = n%(k+k+1)
if   r==0:
    s = k+1
elif r>k+1:
    s = r-k+1
else:
    s = r
l   = list(range(s,n+1,2*k+1))
print(len(l))
print(*l)
