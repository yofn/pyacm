#!/usr/bin/env python3

#https://codeforces.com/group/H9K9zY8tcT/contest/297258/problem/I


def f(l):
    n = len(l)
    l.sort()
    l = [l[i]/(i+1) for i in range(n)]
    if max(l)>1:
        return -1
    return min(l)

_ = input()
l = list(map(int,input().split()))
print(f(l))
