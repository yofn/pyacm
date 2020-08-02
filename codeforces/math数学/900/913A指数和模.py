#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/913/A
# 求m%(2**n), 问题是n,m都很大..
# 用bit运算?? mask??
# n很大,直接算肯定会溢出,所以要利用数学属性?
# 如果n足够大, 答案就是m
# 如果n不够大, 就可以用对m的位运算?
# https://codeforces.com/blog/entry/56992
# 敢于尝试/落实最简单的方案

n = int(input())    #1e8
m = int(input())    #1e8
print(m if n>=27 else m%(2**n))


