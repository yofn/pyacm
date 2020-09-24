#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/1373/C
# 题目比较有意义
# + 看懂伪代码!
# + 能找出规律!
# 1. ok的含义是什么? cur是否>=0
# 2. 什么时候跳出外层的循环?(只能跳出,因为inf!) 当init按s操作后ok时(结果非负时)
# 3. res的含义是什么? 记录用了多少次s里的字符..
# 改进: 这两个循环是否可以合并??

def f(l):
    n  = len(l)
    sl = [0]*n
    sl[0] = 1 if l[0]=='+' else -1
    for i in range(1,n):
        sl[i] = sl[i-1] + (1 if l[i]=='+' else -1)
    nl  = []
    ref = 0
    for i in range(n):
        if sl[i]<ref:
            nl.append(i+1)
            ref -= 1
    return sum(nl) + n

n = int(input())
for _ in range(n):
    print(f(input()))

