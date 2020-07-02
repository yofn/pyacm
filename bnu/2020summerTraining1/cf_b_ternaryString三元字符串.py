#!/usr/bin/env python3

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
ll = []
for i in range(n):
    s = input()
    ll.append(s)
for s in ll:
    print(tstring(s))


