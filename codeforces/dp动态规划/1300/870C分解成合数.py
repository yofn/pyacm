#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/870/C
#需要打表? trick? 总是用4? #1e5, 1e9

[print(([-1]*4+[1,-1,1,-1,2,1,2,-1])[n]) if n<12 else print(n//4 if n%2==0 else n//4-1) for n in [int(input()) for _ in range(int(input()))]]
