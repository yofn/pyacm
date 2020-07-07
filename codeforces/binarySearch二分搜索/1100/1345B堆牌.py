#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1345/B
# cn = c(n-1) + 3*n + 2
# (3*n*n)//2 + (7*n)//2 + 2  #没必要求出这个了?
# 必须二分?

'''
cl  = [2]
mxx = 10**9
i   = 1
while True:
    cl.append(cl[-1]+3*i+2)
    if cl[-1]>mxx:
        break
    i += 1
'''
# card construction list:   O(n)
cl  = [(3*i*i+7*i)//2 + 2 for i in range(30000)]

def bs(k,li):
    l, r    = 0, len(li)-1
    if li[l] >  k:  return 0
    if li[r] <= k:  return len(li)
    while True:     #HOLD: li[l]<=k<li[r] VERY important!
        if  r-l<2:  return r
        m   = l + ((r-l) >> 1)  #safer; NOTE: () for right order
        if  li[m]>k:
            r = m
        else:
            l = m

m   = int(input())  #<1000
for i in range(m):
    n = int(input())
    r = len(cl)
    c = 0
    while True:
        j = bs(n,cl[:r])#NOTE: r is returned, not l
        if j==0:        # no good!
            break
        n  = n-cl[j-1]  # construct +1
        c += 1
        r  = j          # j-1 will miss double 2!
    print(c)
