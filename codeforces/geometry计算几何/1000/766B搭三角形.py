#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/766/B

def maket(l):
    l.sort()
    for i in range(len(l)-2):   #not limit to 4 case
        if l[i]+l[i+1]>l[i+2]:
            return 'YES'
    return 'NO'

_ = input()
l = list(map(int,input().split()))
print(maket(l))
