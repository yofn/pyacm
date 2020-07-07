#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/363/B
# 辅助型数组(积分/前缀/累加)

n,k =   list(map(int,input().split()))
h   =   list(map(int,input().split()))
ss  =   [0,h[0]]
for i in range(2,n+1):
    ss.append(ss[-1]+h[i-1])#s[2]=s[1]+h[1]
ii  =   1
mc  =   ss[-1]  #max
for i in range(1,n-k+2):
    c = ss[i+k-1]-ss[i-1]   #s[k]=sum of 1-k
    if c < mc:
        ii = i
        mc = c
print(ii)
