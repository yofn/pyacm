#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/876/A
# 最短路径,DP?
#       R       | O                 |   E               |   min
# 1     0       | NA                |   NA              |   0
# 2    NA       | a                 |   b               |   min(a,b)
# 3  2a/2b      | b+c               |   a+c             |   min(2a,2b,b+c,a+c)
# 4  a+b+c      | (2a/2b)+a,a+2c    |(2a/2b)+b,b+2c     |   min(a+b+c,3a,3b,2a+b,2b+a,b+2c,a+2c)
# 5  4a/4b      | 2a+b+c....              |   min(4a,4b,2a+b+c,2b+a+c)
# 两种可能:
# 1. min(a,b,c)=min(a,b) 这时总是在这个是(n-1)*a或(n-1)*b的距离
# 2. min(a,b,c)=c        这时除了2特殊之外,其他都是min(a,b)+(n-2)*c

def f(l,n):
    a,b,c = l
    return (n-2)*c+min(a,b) if (n>2 and min(l)==c) else (n-1)*min(a,b)

n  = int(input())
l  = [int(input()) for _ in range(3)]
print(f(l,n))

