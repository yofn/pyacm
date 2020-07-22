#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/653/B
#有dp和暴力两种解法
#dp可以优化..(目前不是最优)

n,q = list(map(int,input().split()))
ql  = [input().split() for _ in range(q)]
d   = {c:[q[0][0] for q in ql if q[1]==c] for c in "abcdef"}
cl  = ['a']
for i in range(n-1):
    cl = [nc for c in cl for nc in d[c]]
print(len(cl))

