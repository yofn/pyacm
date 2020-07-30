#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1013/A

n   = int(input())
xl  = list(map(int,input().split()))
yl  = list(map(int,input().split()))
print('Yes' if sum(xl)>=sum(yl) else 'No')

