#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1108/B
# 有点水,因为大的一下可以找出来

def f(l):
    l.sort(reverse=True)
    x  = l[0]
    n  = len(l)
    for i in range(1,n):
        if x%l[i]>0 or l[i]==l[i-1]:
            return [x,l[i]]

_ = int(input())
l = list(map(int,input().split()))
print(*f(l))
