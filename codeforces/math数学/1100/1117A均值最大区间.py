#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1117/A
# 思路1.前缀和.
# 思路2.最大值的位置,周围有几个一样的...但还有考虑多个最大值..
# 思路3.count run lengths(用点数据结构)

def f(l):
    mt = [l[0],1]
    rt = [l[0],1]
    n  = len(l)
    l.append(-1)    # deal boundary
    for i in range(1,n+1):
        if l[i]==l[i-1]:
            rt[1] += 1
            continue
        #new start
        if rt[0]>mt[0] or (rt[0]==mt[0] and rt[1]>mt[1]):
            mt = [rt[0],rt[1]]  # a better segment; NOTE: avoid shallow copy
        rt = [l[i],1] 
    return mt[1]

n = int(input())
l = list(map(int,input().split()))
print(f(l))
