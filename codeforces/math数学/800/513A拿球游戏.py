#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/513/A

n1,n2,k1,k2 = list(map(int,input().split()))
print('First' if n1>n2 else 'Second')
