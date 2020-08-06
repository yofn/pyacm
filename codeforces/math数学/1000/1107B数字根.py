#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1107/B
# 类似筛子?
# https://codeforces.com/blog/entry/64847
# 性质: n%9=x

def f(l):
    k,x = l
    return 9*(k-1)+x

t = int(input())
for _ in range(t):
    l = list(map(int,input().split()))
    print(f(l))
