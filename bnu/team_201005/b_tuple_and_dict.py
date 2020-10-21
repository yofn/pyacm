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
https://codeforces.com/group/H9K9zY8tcT/contest/297852/submission/94813275
https://codeforces.com/group/H9K9zY8tcT/contest/297852/submission/94813332 (PyPy更快)
这个实现还是节省空间些,但是需要优化下链条过程的问题!!!
暂时放弃优化..
加入字典..但那样空间又不够了..
'''
def f2(n,t1,t2,tc):
    l   = ['-']*(n*n)
    for i in range(n):
        for c in range(tc[i]):
            l[i*n+t1[i][c]]=t2[i][c]
    [print(*l[i*n:(i+1)*n]) for i in range(n)]

def f(v):
    n   = len(v)
    t1  = [[] for _ in range(n)]
    t2  = [[] for _ in range(n)]
    tv  = [[] for _ in range(n)]    #记录是否visit
    tc  = [0]*n
    tvc = [0]*n
    for j in range(1,n-1):
        jj = (v[j]<<1)
        i  = j-1
        k  = j+1
        while k<n and i>=0:
            ik = v[i]+v[k]
            if  ik>jj:
                i -= 1
                continue
            if  ik<jj:
                k += 1
                continue
            t1[i].append(j)
            t2[i].append(k)
            tv[i].append(False)
            tc[i]+=1
            i -= 1
            k += 1
    mx  = 2
    i   = -1
    while i+mx<n:
        i += 1
        if tvc[i]>=tc[i]:
            print("------------------------------")
            continue
        for ti in range(tc[i]):
            if tv[i][ti]:   #i-j-k is visted from i's view
                continue
            j,k = t1[i][ti],t2[i][ti]       #i => j-k
            sl  = 3
            tj  = 0
            while tj<tc[j]:
                kk = t1[j][tj]  #j's t1 = k
                if kk < k:
                    tj += 1
                    continue
                if kk > k:      #note that each t1[i], t2[i] is sorted
                    break
                tv[j][tj] = True
                tvc[j]   += 1
                k   = t2[j][tj] #j=kk=k, k=j's j
                j   = kk
                tj  = 0         #easy2MISS! <===
                sl += 1
            if sl>mx:
                mx=sl
                print('mx:',mx)
        print('i:',i,tc[i])
    return mx

_ = int(input())    #5000. O(N^2) is acceptable
l = sorted(list(map(int,input().split()))) #1e9
print(f(l))

