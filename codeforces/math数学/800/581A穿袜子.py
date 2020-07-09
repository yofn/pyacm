#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/581/A

a,b = list(map(int,input().split()))
print(min(a,b),(max(a,b)-min(a,b))//2)
     
