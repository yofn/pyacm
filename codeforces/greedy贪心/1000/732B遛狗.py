#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/732/B

n,k = list(map(int,input().split()))
an  = list(map(int,input().split())) 

cn  = [0]*n
for i in range(1,n):
    cn[i] = max(k-an[i-1]-cn[i-1]-an[i],0)
print(sum(cn))
print(*[cn[i]+an[i] for i in range(n)]) 
