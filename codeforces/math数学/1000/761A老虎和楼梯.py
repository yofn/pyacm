#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/761/A
# 题目是interal, 不一定是从1开始, 所以之前做错了; 但还是很无聊的题目
# 0 0 不可能, 错第二次

def f(l):
    a,b = l
    return (b==a+1 or b==a or b==a-1) and (a+b>0)

l = list(map(int,input().split()))
print('YES' if f(l) else 'NO')
