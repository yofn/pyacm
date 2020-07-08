#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/522/B

n  = int(input())
pp = [list(map(int,input().split()))+[i] for i in range(n)]
tw = sum([p[0] for p in pp])
pp = sorted(pp,key=lambda p:p[1])
for i in range(n-1):
    pp[i].append( (tw-pp[i][0])*pp[-1][1] )
pp[-1].append( (tw-pp[-1][0])*pp[-2][1])
pp = sorted(pp,key=lambda p:p[2])
print(*[p[3] for p in pp])
