#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/1324/C
#青蛙跳,左和右,不超D,最小D?
#寻找最大的最近R间隔? 跳到L永远是错误选择?

def minD(s):    #2e5, sum<2e5; O(n) is enough!?
    p =-1
    m = 0
    s = s + 'R' #trick
    for i in range(len(s)):
        if s[i]=='R':
            if i-p>m:
                m=i-p
            p = i
    return m

t   = int(input())  #1e4
[print(minD(input())) for _ in range(t)]
