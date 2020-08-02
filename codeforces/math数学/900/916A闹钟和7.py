#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/916/A
# x, hh, mm
# 幸运数字7? hh:mm -x 几次可以得到幸运数字7?
# 因为x<=60,所以躲不过小时..
# 错误逻辑:
#   h7  = [7,17]
#   m7  = [7,17,27,37,47,57]
#   t7  = [h*60+m for h in h7 for m in m7]

def f(l,x):
    tx  = l[0]*60+l[1]
    c   = 0
    while True:
        if (tx%60)%10==7 or ((tx//60)%10==7):
            return c
        tx -= x
        c  += 1
        if tx<0:
            tx += 1440  #60*24

x  = int(input())
l  = list(map(int,input().split()))
print(f(l,x))

