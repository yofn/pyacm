#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/902/B
#通过三个列表(cl,pl,sl)实现了并查的部分思想.

n   = int(input())  #1e4
pl  = list(map(int,input().split()))
cl  = list(map(int,input().split()))

pl  = [0] + [p-1 for p in pl]
sl  = [None]*n  #None=unvisit, False=non-root, True=root
for i in range(n):
    if sl[i] is not None:
        continue
    j   = i
    while pl[j]!=j and cl[pl[j]]==cl[j]:
        sl[j]   = False
        j       = pl[j]
    sl[j] = True

print(sum(sl))

