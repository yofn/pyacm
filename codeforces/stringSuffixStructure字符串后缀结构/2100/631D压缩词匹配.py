#!/usr/bin/env python3

def cal_last(s):
    n    = len(s)
    last = [-1]*(n+1)
    i,j  = 0,-1
    while i<n:
        while j!=-1 and s[i]!=s[j]:
            j=last[j]
        i,j = i+1,j+1
        last[i] = j
    return last

def kmp(p,t,last):
    m = len(p)
    n = len(t)
    i = j = 0
    rl = []
    while i<n:
        while j!=-1 and t[i]!=p[j]:
            j=last[j]
        i,j = i+1,j+1
        if j>=m:
            rl.append(i)
            j=last[j]
    return rl

def solve1(p,t):
    pn,pc = p[0]
    return sum([tn-pn+1 for tn,tc in t if tn>=pn and tc==pc])

def solve2(p,t):
    return sum([t[i][0]>=p[0][0] and t[i][1]==p[0][1] and t[i+1][0]>=p[1][0] and t[i+1][1]==p[1][1] for i in range(len(t)-1)])

def compact(s):
    t = [[int(s[0][:-2]),s[0][-1]]]
    for i in range(1,len(s)):
        n = int(s[i][:-2])
        c = s[i][-1]
        if c == t[-1][-1]:
            t[-1][0] += n
        else:
            t.append([n,c])
    return t

def f(p,t):
    tt,pp = compact(t),compact(p)
    if len(pp)==1:
        return solve1(pp,tt)
    if len(pp)==2:
        return solve2(pp,tt)
    last = cal_last(pp[1:-1])
    ml   = kmp(pp[1:-1],tt,last)
    x    = len(pp)-2
    n    = len(tt)
    return sum([i-x>0 and tt[i-x-1][0]>=pp[0][0] and tt[i-x-1][1]==pp[0][1] and i<n and tt[i][0]>=pp[-1][0] and tt[i][1]==pp[-1][1] for i in ml])

_ = input()
t = input().split()
p = input().split()
print(f(p,t))

