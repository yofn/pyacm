#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/1176/C
#最少移除的数字,使得剩余6l个数可以分为l个子序列[4,8,15,16,23,42]
#贪心?

n   = int(input())  #5e5
al  = list(map(int,input().split()))

rl  = [4,8,15,16,23,42]
cl  = [0]*6
for i in range(n):
    p = rl.index(al[i])
    if p==0 or cl[p]<cl[p-1]:
        cl[p] += 1
print(n-cl[-1]*6)
