#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/732/A

k,r = list(map(int,input().split()))
l   = [ [0],
        [1,2,3,4,5,6,7,8,9,0],
        [2,4,6,8,0],
        [3,6,9,2,5,8,1,4,7,0],
        [4,8,2,6,0],
        [5,0],
        [6,2,8,4,0],
        [7,4,1,8,5,2,9,6,3,0],
        [8,6,4,2,0],
        [9,8,7,6,5,4,3,2,1,0]]
print(min(l[k%10].index(r)+1, l[k%10].index(0)+1))
