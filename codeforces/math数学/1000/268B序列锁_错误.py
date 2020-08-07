#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/268/B
# 总共要按几下,不是尝试几次!
# n*1 + 2*(n-1) + 3*(n-2) + ..
# 有没有通项?
# f(n+1)=f(n)+??

def f(n):
    s = 0
    for i in range(1,n):
        s += i*(n+1-i)
    return s+1

n = int(input())    #2000
print(f(n))
