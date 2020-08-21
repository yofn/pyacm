#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/371/M

def f(l1,l2):
    n,k = l1
    nol = n//k
    sl  = [sum(l2[i:n:k]) for i in range(k)]
    return sum([min(nol*2-s,s-nol) for s in sl])

l1 = list(map(int,input().split()))
l2 = list(map(int,input().split()))
print(f(l1,l2))
