#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/1205/A
# work, 但有没有更好的?

def f(n):
    if n%2==0:
        return [['NO']]
    m = n//2
    s =  n*n   + m      #s or s+1
    p = (n<<1) + 3
    l = [1]*(n<<1) 
    for i in range(1,n,2):
        l[i] = i+3      #l[1]=4, l[3]=6
    for i in range(2,n,2):
        l[i] = p-l[i-1]
    for i in range(n,n<<1,2):
        l[i] = l[i-n]+1
    for i in range(n+1,n<<1,2):
        l[i] = l[i-n]-1
    return [['YES'],l]

n = int(input())
[print(*r) for r in f(n)]
