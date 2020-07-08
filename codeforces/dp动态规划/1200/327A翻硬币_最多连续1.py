#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/327/A
# n<=100, 可以用暴力
# 也可以用DP?
# 读错题意了~~~~

n  = int(input())
a  = list(map(int,input().split()))
# ALL 1 CASE!
if 0 not in a:
    print(len(a)-1)
    exit(0)
# counters
l1 = [a[0]]*n
for i in range(1,n):
    if a[i]==1:
        l1[i] = l1[i-1]+1
    else:
        l1[i] = 0
r1 = [a[-1]]*n
for i in range(n-2,-1,-1):
    if a[i]==1:
        r1[i] = r1[i+1]+1
    else:
        r1[i] = 0
c  = 0  #number of ones possible!
m  = 0  #max consecutive 0s
for i in range(n):
    if a[i]==1:
        c += r1[i]
        if c>m:
            m=c
        c  = l1[i]
    else:
        c += 1      #flipped
print(max(m,c))     #for 110000 case
