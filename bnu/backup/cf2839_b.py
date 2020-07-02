#!/usr/bin/env python3
def abbc(s,start):
    i = start
    a = s[i]
    while s[i]==a:
        i += 1
        if i>=len(s):   
            return None     #CASE aaaaaaa
    ai = i-1
    b  = s[i]
    while s[i]==b:
        i += 1
        if i>=len(s):
            return None     #CASE abbbbb
    if s[i]==a: return i-1  #CASE abba
    return s[ai:i+1]        #CASE abbc

def tstring(s):
    counts = [s.count('1'),s.count('2'),s.count('3')]
    if 0 in counts:
        return 0
    minlen = len(s)
    i = 0
    while i<minlen-2: 
        c = abbc(s,i)
        if c is None:
            break
        if type(c) is int:
            i = c
            continue
        if len(c)<minlen:
            minlen = len(c)
        i+=1
    return minlen


'''
n  = int(input())
ll = []
for i in range(n):
    s = input()
    ll.append(s)
for s in ll:
    print(tstring(s))
'''

