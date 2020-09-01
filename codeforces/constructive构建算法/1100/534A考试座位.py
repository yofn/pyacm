#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/534/A

def f(n):
    l  = [None,[[1],[1]], [[1],[1]], [[2],[1,3]]]
    if n<4:
        return l[n]
    ol = list(range(1,n+1,2))
    ol.reverse()
    el = list(range(2,n+1,2))
    el.reverse()
    return [[n],ol+el]  # ...-3-1-(2k)-(2k-2)-...-2

[print(*r) for r in f(int(input()))]
