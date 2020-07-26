#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/1284/B
#记录每个序列是否有上升，如果没有min.max是多少..
#n=1e5,还得避免O(N**2)..
#上升情况分解
#情况1: sx+sy中sx或sy本身是上升的
#情况2: sx,sy都不上升,判断四个极值的情况(存在几个上升)
#DP..增量计数; f(n+1)=f(n)+X; X=??
# 如果s本身上升,X=(2n+1)
# 如果s本身不升,拿s的min/max去一个数据结构去检查(min/max各一个?)..(低于线性..binary search??)
# ..

def bs(k,li):
    l, r    = 0, len(li)-1
    if li[l] >  k:  return 0
    if li[r] <= k:  return len(li)
    while True:     #HOLD: li[l]<= k < li[r] VERY important!
        if  r-l<2:  return r
        m   = l + ((r-l) >> 1)  #safer; NOTE: () for right order
        if  li[m]>k:
            r = m
        else:
            l = m

n    = int(input())
sll  = [list(map(int,input().split())) for _ in range(n)]
minl = []
maxl = []
for sl in sll:
    nn      = sl[0]
    m       = sl[1]
    ascent  = False
    if nn==1:
        minl.append(m)
        maxl.append(m)
        continue
    for i in range(2,nn+1):
        if sl[i] > m:
            ascent = True
            break
        else:
            m = sl[i]
    if not ascent:  # count non-ascenting
        minl.append(min(sl[1:]))
        maxl.append(max(sl[1:]))
maxs = sorted(maxl) #mins = sorted(minl)
cnt  = sum([bs(m,maxs) for m in minl])  # m+maxs, counting non-ascending (m >= maxs)
print(n*n-cnt)

