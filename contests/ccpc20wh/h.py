#!/usr/bin/env python3
#ccpc20wh
'''
1 差分思想
2 结束的时候要清算! 维护哪些人还在组里?? ....   
3 自己发的言不算消息!
'''

n,m,s  = map(int,input().split()) # n=#groups; m=#students; s=#events..
gpmsgs = [0]*(n+1)
gpmber = [set() for i in range(n+2)]
person = [0]*(m+1)
for i in range(s):
    t,x,y = map(int,input().split())
    if   t==1:  #join
        person[x] -= gpmsgs[y]
        gpmber[y].add(x)
    elif t==2:  #quit
        person[x] += gpmsgs[y]
        gpmber[y].discard(x)
    else:       #msgs
        person[x] -= 1
        gpmsgs[y] += 1
for y in range(1,n+1):
    for x in gpmber[y]: 
        person[x] += gpmsgs[y]

[print(person[x]) for x in range(1,m+1)]
