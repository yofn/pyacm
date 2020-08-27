#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/987/B
# https://codeforces.com/blog/entry/59758
# 求f=ln(x)/x的导数,看f的曲线
# 思路1: 实现所有情况的逻辑
# 思路2: 调用实际函数ln(x)/x
# 思路3: 构建一个函数代替ln(x)/x

def f(l):
    g = lambda x: 1/x if x>2 else [0,1/4][x-1]
    r = list(map(g,l))
    if r[0]>r[1]:
        return '>'
    if r[0]<r[1]:
        return '<'
    return '='

l = list(map(int,input().split()))
print(f(l))
