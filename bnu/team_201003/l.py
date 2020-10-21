#!/usr/bin/env python3
'''
https://codeforces.com/group/H9K9zY8tcT/contest/297617
L题: 忽略进位的加法和乘法..给出N,求最小的a使得a*a=N
149=17*17的例子证明不能从后向前推导..
回溯法!
需要一个平方的map,还需要一个a*b*2=n的map. m[n][a]=[b list]
print(mm,sm)
深度为13的树的构建和搜索问题..用DFS来做?
'''

def makeMulMap():
    m = [[[] for _ in range(10)] for _ in range(10)]
    [m[(i*j*2)%10][i].append(j) for i in range(10) for j in range(9,-1,-1)]
    return m

def makeSqrMap():
    m = [[] for _ in range(10)]
    [m[(i*i)%10].append(i) for i in range(9,-1,-1)] #small
    return m

def f(l):
    mm  = makeMulMap()
    sm  = makeSqrMap()
    n   = len(l)
    if n%2==0:
        return -1
    m     = (n+1)//2
    al    = [None]*m
    sk    = [None]*8096
    sk[0] = (-1,0)
    sp    = 0
    while sp>-1:
        i,v = sk[sp]
        sp -= 1
        if i>=0:        #choose this value temporarily
            al[i]=v
        if i==(m-1):    #start verification
            valid = True
            for j in range(m,n):
                s = sum([al[ii]*al[j-ii] for ii in range(j-i,m)])
                if s%10 != l[j]:
                    valid = False
                    break
            if valid:
                return ''.join(list(map(str,al)))
            continue
        # push further nodes to stack
        j     = i+1
        cands = mm[(l[j]-sum([al[i]*al[j-i] for i in range(1,j)]))%10][al[0]] if j>0 else sm[l[0]]
        for a in cands:
            sp    += 1
            sk[sp] = (j,a)
    return -1

l   = list(map(int,input()))   #list of max25 digits
print(f(l))

