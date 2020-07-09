#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/546/A

k,n,w = list(map(int,input().split()))
print( max(0,((w*(w+1))//2) * k -n) )

