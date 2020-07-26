#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/180/C
#这个题难度好像标的有点虚高

s   = input()   #1e5
n   = len(s)
ll  = [0]*(n+1) #lower@left
ur  = [0]*(n+1) #upper@right
for i in range(n):
    ll[i+1]  = ll[i]+1   if s[i].islower() else ll[i]
for i in range(n-1,-1,-1):
    ur[i]    = ur[i+1]+1 if s[i].isupper() else ur[i+1]
print(min([ll[i]+ur[i] for i in range(n+1)]))

