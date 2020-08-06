#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1353/B
# f(2n+1) = f(2n-1) + 8*n*n
# 1+4+8+9+.. = n*(n+1)*(2n+1)/6
# 幂和公式..
# 所以此题中: f(n)=n*(n+1)*(n-1)*2//3

t = int(input())
for _ in range(t):
    n   = int(input())
    print((n-1)*n*(n+1)//3)
