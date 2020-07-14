#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/959/B
#发消息的最小成本?
#好像和并查集关系不大..也就是一个分组的概念而已!


n,k,m   = list(map(int,input().split())) #1e5@nkm
voc     = input().split()
al      = list(map(int,input().split()))
gl      = [list(map(int,input().split())) for _ in range(k)]    #g[0] is number of words in group
wl      = input().split()

w2i     = {voc[i]:i for i in range(n)}
g2c     = [min([al[i-1] for i in g[1:]]) for g in gl]
i2g     = [None]*n
for gi,g in enumerate(gl):
    for i in g[1:]:
        i2g[i-1]=gi
cost    = sum([g2c[i2g[w2i[w]]] for w in wl])
print(cost)

