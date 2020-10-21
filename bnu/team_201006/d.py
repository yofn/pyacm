#!/usr/bin/env python3
#https://codeforces.com/group/H9K9zY8tcT/contest/297264/problem/D

'''
#[print(*l) for l in gt]
#线下打表?
gt = [[i] for i in range(11)]
for i in range(2,11):
    c  = i
    ii = i 
    while c<1e9:
        ii *= i
        c  += ii
        gt[i].append(c)
[print(l) for l in gt]
考虑一次while的解决方案
'''


q = int(input())        #1e5
for _ in range(q):
    k   = int(input())  #10
    x   = int(input())  #1e9
    s   = []
    while x>0:         #optimize this?
        s.append(10-k+(x-1)%k)
        x   = (x-1)//k
    s.reverse()
    print(''.join(map(str,s)))

