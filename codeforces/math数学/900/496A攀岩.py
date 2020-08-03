#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/496/A
# 要拿走一个使得相邻的距离最小, 但答案是剩下所有距离最大的

n   = int(input())
l   = list(map(int,input().split()))
mi  = l[-1]-l[0]
for i in range(1,n-1):
    if l[i+1]-l[i-1] < mi:
        mi = l[i+1]-l[i-1]
mx  = max([l[i]-l[i-1] for i in range(1,n)])
print(max(mi,mx))

