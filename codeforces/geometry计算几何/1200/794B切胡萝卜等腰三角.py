#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/794/B
#胡萝卜是1xh的等边三角形, 切成n等分; 从上向下给出下刀列表.

from math import sqrt

n,h = list(map(int,input().split()))
print(*[ h*sqrt(i/n) for i in range(1,n)])

