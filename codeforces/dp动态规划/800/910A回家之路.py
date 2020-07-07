#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/910/A

n, d = list(map(int,input().split())) 
s    = input()

i    = n-1
jmps = 1
fail = False
while True:
    x   = max(i-d,0)
    if x==0:
        print(jmps)
        break
    ii  = s.find('1',x,i)
    if  ii  == -1:
        print(-1)
        break
    i     = ii
    jmps += 1

