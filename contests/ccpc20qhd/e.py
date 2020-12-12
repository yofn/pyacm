#!/usr/bin/env python3
#ccpc20qhd-e
'''
还有更好的,扫描方法!
'''

def f(n,p,l):
    nl = [0]*(n<<1)
    for i in range(n):
        ii       = i<<1
        nl[ii]   = (l[i][0],i)
        nl[ii+1] = (l[i][1],i)
    nl.sort(key=lambda t:t[0],reverse=True)
    pi = 0
    cs = [0]*n
    cl = []
    tc = 0
    for i in range(n):  #0~(n-1); n~(2n-1)
        pp = (nl[i][0]*p)/100
        if i>0 and nl[i-1][0]>nl[i][0]:
            si = nl[i-1][1]
            cs[si] -= 1
            if cs[si]==0:
                tc -= 1
        while pi<(n<<1) and nl[pi][0]>=pp:
            si = nl[pi][1]  #student index
            if cs[si]==0:
                tc += 1
            cs[si] += 1
            pi     += 1
        cl.append(tc)
    return max(cl) 

t = int(input())
for i in range(t):
    n,p =  list(map(int,input().split()))
    l   = [list(map(int,input().split())) for _ in range(n)]
    print('Case #%d: %s'%((i+1), f(n,p,l)))

