#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/665/C

s   = list(input())
for i in range(1,len(s)-1):
    if s[i]==s[i-1]:
        if   s[i-1]!='a' and s[i+1]!='a':
            s[i]='a'
        elif s[i-1]!='b' and s[i+1]!='b':
            s[i]='b'
        else:
            s[i]='c'
if len(s)>1 and s[-1]==s[-2]:
    s[-1] = 'a' if s[-2]=='b' else 'b'
print(''.join(s))
