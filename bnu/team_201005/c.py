#!/usr/bin/env python3
'''
https://codeforces.com/group/H9K9zY8tcT/contest/297852
下车steps!
r,s,p (行数,每边座位数,人数),人的位置..
'''

def f(r,s,p,ll):
    fd = lambda p: p[0]+(p[1] if p[1]>0 else -p[1])
    fj = lambda j: s-(j-1) if j<=s else j-s
    ll = [[r-pp[0],fj(pp[1])] for pp in ll]
    dl = list(map(fd,ll))
    dl.sort()
    for i in range(1,len(dl)):
        dl[i] = max(dl[i-1]+1,dl[i])
    return dl[-1]+1

r,s,p =  list(map(int,input().split()))  #500,500
ll    = [list(map(int,input().split())) for _ in range(p)]
print(f(r,s,p,ll))

