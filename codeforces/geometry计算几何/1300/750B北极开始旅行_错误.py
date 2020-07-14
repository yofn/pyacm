#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/750/B
#球面坐标系?
#不用那么复杂,从示意图看,只需要关注向北和向南的就行,东西的不用管

n   = int(input())
jl  = []
for i in range(n):
    l, d = input().split()
    if d[0] in ['N','S']: 
        jl.append(int(l) if d[0]=='S' else -int(l)) #encode d in +/-
x   = 0
for j in jl:
    x = min(max(0,x+j),20000)
print('YES' if x==0 else 'NO')
