#!/usr/bin/env python3

def apb(s):
    i = 0
    j = len(s)-1
    while i<j and s[i]==s[j]:
        i += 1
        j -= 1
    return s[:i]+s[j:]

def rebuild(s):
    n     = len(s)
    ss    = ['#']*(n*2+3)
    ss[0] = '$'
    for i in range(1,n+1):
        ss[i*2]=s[i]
    ss[-1]= 0 #for boundary condition
    return ss

def Manacher(s):
    n   = len(s)
    p   = [1]*n
    mx  = 0
    ans = 1
    for i in range(len(s)):
        p[i] = 1 if mx<=i else min(p[2*mi-i],mx-i)
        while s[i-p[i]]==s[i+p[i]]: p[i]+=1
        if p[i]+i>mx:
            mx=p[i]+i
            mi=i
        ans=max(ans,p[i]-1)
    return ans

def b(s):
    pass

def f(s):
    s1  = apb(s)
    s2  = a(s)
    s3  = b(s)
    ss = s1 if len(s1)>len(s2) else s2
    ss = ss if len(ss)>len(s3) else s3
    return ss

[print(f(input())) for _ in range(int(input()))] 

