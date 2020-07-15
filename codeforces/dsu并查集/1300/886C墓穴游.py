#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/886/C
#一种比较特殊的并查集?
#像,但a tiny part!
#关键是解决last问题..

n   = int(input())
tl  = [0] + list(map(int,input().split()))    #2e5
ll  = list(range(n+1))  #0-n
cnt = 1
for m,t in enumerate(tl):
    if ll[t] > t:
        ll[m]  = m
        cnt   += 1
    else:
        ll[t]  = m
print(cnt)

