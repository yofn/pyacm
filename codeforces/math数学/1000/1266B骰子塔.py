#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1266/B
# 相对的面和为7,所以中间骰子可见的面=14; 骰子塔可见的面=14*k+(1-6)

n = int(input())
l = list(map(int,input().split()))
[print('YES' if i>14 and (i-1)%14<6 else 'NO') for i in l]
