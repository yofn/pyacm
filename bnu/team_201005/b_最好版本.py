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
    [print([(t1[i][c],t2[i][c]) for c in range(tc[i])]) for i in range(n)]
    f2(n,t1,t2,tc)
def f2(n,t1,t2,tc):
    l   = ['-']*(n*n)
    for i in range(n):
        for c in range(tc[i]):
            l[i*n+t1[i][c]]=t2[i][c]
    [print(*l[i*n:(i+1)*n]) for i in range(n)]
还是之前的表现最好..https://codeforces.com/group/H9K9zY8tcT/contest/297852/submission/94764379
字典就是最好的版本?
'''

def f(v):
    n  = len(v)
    mx = 0
    d2 = {}
    for j in range(n):
        jj = (v[j]<<1)
        i  = j-1
        k  = j+1
        while k<n and i>=0:
            ik = v[i]+v[k]
            if ik==jj:
                d2[i*n+j] = k
            i -= 1 if ik>=jj else 0
            k += 1 if ik<=jj else 0
    for ij in sorted(d2.keys()):
        ck  = 0
        while ij in d2:
            ij  = (ij%n)*n+d2[ij]
            ck += 1     #how many k: i,j,k1,k2,...
        if ck>mx:
            mx=ck
    return mx+2
 
_ = int(input())    #5000. O(N^2) is acceptable
l = sorted(list(map(int,input().split())))  #1e9
print(f(l))
