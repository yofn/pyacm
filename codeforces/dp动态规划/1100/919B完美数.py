#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/919/B
# 第一个正经的DP?

k = int(input())

t = [[0]*11]
while True:
    l = [1]*10+[0]
    s = 0
    for j in range(1,11):
        s    += t[-1][j]
        l[j] += s
    t.append(l)
    if l[-1]>=k:
        break
i,j = len(t)-2,10
ss = 10
kk = 0
n  = 0
while i>=1:     #now will want to find bigger kk and decompose
    kk += t[i][j]
    if kk<k:
        j -= 1
        continue
    k  = t[i][j]-(kk-k)
    i -= 1
    kk = 0
    x  = ss-j       #found digit
    ss-= x          #update sum
    n  = n*10+x     #update value
print(n*10+ss)
