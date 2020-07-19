#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/777/B

n   = int(input())  #1000
il  = [int(c) for c in input()]
jl  = [int(c) for c in input()]

il.sort()
jl.sort()
i   = 0
j   = 0
lc  = 0
while j<n:
    if jl[j]>=il[i]:
        i  += 1
    else:
        lc += 1
    j += 1
print(lc)   #min # of lose
i   = 0
j   = 0
wc  = 0
while j<n:
    if jl[j]>il[i]:
        i  += 1
        wc += 1
    j += 1
print(wc)   #max # of win

