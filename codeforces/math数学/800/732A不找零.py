#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/732/A
# 之前尝试打表,有点问题


def buy(k,r):
    for i in range(1,11):
        if (k*i)%10 in [0,r]:
            return i

k,r = list(map(int,input().split()))
print(buy(k,r))
