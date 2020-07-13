#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/1047/B

ps = [list(map(int,input().split())) for _ in range(int(input()))]
print(max([p[0]+p[1] for p in ps]))

