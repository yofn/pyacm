#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/1097/B
#n<=15 太小了完全可以暴力
#n更大时应如何优化? 剪枝?
#360也很小,完全可以利用

n   = int(input())
a   = [int(input()) for i in range(n)]
s   = set([0])
for x in a:
    ns = set()
    for y in s:
        ns.add((y+x)%360)
        ns.add((y-x)%360)
    s  = ns
print('YES' if sum([y%360==0 for y in s])>0 else 'NO')
