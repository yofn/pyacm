#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/1037/C
#swap代价|i-j|, flip代价1; 修改a让其等于b; 求最小成本
#相邻的swap才划算; 相隔>2,不如两个分别flip!

n   = int(input())  #1e6
a   = input()
b   = input()
print(a)
print(b)
c   = 0
sb  = False         #swapable
for i in range(n):
    if a[i] == b[i]:
        sb  = False
        continue
    if not sb:
        c  += 1
        sb  = True
    else:
        sb  = False
print(c)
