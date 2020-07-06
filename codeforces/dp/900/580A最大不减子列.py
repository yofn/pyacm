#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/580/A
#严格来说不能算DP?

_ = input()
l = list(map(int,input().split())) #https://codeforces.com/blog/entry/71884

maxL = 1
curL = 1
for i in range(1,len(l)):
    if l[i]<l[i-1]:
        curL  = 1
        continue
    curL += 1
    if curL > maxL: maxL = curL
print(maxL)
