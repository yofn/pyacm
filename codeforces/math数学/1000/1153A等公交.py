#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1153/A

n,t =  list(map(int,input().split()))
sdl = [list(map(int,input().split())) for _ in range(n)]
mbl = [max(0,(t-sd[0]+sd[1]-1)//sd[1])*sd[1] + sd[0] for sd in sdl]
print(1+mbl.index(min(mbl)))
