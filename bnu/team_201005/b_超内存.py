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
'''

def f(v):
    n  = len(v)
    mx = 0
    l2 = ['-']*(n*n)  #l2[i*n+j]=k so that v[k]=v[j]+(v[j]-v[i]), v[i]<v[j]<v[k]
    pl = []
    for j in range(n):
        i  = j-1
        k  = j+1
        jj = (v[j]<<1)
        while k<n and i>=0:
            ik = v[i]+v[k]
            if   ik>jj:
                i -= 1
            elif ik<jj:
                k += 1
            else:
                ij = i*n+j
                l2[ij] = k
                pl.append(ij)
                i -= 1
                k += 1
    pl.sort()
    for ij in pl:
        ck  = 0
        while type(l2[ij])==int:
            ij  = (ij%n)*n+l2[ij]
            ck += 1     #how many k: i,j,k1,k2,...
        if ck>mx:
            mx=ck
    return mx+2

_ = int(input())    #5000. O(N^2) is acceptable
l = sorted(list(map(int,input().split())))  #1e9
print(f(l))

