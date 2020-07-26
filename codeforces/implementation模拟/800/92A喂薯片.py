#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/92/A
# 之前是模拟解; 现在尝试数学解..
import math
n,m = list(map(int,input().split()))    #50,1e4
cc  = (n*(n+1))//2
m   = m%cc
x   = int((math.sqrt((m<<3)+1)-1)/2)
print(m-(x*(x+1))//2)
