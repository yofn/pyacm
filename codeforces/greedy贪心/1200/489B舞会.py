#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/489/B

n  = int(input())
a  = list(map(int,input().split())) 
m  = int(input())
b  = list(map(int,input().split())) 
a.sort()
b.sort()

i,j =0,0
c   =0
dif =[-1,0,1]
while True:
    if i>=n or j>=m:
        break
    if a[i]-b[j] in dif:
        i += 1
        j += 1
        c += 1
    elif a[i]>b[j]:
        j += 1
    else:
        i += 1
print(c)

