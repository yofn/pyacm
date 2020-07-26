#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1311/A
# Choose any positive  odd integer x (x>0) and replace a with a+x;
# choose any positive even integer y (y>0) and replace a with a−y.

t = int(input())
for _ in range(t):
    a,b = list(map(int,input().split()))
    if a==b:
        print(0)
    elif b>a:
        print(2 if (b-a)%2==0 else 1)
    else:
        print(1 if (b-a)%2==0 else 2)

