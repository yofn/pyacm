#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1204/A
# 翻译成人话: 2**k, k必须连续
# 编号是1024就贴切了..

def f(l):
    n,l,r = l
    return [2**l-1+(n-l),2**r-1+(n-r)*2**(r-1)]

l   = list(map(int,input().split()))
print(*f(l))

