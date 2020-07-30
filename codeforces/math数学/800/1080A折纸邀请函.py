#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1080/A

n,k = list(map(int,input().split()))
print((2*n+k-1)//k+(5*n+k-1)//k+(8*n+k-1)//k)
