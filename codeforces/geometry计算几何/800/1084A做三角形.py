#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/1084/A

maket = lambda l: max(0,(max(l)<<1)+1-sum(l))
print(maket(list(map(int,input().split()))))

