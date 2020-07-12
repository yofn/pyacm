#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/998/B

n,b = list(map(int,input().split()))
al  = list(map(int,input().split()))

od  = ((al[0]%2)<<1)-1  #od=odd-even
cl  = []
for i in range(1,n-2):
    od += ((al[i]%2)<<1)-1
    if od == 0:
        d  = al[i+1]-al[i]
        cl.append(d if d>0 else -d)
        od = 0
cl.sort()
s   = 0 
i   = 0
while i<len(cl):
    s   += cl[i]
    if s>b:
        break
    i   += 1
print(i)
