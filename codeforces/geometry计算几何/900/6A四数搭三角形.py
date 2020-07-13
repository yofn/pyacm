#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/6/A

def maket(l):
    l.sort()
    bad = 'IMPOSSIBLE'
    for i in range(len(l)-2):   #not limit to 4 case
        if l[i]+l[i+1]>l[i+2]:
            return 'TRIANGLE'
        if l[i]+l[i+1]==l[i+2]: 
            bad = 'SEGMENT'
    return bad

l = list(map(int,input().split()))
print(maket(l))
