#!/usr/bin/env python3

def f(h,l,p):
    #print(h,p,l)
    nc = len(l)
    for i in range(nc):
        l[i] -= p[1][i]
        if l[i]<0: return ['NO']
    v2s = [0]*(nc-1)    #quota of small
    v2b = [0]*(nc-1)    #quota of big
    for i in range(nc-1):
        v2s[i]   = l[i]     #use all small left!
        p[2][i] -= v2s[i]
        if p[2][i]<=0:
            continue        #if covered, continue to next (i,i+1)
        v2b[i]   = p[2][i]
        l[i+1]  -= v2b[i]
        if l[i+1]<0: return ['NO']
    rl = ['YES']
    for i in history:
        if i>=0:
            rl.append(i2s[i])
            continue
        i = -i-1    #make -1 to 0, -2 to 1, ..
        if v2s[i]>0:
            rl.append(i2s[i])
            v2s[i] -= 1
        else:
            rl.append(i2s[i+1])
    return rl 

history = []
s2i = {'S':0,'M':1,'L':2,'XL':3,'XXL':4,'XXXL':5}
i2s = ['S','M','L','XL','XXL','XXXL']
p   = [None,[0]*6,[0]*5]
l   = list(map(int,input().split()))
n   = int(input())
for _ in range(n):
    s = input().split(',')
    i = s2i[s[0]]
    history.append(i if len(s)==1 else -i-1)   #careful 0,1 should record -1
    p[len(s)][i] += 1
[print(s) for s in f(history,l,p)]

