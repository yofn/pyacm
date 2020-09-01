#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/557/A

def f(n,l):
    l1,r1=l[0]
    l2,r2=l[1]
    l3,r3=l[2]
    c1 = min(r1,n-l2-l3)
    c2 = min(r2,n-c1-l3)
    c3 = n-c1-c2
    return [c1,c2,c3]

n = int(input())
l = [list(map(int,input().split())) for _ in range(3)]
print(*f(n,l))
