#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/120/C
# input.txt
# output.txt
# n罐蜂蜜, 每次喝k; 每次拿最多的, 如果少于k或喝过三次, 将蜂蜜给piglet
# 问: piglet得到多少蜂蜜


nk,al   = [line.rstrip() for line in open('./input.txt')]
n,k     = list(map(int,nk.split()))
al      = list(map(int,al.split()))
s       = sum([max(ai-k*3,ai%k) for ai in al])
with open('./output.txt','w') as f:
    f.write('%s'%s)
