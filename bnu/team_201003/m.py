#!/usr/bin/env python3

#https://codeforces.com/group/H9K9zY8tcT/contest/297617
#inflate by 2, so that 里面也有点!
#step1: 先inflate by 2! 用LUT(m)
#step2: 四边都要加边界!
#step2: 算#connected components! (BFS,DFS?)
# [print(s) for s in [''.join(map(str,l)) for l in ll]]

i2c = lambda i: chr(i+ord('a'))

def f(r,c,ll):
    # inflate and add boundary
    m  = {'/':['.','/'],'\\':['\\','.'],'.':['.','.']}
    ll = [['.'] + [m[ll[i>>1][j>>1]][(i+j)%2] for j in range(c<<1)] + ['.'] for i in range(r<<1)]
    rr = (r+1)<<1
    cc = (c+1)<<1
    ll = [['.']*cc] + ll + [['.']*cc]
    # count CC by dfs!
    vd = lambda p: p[0]>=0 and p[0]<rr and p[1]>=0 and p[1]<cc and ll[p[0]][p[1]]=='.'
    dr = [(0,1),(0,-1),(-1,0),(1,0)]
    k  = 0
    s  = [None]*(rr*cc)
    for i in range(rr):
        for j in range(cc):
            if ll[i][j]!='.':
                continue
            sp       = 0    #stack pointer, points to current stack head!
            s[sp]    = (i,j)
            ll[i][j] = i2c(k)   #mark for CC idx
            while sp>-1:
                p   = s[sp]
                sp -= 1
                for d in dr:
                    pp = (p[0]+d[0],p[1]+d[1])
                    if vd(pp):
                        sp   += 1
                        s[sp] = (pp[0],pp[1])
                        ll[pp[0]][pp[1]] = i2c(k) #mark for CC idx
            k += 1
    return k-1

r,c =  list(map(int,input().split()))   #both 1e5
l   = [list(input()) for _ in range(r)]
print(f(r,c,l))
