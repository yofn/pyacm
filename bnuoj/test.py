#!/usr/bin/env python3

def f(ll):
    return [sum(l) for l in ll]

n = int(input())
l = [list(map(int,input().split())) for _ in range(n)]
[print(r) for r in f(l)]
