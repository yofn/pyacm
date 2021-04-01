#!/usr/bin/python3
#https://codeforces.com/contest/1426/problem/F

def f(s):
    t = [1]+[0]*3 #_, 'a','ab','abc' respectively
    for c in s:
        if   c=='a':
            t[1]+=t[0]
        elif c=='b':
            t[2]+=t[1]
        elif c=='c':
            t[3]+=t[2]
        else:
            t[3] = t[3]*3+t[2]
            t[2] = t[2]*3+t[1]
            t[1] = t[1]*3+t[0]
            t[0] = t[0]*3
    return t[3]%1000000007

_ = input()
s = input()
print(f(s))
