#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/370/A

def f(l):
    ab = lambda x: x if x>0 else -x
    r1,c1,r2,c2 = l
    r = 1 if (r1==r2 or c1==c2) else 2
    b = (1 if (r2-r1==c1-c2 or r2-r1==c2-c1) else 2) if (r1+r2+c1+c2)%2==0 else 0 
    k = max(ab(r2-r1),ab(c2-c1))
    return [r,b,k]

l = list(map(int,input().split()))
print(*f(l))

