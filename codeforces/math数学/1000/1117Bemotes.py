#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1117/B

def f(l,m,k):
    l.sort(reverse=True)
    n2 = m//(k+1)
    return m*l[0]-n2*(l[0]-l[1])

n,m,k   = list(map(int,input().split()))
al      = list(map(int,input().split()))
print(f(al,m,k))
