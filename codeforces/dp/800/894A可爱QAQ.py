#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/894/A

s   = input()
cnt = [0,0,0]  #0=Q, 1=QA, 2=QAQ
for c in s:
    if c == 'Q':
        cnt[0] += 1
        cnt[2] += cnt[1]
    if c == 'A':
        cnt[1] += cnt[0]
print(cnt[2])
