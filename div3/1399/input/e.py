#!/usr/bin/python3
#https://codeforces.com/contest/1462/problem/A

def f(ll):
    n     = len(ll)
    nl    = [0]*n
    i,l,r = 0,0,n-1
    while l<=r:
        nl[i]   = ll[l]
        if i+1 >= n:
            break
        nl[i+1] = ll[r]
        i += 2
        l += 1
        r -= 1
    return nl

T  = int(input())
for i in range(T):
    _ = input()
    l = list(map(int,input().split()))
    print(*f(l))
