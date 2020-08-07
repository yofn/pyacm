#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/552/A

n  =  int(input())
ll = [list(map(int,input().split())) for _ in range(n)]
print(sum([(l[2]-l[0]+1)*(l[3]-l[1]+1) for l in ll]))
