#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1343/A
# 前半是偶数,后半是奇数
# 前半和=后半和..

t = int(input())
for _ in range(t):
    n   = int(input())
    if n%4 != 0:
        print('NO')
    else:
        print('YES')
        print(*([i*2+2 for i in range(n//2)] + [i*2+1 for i in range(n//2-1)] + [n+n//2-1]))
