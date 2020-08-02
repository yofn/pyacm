#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/973/A
# 先排序?? 或者不排序,找最小值; 或者都不用直接看是否同余!
# 由于要算次数,所以还是得求最小值..

n,k = list(map(int,input().split()))    #1e5, 1e9
al  = list(map(int,input().split()))
rl  = [a%k for a in al]
if max(rl)>min(rl):
    print(-1)
else:
    ma  = min(al)
    jl  = [(a-ma)//k for a in al]
    print(sum(jl))
