#!/usr/bin/env python3
# brute-force or 01 backpack!
 
pl = [648,328,198,88,28, 6,1]
rl = [388,198,128,58,28,18,8]
 
def f(n):
    awards = [0]
    yuan   = [n]
    for i in range(7):
        na = []
        ny = []
        for j in range(len(yuan)): 
            if yuan[j]>=pl[i]:
                na.append(awards[j]+rl[i])
                ny.append(yuan[j]-pl[i])
        awards = awards + na
        yuan   = yuan   + ny
    return max(awards) + n*10
 
n = int(input())
print(f(n))
