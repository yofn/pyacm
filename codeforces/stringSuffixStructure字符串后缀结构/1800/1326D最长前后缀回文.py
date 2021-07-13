#!/usr/bin/env python3

#from sys import stdout 
#import io,os
#input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline

def bitrim(s):
    i = 0
    j = len(s)-1
    while i<j and s[i]==s[j]:
        i += 1
        j -= 1
    return i,s[i:j+1]

def rebuild(s):
    n     = len(s)
    ss    = ['#']*(n*2+3)
    ss[0] = '$'
    for i in range(1,n+1):
        ss[i*2]=s[i-1]
    ss[-1]= 0 #for boundary condition
    return ss

def Manacher(s):
    n   = len(s)-1  #leave 0 out!
    p   = [1]*n
    mx  = 0
    hp  = 1
    tp  = 1
    for i in range(n):
        p[i] = 1 if mx<=i else min(p[mx-i+ml],mx-i)
        while s[i-p[i]]==s[i+p[i]]: p[i]+=1
        if i+p[i]>mx:
            mx=i+p[i]
            ml=i-p[i]
        if ml==0: hp=max(hp,p[i]-1)
        if mx==n: tp=max(tp,p[i]-1)
    return [hp,tp]

def f(s):
    bi,ts = bitrim(s) #bi and trimmed
    hp,tp = Manacher(rebuild(ts))
    ps    = ts[:hp] if hp>tp else ts[-tp:]
    return s[:bi]+ps+(s[-bi:] if bi>0 else '')

#msg = '\n'.join([f(str(input())) for _ in range(int(input()))])
#stdout.write(msg)
[print(f(input())) for _ in range(int(input()))]
#combine and print
