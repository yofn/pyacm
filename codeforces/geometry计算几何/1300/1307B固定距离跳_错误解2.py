#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/1307/B
#欧式距离..比预想的复杂些..
#三角形.多边形? 多边形条件? 1直接->2三角形->3四边形->..
#之前的错误假设所有跳都小于x


tit = lambda l: (max(l)<<1)<=sum(l) #allow degenerate

def noh(al,x):
    if x in al:
        return 1
    al.append(x)
    al.sort(reverse=True)   #nlogn
    xi  = al.index(x)
    # find polygon start from n=3(triangle, noh=2)
    n   = 3
    while True:
        lrl = [(xi+i-n,xi+i+1) for i in range(0,n) if xi+i-n>0 and xi+i+1<n]
        print(lrl)
        for l,r in lrl:
            if tit(al[l:r]):
                return n-1
        n  += 1

t   = int(input())
for i in range(t):
    n,x = list(map(int,input().split())) 
    al  = list(map(int,input().split()))    #1e5
    print(noh(al,x))
