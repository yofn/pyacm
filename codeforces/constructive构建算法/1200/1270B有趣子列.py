#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/1270/B
#只要相邻的相差>1就可以

ab = lambda x: x if x>0 else -x

def f(l):
    n = len(l)
    for i in range(n-1):
        if ab(l[i]-l[i+1])>1:
            return [['YES'],[i+1,i+2]]
    return [['NO']]

q = int(input())
for _ in range(q):
    _ = input()
    l = list(map(int,input().split()))
    [print(*r) for r in f(l)]
