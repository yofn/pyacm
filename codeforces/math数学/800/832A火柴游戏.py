#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/832/A

n,k = list(map(int,input().split()))
print('YES' if (n//k)%2==1 else 'NO')

