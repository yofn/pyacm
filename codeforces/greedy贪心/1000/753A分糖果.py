#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/753/A

n = int(input())
l = list(range(1,51))
t = 0
for i in l:
    t += i 
    if t>n:
        break
print(i-1)
print(*(l[:i-2]+[n-t+i+i-1]))
