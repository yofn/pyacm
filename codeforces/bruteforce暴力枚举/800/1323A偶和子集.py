#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1323/A

def evenSum(l):
    for i in range(len(l)):
        if l[i]%2==0:
            print(1)
            print(i+1)
            return
        if i>0:
            print(2)
            print(i,i+1)
            return
    print(-1)
    return
         
n  = int(input())
for i in range(n):
    _ = input()
    l = list(map(int,input().split())) #https://codeforces.com/blog/entry/71884
    evenSum(l)

