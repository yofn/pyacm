#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/835/A

s,v1,v2,t1,t2 = list(map(int,input().split()))
l1 = (t1<<1) + s*v1
l2 = (t2<<1) + s*v2
if   l1==l2:
    print('Friendship')
elif l1<l2:
    print('First')
else:
    print('Second')

