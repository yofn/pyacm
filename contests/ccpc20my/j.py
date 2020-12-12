#!/usr/bin/env python3
'''
n = 灯泡个数
m = 第n秒..
t = 周期
x = 亮度
每个bulb亮的时间=(1-t), (2t+1-3t), ..
求最大亮度..
sort by x?
sort by t?
一个t只要最大的x?
排除没有机会的?
+ 如果ti是tj的倍数，且xi比xj大，则可以排除!
如果用堆,先处理t大的,还是先处理t小的?
+ 先处理t大的,因为区间大?..  
    + 都可以??
论断:
    1 无法维护每个灯泡和m个时间的联合信息....
    2 如果t是从大到小处理，则一旦
    3 维护一个lcm? lcm之内的复制到后面就行???? 如果t很大就没必要?
    4 其实是按照周期=2t来?
    + 从小到大? 如果其倍数的x更大,则忽略?
    5 要不要维护一个倍数关系? 来处理《如果ti是tj的倍数，且xi比xj大，则可以排除!》
'''

'''
e5  = 100001
ll  = [[] for i in range(e5)]
for i in range(1,e5):
    for j in range(2, 1+(e5-1)//i):
        ll[i*j].append(i)
[print(i,*r[i]) for i in range(e5)]
        for j in ll[t]:
            if l1[t]>=l1[j]:
                l1[j]=0
'''

e5  = 100001
for i in range(int(input())):
    l1  = [0]*e5                        #l[t]=max x at period t 
    n,m = map(int,input().split())      #1e5
    l2  = [0]*(m+1)                     #r[t]=max light at time t
    for j in range(n):
        t,x = map(int,input().split())  #1e5
        if x>l1[t]:
            l1[t]=x
    for t in range(e5-1,0,-1):  #1-t, 2t+1-3t, 2kt+1, 2kt+t
        if l1[t]==0:
            continue
        l = 1
        x = l1[t]
        while l<=m:
            r = min(m+1,l+t)
            for j in range(l,r):
                if x>l2[j]:
                    l2[j] = x
            l = r+t
    print('Case #%d:'%(i+1), *l2[1:])

