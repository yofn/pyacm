#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/1354/B
#找到最短连续子串包含123.
#规律: 一定是abbbbc形式..
#recent含义是1/2/3最近出现的位置..

def tstring(s):
    counts = [s.count('1'),s.count('2'),s.count('3')]
    if 0 in counts:
        return 0
    minlen = len(s)
    recent = [None,None,None]
    for i in range(len(s)):
        n = int(s[i])-1
        recent[n] = i
        if None in recent:
            continue
        l = min(recent)
        minlen = min(minlen,i-l+1)
    return minlen

n  = int(input())
[print(r) for r in [tstring(input()) for i in range(n)]]
