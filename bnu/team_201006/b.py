#!/usr/bin/env python3
#https://codeforces.com/group/H9K9zY8tcT/contest/297264/problem/B
#利用奇偶性?
#每次移除奇数个节点..所以就看原来n是奇数还是偶数


q = int(input())        #5e4
for _ in range(q):
    n = int(input())    #5e4 (summed)
    l = [input() for _ in range(n-1)]
    print('Alice' if n%2>0 else 'Bob')
