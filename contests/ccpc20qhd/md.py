#!/usr/bin/env python3
#ccpc20qhd-fd(female-d)

def f(n,l):
    dm = [True]*((n+2)*(n+2))   # danger map
    for x,y,d in l:
        xr = range(x,n+2) if (d==1 or d==4) else range(x+1)
        yr = range(y,n+2) if (d==1 or d==2) else range(y+1) 
        for i in xr:
            for j in yr:
                dm[i*(n+2)+j] = False
    return 'No' if sum(dm)>0 else 'Yes'

t = int(input())
for i in range(t):
    n   =  int(input())
    l   = [list(map(int,input().split())) for _ in range(n)]
    print('Case #%d: %s'%((i+1), f(n,l)))

