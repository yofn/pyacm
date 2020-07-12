#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/189/A
#n分为a,b,c三个长度; 求最常分法.
#典型DP: 递归/记忆化搜索容易些? 或者用更适合py的构建?
#或许用bfs/BFS? 但和bfs相比,DP只需一层层记录,所以还是更像DP
#看来BFS是一条弯路..还是回到递归和记忆化搜索.
#倒着用set?

n,a,b,c = list(map(int,input().split()))    #<4000

ss  = set([n])
ii  = 0
cl  = []
while len(ss)>0:
    ss  = set([i-j for i in ss for j in [a,b,c] if i>=j])
    ii += 1
    if  0 in ss:
        cl.append(ii)
print(max(cl))
