#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/69/A

def f(ll):
    n = len(ll)
    for l in ll[1:]:
        for i in range(3):
            ll[0][i] += l[i]
    return sum([i==0 for i in ll[0]])==3 

t  = int(input())
ll = [list(map(int,input().split())) for _ in range(t)]
print('YES' if f(ll) else 'NO')
