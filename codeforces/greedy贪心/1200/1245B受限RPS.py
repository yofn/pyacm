#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/1245/B
#注意看赢的次数,所以谨慎选择去平或输!

wd  = {'R':'P','P':'S','S':'R'}
ld  = {'R':'S','P':'R','S':'P'} 
tc  = int(input())
for i in range(tc):
    n       = int(input())
    a,b,c   = list(map(int,input().split()))
    ad      = {'R':a,'P':b,'S':c}   #a's abc
    bd      = {'R':0,'P':0,'S':0}   #b's abc(from bseq)
    bseq    = input()
    for k in bseq:
        bd[k] += 1  #cnt b cases
    ald     = {k:max(0,ad[k]-bd[ld[k]]) for k in bd}    # number of a-lose for each case
    if sum(ald.values()) > n//2:    #a lose > n//2
        print('NO')
        continue
    print('YES')
    aseq    = []
    for k in bseq:
        w   = wd[k]
        if  ad[w]  > 0:
            aseq.append(w)
            ad[w] -= 1
            continue
        x   = k if ald[k]>0 else ld[k]
        aseq.append(x)
        ad[x] -= 1
        ald[x]-= 1
    print(''.join(aseq))

