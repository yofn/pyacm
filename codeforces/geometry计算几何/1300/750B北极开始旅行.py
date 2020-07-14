#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/750/B
#球面坐标系?
#不用那么复杂,从示意图看,只需要关注向北和向南的就行,东西的不用管
#错误1=题目理解不对,East不能删除.如果在南北极出现不允许的方向就应该返回NO
#这个题目出的不太好!

def okay(jl):
    x   = 0
    for l,d in jl:
        if (x==0 and d!='S') or (x==20000 and d!='N'):
            return False
        if d=='S':
            x += l
        if d=='N':
            x -= l
        if x<0 or x>20000:
            return False
    return x==0

n   = int(input())
jl  = []
for i in range(n):
    l, d = input().split()
    jl.append((int(l),d[0]))
print('YES' if okay(jl) else 'NO')
