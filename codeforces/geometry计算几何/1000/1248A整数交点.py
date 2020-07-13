#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/1248/A
#奇偶相同则有IIP,否则没有..

def iip(pl,ql): # interger intersection points
    evns = lambda l: sum([i%2==0 for i in l])
    odds = lambda l: sum([i%2==1 for i in l])
    return evns(pl)*evns(ql)+odds(pl)*odds(ql)

t   = int(input())
for i in range(t):
    _   = input()
    pl  = list(map(int,input().split()))
    _   = input()
    ql  = list(map(int,input().split()))
    print(iip(pl,ql))
