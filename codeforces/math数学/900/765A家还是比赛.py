#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/765/A
# 所以只要第一行输入就够了....

n   = int(input())
h   = input()
tl  = [input() for _ in range(n)]
print('home' if n%2==0 else 'contest')

