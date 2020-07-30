#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1047/A

n   = int(input())
l   = [[1,1],[1,1],[1,2]]
r   = l[n%3]
r.append(n-sum(r))
print(*r)
