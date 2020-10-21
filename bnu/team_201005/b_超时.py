#!/usr/bin/env python3
'''
https://codeforces.com/group/H9K9zY8tcT/contest/297852
最长等差数列?
要用二分搜索?
nl = [l[i]-l[i-1] for i in range(1,n)]
n  = len(nl)
实际是一个图的问题? 广度优先搜索?
    print(l)
'''

def f(l):
    n  = len(l)
    dl = [[l[j]-l[i] for j in range(n)] for i in range(n)]
    mx = 2
    for i in range(n):
        if i>n-mx:
            break
        for j in range(i+1,n):
            if j>n-mx:
                break
            # choose s[0],s[1]
            if dl[i][j] is None:
                continue
            ss = dl[i][j]
            sl = 2
            cl = [l[i],l[j]]
            #print(ss,cl)
            while True:
                hasNext = False
                for k in range(j+1,n):
                    if dl[j][k]==ss:
                        sl += 1
                        cl.append(l[k])
                        j   = k
                        hasNext = True
                        dl[j][k]= None
                        break
                if not hasNext:
                    if sl > mx:
                        mx = sl
                        #print(mx,cl)
                    break
    return mx

_ = int(input())    #5000. O(N^2) is acceptable
l = sorted(list(map(int,input().split())))  #1e9
print(f(l))

