#!/usr/bin/python3
'''
要通过记忆化搜索(DP)来降低每个testcase内的计算量!?
预处理0-1e9的list能否节省时间? 1e9=1G!
'''

#@profile
def f(x,y):
    l   = [None]*40
    nx  = 0
    while x>0:
        l[nx]  = (1 & x, 1 & y)
        x    >>= 1
        y    >>= 1
        nx    += 1
    ybok    = l[nx-1][1]
    hhp     = not ybok
    c       = [1,1,1] if ybok else [0,1,0]  #[bb,bh,hb]
    w       = [0,1,1] if ybok else [0,0,0]
    for i in range(nx-2,-1,-1):
        xi,yi   = l[i]
        nx2b    = hhp and xi
        ny2b    = hhp and yi
        nxy2b   = hhp and xi and yi
        ybok    = ybok or yi
        if ybok:
            c[0]= c[0]*3 + (xi*c[2]+yi*c[1])*2 + nxy2b #bb = bb + bh + hb + hh
            w[0]= w[0]*3 + (xi*w[2]+yi*w[1])*2 + nxy2b*i + c[0]-1  #don't 00
            c[2]= c[2]*(2-xi) + ny2b
            w[2]= w[2]*(2-xi) + ny2b*i + c[2]
        c[1]    = c[1]*(2-yi) + nx2b
        w[1]    = w[1]*(2-yi) + nx2b*i + c[1] - (not ybok)
        hhp     = hhp and (xi+yi<2)
    return (sum(w)+(hhp*nx))%1000000007

T   = int(input())  #t=1e5
for _ in range(T):  #60*60=3600
    x,y = map(int,input().split())
    if x==0 and y==0:
        print(0)
        continue
    print(f(x,y) if x>y else f(y,x))
