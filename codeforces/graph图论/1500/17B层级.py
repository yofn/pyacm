#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/17/B
# 覆盖所有节点的最短路径?
# 图的表示:  matrix, list 
# https://www.geeksforgeeks.org/comparison-between-adjacency-list-and-adjacency-matrix-representation-of-graph/
# DFS的实现: stack(非递归); 递归
# https://likegeeks.com/depth-first-search-in-python/
# 到底是DSU更好还是DFS更好?
# https://codeforces.com/blog/entry/451
# 即不用DSU也不用DFS, 可以用最小生成树或贪心方法(取cost最小的parent)

def f(n,l):
    pl = [None]*(n+1)   #p[0] is not used!
    for a,b,c in l:
        if pl[b] is None:
            pl[b] = []
        pl[b].append(c)
    cr = sum([p is None for p in pl])
    if cr>2:
        return -1
    return sum([min(p) for p in pl if p is not None])

n = int(input()) #1000
input()
a = int(input())
l = [list(map(int,input().split())) for _ in range(a)]
print(f(n,l))
