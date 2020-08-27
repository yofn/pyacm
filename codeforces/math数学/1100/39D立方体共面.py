#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/39/D

def f(l1,l2):
    return sum([l1[i]==l2[i] for i in range(len(l1))])>0

l1 = list(map(int,input().split()))
l2 = list(map(int,input().split()))
print('YES' if f(l1,l2) else 'NO')
