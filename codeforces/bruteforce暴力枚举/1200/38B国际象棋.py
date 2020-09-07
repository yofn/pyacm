#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/38/B
#http://www.learnchessrules.com/knights.htm
#http://www.learnchessrules.com/rooks.htm
#r+k, 再放一个knight, 相互打不到!
#骑士是相互的,所以只要k2 not in r和k1的攻击范围就行
#还要考虑边界,所以用dx太麻烦,不如直接来暴力的!
#if ix==rx or iy==ry or (dx<1 and dy<2) or (dy<1 or dx<2) or (dx==2 and dy==1) or (dx==1 and dy==2):
#注意: 还要考虑k2不能攻击r的条件!!!
#规则搞错,绿点是跳过,不是攻击范围!!!
'''
    b[rx*8+ry]='R'
    b[kx*8+ky]='K'
    for i in range(8):
        print(b[i<<3:(i+1)<<3])
'''

ab = lambda x: -x if x<0 else x

def f(l):
    s       = "abcdefgh"
    r,k     = l
    rx,kx   = s.index(r[0]), s.index(k[0])
    ry,ky   = int(r[1])-1,   int(k[1])-1
    b       = [1]*64    #1=valid; 0=invalid
    for i in range(64):
        ix,iy = i//8,i%8
        dx,dy = ab(ix-kx),ab(iy-ky)
        ex,ey = ab(ix-rx),ab(iy-ry)
        if ix==rx or iy==ry or dx+dy==0 or (dx<3 and dy<3 and dx+dy==3) or (ex<3 and ey<3 and ex+ey==3):
            b[i]=0
    return sum(b)

l  = [input() for _ in range(2)]
print(f(l))
