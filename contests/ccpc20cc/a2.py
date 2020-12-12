#!/usr/bin/env python3
# brute-force or 01 backpack!
 
c = [648,328,198,88,28, 6,1]
r = [388,198,128,58,28,18,8]
 
def make(i,n):
    if i==7:
        return n*10
    if n>=c[i]:
        r1 = make(i+1,n)    #not buy this!
        r2 = (r[i]+c[i]*10) + make(i+1,n-c[i])
        return max(r1,r2)
    else:
        return make(i+1,n)
 
n = int(input())
print(make(0,n))
