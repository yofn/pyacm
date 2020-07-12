#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/1360/E
#判断射击结果图是真还是假!
#注意confidence的传递次序.
#从边界做bfs? 或者记忆化搜索DP? 哪个比较高效?
#从右下角开始斜着扫描也可以?

t = int(input())        #1000
for _ in range(t):
    n   = int(input())  #50
    s   = [[int(c) for c in input()] for i in range(n)]
    t   = [0]*(n*n)
    ok  = True
    for sij in range(2*n-2,-1,-1):
        if not ok:
            break
        il  = max(0,sij-n-1)
        ir  = min(n-1,sij)
        for i in range(il,ir+1):
            j = sij-i
            if j<0 or j>=n or s[i][j]==0:  #DON'T CARE!
                continue
            ii = i*n + j
            if i==n-1 or j==n-1 or t[ii+n]==1 or t[ii+1]==1: #trust propagate!
                t[ii] = 1
            else:
                ok = False
                break
    print('YES' if ok else 'NO')

