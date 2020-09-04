#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/1028/B
#a和b的位数和都>=n; a+b的位数和都<=m
#https://codeforces.com/blog/entry/61493
#构建算法还真是要敢想

def f(l):
    n,m = l #1129
    return ['5'*282,'4'*281+'5']

l = list(map(int,input().split()))
[print(r) for r in f(l)]
