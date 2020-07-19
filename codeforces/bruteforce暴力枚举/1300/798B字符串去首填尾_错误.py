#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/798/B
#T94 报错

n   = int(input())    #50
sl  = [input() for _ in range(n)]
r   = sl[0]
m   = len(r)
ml  = [0]
for s in sl[1:]:
    for i in range(m):
        if (s[i:]+s[:i])==r:
            ml.append(i)
            break
print([[(i+j)%m for i in ml] for j in range(m)])
print(min([sum([(i+j)%m for i in ml])for j in range(m)]) if len(ml)==n else -1)
