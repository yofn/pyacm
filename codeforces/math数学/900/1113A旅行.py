#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1206/B
# 数学题,非DP

n,v = list(map(int,input().split()))
print(n-1 if n-1<=v else v + (n-v-1)*(n-v+2)//2)
