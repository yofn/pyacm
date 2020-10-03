#!/usr/bin/env python3

#https://codeforces.com/group/H9K9zY8tcT/contest/297258/problem/H
#贪心方法

def f(l1,l2):
    n,c,b = l1
    s   = ['0']*n
    bl  = [False]*n
    for i in l2:
        bl[i-1] = True
    p   = n-2
    cc  = 0
    while True:
        if cc==c:
            return s
        if cc==c-1:
            s[0]='1'
            return s
        if bl[p]:
            p -= 1
            continue
        s[p] = '1'
        cc  += 2
        p   -= 2

l1 = list(map(int,input().split()))
l2 = list(map(int,input().split()))
print(''.join(f(l1,l2)))
