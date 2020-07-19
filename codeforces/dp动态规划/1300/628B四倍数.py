#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/628/B
#nn: 1  2  3  4  5  6  7  8  9 10
#str 5  8  1  0  4  3  8  1  7  4
#--------------------------------
#n1: 1  0  3  0  0  6  0  8  9  0
#n2: 0  1  0  3  0  0  6  0  0  9
#n4: 0  1  0  1  5  0  1  0  0  1
#--------------------------------
#c4: 0  1  1  2  7  7  8  8  8  9
#nn包含最近1位的情况!!
#连续情况!!!
#rev4718340185

s  = input()
n1,n2,n4,c4 = 0,0,0,0
for i in range(len(s)):
    r = int(s[i])%4
    if r==1 or r==3:
        n1,n2,n4 = i+1,0,0
    elif r==2:
        n1,n2,n4 = 0,(n2+n4+1),n1
    else:
        n1,n2,n4 = 0,n1,(n2+n4+1)
    c4 += n4
print(c4)
