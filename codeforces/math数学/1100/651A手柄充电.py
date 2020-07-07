#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/651/A
# 数学,DP,贪心?
# 注意边界条件..

a1,a2 = list(map(int,input().split()))
if a1<=1 and a2<=1:
    print(0)
else:
    print(a1+a2-3 if (a1-a2)%3==0 else a1+a2-2)
