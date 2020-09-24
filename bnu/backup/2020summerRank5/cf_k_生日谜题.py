#!/usr/bin/env python3

# 2020暑期排位5K_生日谜题
# https://codeforces.com/group/H9K9zY8tcT/contest/286081/problem/K
# bit-operation? 不适合python? 也能做
# 还能用dfs来做!?

t = input()
l = list(map(int,input().split())) 

nob     = 20            #as ai<10^5
n       = len(l)
counts  = [sum([(1<<i)&x == 0 for x in l]) for i in range(nob)]    #count zero for each bit!
total   = sum([((1 << n) - (1 << counts[i])) << i for i in range(nob)])
print(total)
