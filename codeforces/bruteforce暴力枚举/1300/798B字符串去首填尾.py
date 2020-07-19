#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/798/B
#T94 报错
#解决自身循环相等的问题
#print([[(i+j)%c for i in ml] for j in range(c)])

n   = int(input())    #50
sl  = [input() for _ in range(n)]
r   = sl[0]
m   = len(r)
c   = m
for i in range(1,m):
    if r[i:]+r[:i]==r:
        c = i
        break
ml  = [0]
for s in sl[1:]:
    for i in range(c):
        if (s[i:]+s[:i])==r:
            ml.append(i)
            break
print(min([sum([(i+j)%c for i in ml])for j in range(c)]) if len(ml)==n else -1)
