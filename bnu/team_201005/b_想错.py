#!/usr/bin/env python3
'''
https://codeforces.com/group/H9K9zY8tcT/contest/297852
最长等差数列?
先排序... 想错了...
'''

def f(l):
    n  = len(l)
    mx = 0
    for i in range(n):
        for j in range(i+1,n):
            s = l[j]-l[i]
            c = sum([l[k]%s==l[i] for k in range(n)])   #CUBE!
            if c>mx:
                mx = c
                print(l[i],l[j],s)
            if j>n-c:
                break 
        if i>n-c:
            break
    return mx

_ = int(input())    #5000. O(N^2) is acceptable
l = sorted(list(map(int,input().split())))  #1e9
print(f(l))

