#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/1037/C
#swap代价|i-j|, flip代价1; 修改a让其等于b; 求最小成本
#相邻的swap才划算; 相隔>2,不如两个分别flip!

n   = int(input())  #1e6
a   = input()
b   = input()
sb  = (a[0]!=b[0])   #swapable
c   = 1 if sb else 0
for i in range(1,n):
    if a[i] == b[i]:
        sb  = False
        continue
    if (not sb) or a[i]==a[i-1]:
        c  += 1
        sb  = True
    else:
        sb  = False
print(c)
