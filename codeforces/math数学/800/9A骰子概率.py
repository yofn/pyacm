#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/9/A

al  = list(map(int,input().split()))
wp  = 7-max(al)
ll  = [None,'1/6','1/3','1/2','2/3','5/6','1/1']
print(ll[wp])

