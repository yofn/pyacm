#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/148/A
# 可以用实现, 可以用数学. 实现可读性更强? 所以用实现来做

k = int(input()) 
l = int(input()) 
m = int(input()) 
n = int(input()) 
d = int(input()) 

dd = [False]*(d+1)
mm = min(k,l,m,n)
for i in range(1,((d+mm-1)//mm)+1):
    if i*k <= d: dd[i*k] = True
    if i*l <= d: dd[i*l] = True
    if i*m <= d: dd[i*m] = True
    if i*n <= d: dd[i*n] = True

print(sum(dd))

