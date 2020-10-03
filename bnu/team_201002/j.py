#!/usr/bin/env python3

#https://codeforces.com/group/H9K9zY8tcT/contest/297258/problem/J
#很简单的问题,但好像不好搞!
#DP问题?
#需要什么数据结构? 区间?

def f(l):
    j = l[0]
    l = l[1:]
    l = [j-i for i in l]
    l.sort()
    s = l[0]+l[1]
    if l[2]>=s:
        return s
    return l 

_  = input()
l  = list(map(int,input().split()))
print(f(l))
