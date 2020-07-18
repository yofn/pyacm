#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/1292/A
#由于toggle,dsu实现的话还要支持split?
#每次q必须低于O(n)! 每次查询都走一遍是不行的!
#分成两个情况:
# 1. unblock->block的情况: 判断一下block的位置和周围位置状态
# 2. unblock action: 将unblock块和三个邻居分别union, 然后再看(1,1)和(2,n)是否联通.
# 但是问题是要为case 2维护dsu; 所以case1也要用dsu来做才行....
# 1. block action, 应如何维护dsu??
# 还有一个问题是2xn是用两个list,一个大list还是如何表示? 还是两个dsu?
# 还是太复杂了,感觉有更简单的方法,可能被dsu带歪了..
# NOTE: no dsu used!
# https://codeforces.com/blog/entry/73051
# https://www.youtube.com/watch?v=mhrvlor1qH0
# https://codeforces.com/contest/1292/submission/69151636
# 注意对bad的定义, 我们的定义是走不到的地方从左边走$完全$走不到的列! 如果能走到一行,也算good,不算bad!
# https://codeforces.com/contest/1292/submission/69151636 实现更简洁,建议参考! NOTE
# 修改下实现..using bad neighbor! 用bad neighbor比bad columns方便的多~~~
# 走了两个弯路: 1.dsu; 2.bad-columns; 最后才了解bad neighbor这个简单解法!.

n,q =  list(map(int,input().split()))    #1e5,1e5
tl  = [list(map(int,input().split())) for _ in range(q)]
gd  = [[False]*n, [False]*n]    #easier to count blocks
bn  = 0 #bad neighbor
for t in tl:
    r,c      = t[0]-1,t[1]-1
    bnc      = sum(gd[1 if r==0 else 0][max(0,c-1):min(c+2,n)])
    gd[r][c] = not gd[r][c]
    bn      += bnc if gd[r][c] else -bnc
    print('Yes' if bn==0 else 'No')

