#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/189/A
#n分为a,b,c三个长度; 求最常分法.
#典型DP: 递归/记忆化搜索容易些? 或者用更适合py的构建?
#或许用bfs/BFS? 但和bfs相比,DP只需一层层记录,所以还是更像DP

n,a,b,c = list(map(int,input().split()))    #<4000
ss      = set([a,b,c])
ii      = 0
while min(ss)<n:
    l   = list(ss)
    ss  = set([i+j for i in l for j in [a,b,c]])
    ii += 1
    print(ss)
print(ii)

