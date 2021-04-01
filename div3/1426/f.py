#!/usr/bin/python3
#https://codeforces.com/contest/1426/problem/F

def f(s):
    _,a,ab,abc = 1,0,0,0
    for c in s:
        if   c=='a':
            a   += _
        elif c=='b':
            ab  += a
        elif c=='c':
            abc += ab
        else:
            abc *= 3
            abc += ab
            ab  *= 3
            ab  += a
            a   *= 3
            a   += _
            _   *= 3
    return abc%1000000007

_ = input()
s = input()
print(f(s))
