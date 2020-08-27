#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1165/A
#   c  = sum(l2[:y])
#   c += 1 if l2[y]==0 else 0
#   c += sum(l2[y+1:x])

def f(l1,l2):
    n,x,y = l1
    l2.reverse()
    l2[y] = [1,0][l2[y]]    #1->0,0->1
    return sum(l2[:x])

l1 = list(map(int,input().split()))
l2 = list(map(int,list(input())))
print(f(l1,l2))
