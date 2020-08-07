#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/608/A

def f(ll,s):
    tl = [l[0]+l[1] for l in ll]
    tl.append(s)
    return max(tl)

n,s =  list(map(int,input().split()))
ll  = [list(map(int,input().split())) for _ in range(n)]
print(f(ll,s))
