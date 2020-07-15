#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/217/A
#只能直着滑..看需要加多少个点,才能保证所有点是连通的(直着..)
#n<100..
#xy<1000,可以用暴力! 但现在不想用暴力,想尝试dsu
#构建dsu,然后检查有n个,则需要加n-1个点..将dsu变为1
#这个特殊并查集的范围就由覆盖的x和y整数描述了..
#优化/实现的可能性不少,时间关系暂不考虑

def need(xyl):
    dsul    = []    #use list to repsent dsu
    for x,y in xyl:  #100
        ux,uy   = None,None     #x and y's union
        for i in range(len(dsul)):
            ds  = dsul[i]
            if x in ds[0]:      #found x in ith dsu
                ds[1].add(y)
                ux  = i
                continue
            if y in ds[1]:
                ds[0].add(x)
                uy  = i
                continue
        if ux is None and uy is None:   #found 0, create new dsu
            dsul.append((set([x]),set([y])))
        elif ux is None or uy is None:  #found 1, no merge, do nothing!
            pass
        else:                           #found 2, merge!
            dsul[ux] = (dsul[ux][0].union(dsul[uy][0]),dsul[ux][1].union(dsul[uy][1]))
            dsul     = dsul[:uy]+dsul[uy+1:]
    return len(dsul)-1

xyl = [list(map(int,input().split())) for _ in range(int(input()))] #100;1000(xy)
print(need(xyl))

