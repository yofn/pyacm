#!/usr/bin/env python3

#https://codeforces.com/group/H9K9zY8tcT/contest/297852
#字典序和数值序的结合..

def mml(s):  #make my list from string
    isDigit = lambda c: c>='0' and c<='9'
    dl = [isDigit(s[0])]
    nl = [int(s[0]) if dl[0] else s[0]]
    for c in s[1:]:
        if isDigit(c):
            if dl[-1]:
                nl[-1] = nl[-1]*10 + int(c)
            else:
                dl.append(True)
                nl.append(int(c))
        else:
            dl.append(False)
            nl.append(c)
    return nl

def mcmp(r,s):
    i  = 0
    nr = len(r)
    ns = len(s)
    while True:
        if i==nr and i==ns:
            return '+'
        if i==nr:
            return '+'
        if i==ns:
            return '-'
        if type(r[i])==type(s[i]):
            if r[i]==s[i]:
                i += 1
                continue
            return '+' if r[i]<s[i] else '-'
        return '+' if type(r[i])==int else '-'

def f(l):
    nl = list(map(mml,l))
    rl = [mcmp(nl[0],s) for s in nl[1:]]
    return rl

t = int(input())    #1000
l = [input() for _ in range(t+1)]
[print(r) for r in f(l)]


