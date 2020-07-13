#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/270/A

fok = lambda a: 360%(180-a)==0 and 360//(180-a)>2
[print('YES' if fok(int(input())) else 'NO') for _ in range(int(input()))]
