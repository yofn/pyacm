#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1187/A
# 要多少个蛋才能确保既有stick,又有toy?
# 两个都有的? (t+s-n) 
# 只有toy, 没有stick的蛋有几个?  t-(t+s-n)=n-s
# 只有stick, 没有toy的蛋有几个?  s-(t+s-n)=n-t

def f(l):
    n,s,t = l
    return max(n-s,n-t)+1

t  = int(input())
for _ in range(t):
    l  = list(map(int,input().split()))
    print(f(l))

