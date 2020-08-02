#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1291/A

def f(s):
    i = len(s)-1
    l = []
    while i>=0 and len(l)<2:
        if int(s[i])%2==1:
            l.append(s[i])
        i -= 1
    if len(l)<2:
        return -1
    l.reverse()
    return ''.join(l)

t  = int(input())
for _ in range(t):
    _   = input()
    s   = input()
    print(f(s))

