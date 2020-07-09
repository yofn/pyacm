#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1352/A

def split(n):
    l = []
    i = 1
    while n>0:
        if n%10 != 0:
            l.append(i*(n%10))
        n = n//10
        i = i*10
    print(len(l))
    print(*l)

[split(int(input())) for i in range(int(input()))]
     
