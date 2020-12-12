#!/usr/bin/env python3
#ccpc20qhd-e
'''
这次应该是想透了!
两个小堆:一个>max(M堆); 一个>max*p(p堆)
对b排序..每次被排除的b,对应的a就加入到这两个小堆中..
则以a过的人数   = 这两个小堆的人数差..
所有过线的人数  = 这两个小堆的人数差 + 比线高的b个数!
------
还有一个细节:
+ 是用b来步进还是用a?
论断: 因为是要求最大的, 所以要每次从M堆..pop出一个..再根据pass线维护p堆和b的列表..! 
'''

from queue import PriorityQueue as PQ

def f(n,p,l):
    l.sort(key=lambda i:i[1])
    mq = PQ()
    pq = PQ()
    mx = l[-1][1]       # max(b) 
    pl = mx*p/100
    i  = 0
    while i<n and l[i][1]<pl:  # no pass
        a = l[i][0]
        if a>pl:
            pq.put((a,i))
            if a>mx:
                mq.put((a,i))
        i += 1
    cl = [(n-i)+(pq.qsize()-mq.qsize())]
    #print('pl','n','i','pq','mq')
    while not mq.empty():
        mx,ai  = mq.get()    #no need to add into pq, as mq is included in pq.
        pl     = (mx*p)/100  #strictly increasing!?
        while i< n and l[i][1]<pl:
            a = l[i][0]
            if a>pl:
                pq.put((a,i))
                if a>mx:
                    mq.put((a,i))
            i += 1
        while pq.queue[0][0]<pl:
            pq.get()
        #print(mx,pl,n,i,pq.qsize(),mq.qsize(),pq.queue,mq.queue)
        cl.append((n-i)+(pq.qsize()-mq.qsize()))
    return max(cl)

t = int(input())
for i in range(t):
    n,p =  list(map(int,input().split()))
    l   = [tuple(map(int,input().split())) for _ in range(n)]
    print('Case #%d: %s'%((i+1), f(n,p,l)))

