#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/233/A

n = int(input())
print(-1 if n%2!=0 else ' '.join(map(str,[i+2 if i%2==0 else i for i in range(n)])))
