#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/522/A
#求转发链的最大长度
#NOTE: 大小写不敏感
#这是(迭代式)DFS/dfs的一个例子.
#好像不是特别标准的DFS实现?

n  = int(input())
vd = {}
for i in range(n):
    vf,_,vt = input().lower().split()
    if vt not in vd:
        vd[vt] = []
    vd[vt].append(vf)
vs  = ['polycarp']*(n+1)    #vertice stack
sp  = 0                     #stack pointer
vl  = {'polycarp':1}        #layer of Vs
while sp>-1:      #while stack is not empty
    p   = vs[sp]  #pop top as parent
    sp -= 1       #pop is MUST!
    if p not in vd: # no child, no push
        continue
    for v in vd[p]: # push all children with L+1
        sp   += 1
        vs[sp]= v
        vl[v] = vl[p]+1
print(max(vl.values())) 
