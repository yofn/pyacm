#!/usr/bin/env python3
'''
https://codeforces.com/group/H9K9zY8tcT/contest/297852
最长等差数列?
要用二分搜索?
nl = [l[i]-l[i-1] for i in range(1,n)]
n  = len(nl)
实际是一个图的问题? 广度优先搜索?
看题解!
[print(*l2[i*n:(i+1)*n]) for i in range(n)]
l2 = ['-']*(n*n)  #l2[i*n+j]=k so that v[k]=v[j]+(v[j]-v[i]), v[i]<v[j]<v[k]
#57上面超内存!
内存和时间有点超!
'''

def f(v):
    v.sort()
    n   = len(v)
    mx  = 0
    d2  = [0]*(n*n)
    for j in range(1,n-1):
        jj = (v[j]<<1)
        i  = j-1
        k  = j+1
        while k<n and i>=0:
            ik = v[i]+v[k]
            if  ik==jj:
                d2[i*n+j] = k
                i -= 1
                k += 1
            elif ik>jj:
                i -= 1
            else:
                k += 1
    for ij in range(n*n):
        ck  = 0
        while d2[ij]>0:
            k      = d2[ij]
            d2[ij] = -1
            ij     = (ij%n)*n+k
            ck    += 1     #how many k: i,j,k1,k2,...
        if ck>mx:
            mx=ck
    return mx+2

_ = int(input())    #5000. O(N^2) is acceptable
l = list(map(int,input().split()))  #1e9
print(f(l))

