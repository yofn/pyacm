#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/1020/B
#寻找环.

def who(al,i):
    vl  = [False]*len(al)
    while vl[i] is False:
        vl[i]   = True
        i       = al[i]
    return i

n   = int(input())  #1000
al  = [0] + list(map(int,input().split()))  #al
print(*[who(al,i) for i in range(1,n+1)])
