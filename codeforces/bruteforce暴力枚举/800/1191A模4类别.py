#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1191/A

n  = int(input())
cl = ['A','A','B','A']
il = [1,0,1,2]
print(il[n%4],cl[n%4])
