#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1375/A
# 感觉没有找到一个好方法!
# 搜索和构建的选择!
# 如果要求最优,就必须搜索.
# 如果搜索空间很大且没有优化的思路,就应该考虑构建!

def f(l):
    n  = len(l)
    for i in range(n):
        if (i%2==0 and l[i]<0) or (i%2>0 and l[i]>0):
            l[i] = -l[i]
    return l

q = int(input())
for i in range(q):
    _ = input()
    print(*f(list(map(int,input().split()))))
