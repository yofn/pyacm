#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/1042/B
# 2^1000超标
# 采用记忆性搜索..
# 字符串分割不合适

n   = int(input())
d   = {}
for i in range(n):
    c,s = input().split()
    c   = int(c)
    s   = ''.join(sorted(s.lower()))
    if (s not in d) or c<d[s]:
        d[s] = c
md  = {}
def mcost(k):
    global d, md
    if len(k)==1:
        return d[k] if k in d else None
    if k in d:
        md[k] = d[k]
    ss  = set([(k[i],k[0:i]+k[i+1:]) for i in range(len(k))])
    for c,k2 in ss:
        if k2 not in md:    # recurse if not in memory
            md[k2] = mcost(k2)
        if (c not in d) or (md[k2] is None):
            continue        # c+k2 FAIL
        ncost = d[c] + md[k2]
        if (k not in md) or (ncost < md[k]):
            md[k]  = ncost 
    return md[k] if k in md else None
print(-1 if mcost('abc') is None else md['abc'])
