#!/usr/bin/env python3
#ccpc20qhd-e
'''
#每个人有高低两个分; 得分>=最高分*p%的是可以通过的..
#求所有情况下，通过最多的人数!
不需要优先队列!
对b进行排序..
论断1: 最低的(max,线)是 (max(bi),*p)
论断2: 过的人数 = bi过线的人数(BL)! + bi没过线但是ai在(max,max*p)之间的人数(ABL)!
------
实现:
维护两个列表
+ 一个是bi过线的列表(sorted)
+ 一个是从上个列表淘汰下来的元素(按照ai排序)..根据(max,max*p)计算范围! 但需要一个快速的插入方法(二分+链表)!

低成本的插入和..

区间维护??
'''

from queue import PriorityQueue as PQ

def f(n,p,l):
    l.sort(key=lambda i:i[0])
    a  = [i[0] for i in l]
    b  = [i[1] for i in l]
    # print(a)
    # print(b)
    pqa = PQ()           #DYNAMIC tracking passed by scoring ai
    pqb = PQ()           #DYNAMIC tracking passed by scoring bi
    fsb = set()          #DYNAMIC tracking failed by scoring bi
    fsa = set()          #DYNAMIC tracking failed by scoring ai
    pca = [0]*(n+1)      #HISTORY count of pass by a: [0]=>all b; [n]=all a
    pcb = [0]*(n+1)      #HISTORY count of pass by b: [0]=>all b; [n]=all a

    mx = max(b)         #assume all scored bi
    pp = (mx*p)/100     #and get MINIMAL pass line!
    # print(mx,pp)
    for i in range(n):
        if b[i]>=pp:
            pqb.put((b[i],i))   #priority=score, value=student's index!
            pcb[0] += 1         #pass count of b
        else:
            fsb.add(i)

    for i in range(n):      # turning b[i] into a[i]
        # print('BEFORE %s: [FSA] %s; [FSB] %s'%(i,fsa,fsb))
        ii      = i+1       # number of ai's 
        pca[ii] = pca[i]
        pcb[ii] = pcb[i]
        if a[i] <= mx :     # LINE is same! no POPPING needed!
            # print('NO CHANGE',mx,pp)
            # case 1: from failed bi to passed ai, ap[i]++; 
            # case 3: from passed bi to passed ai, bp[i]--; ap[i]++
            # case 2: from failed bi to failed ai, DO NOTHING
            # case 4: from passed bi to failed ai (impossible! as ai>bi)
            if a[i]>=pp:
                pqa.put((a[i],i))
                pca[ii] += 1
                if i not in fsb:    #passed bi ==> passsed ai
                    fsb.add(i)
                    pcb[ii] -= 1
            else:
                fsa.add(i)
            continue

        # LINE is moving up
        mx = a[i]
        pp = (mx*p)/100
        # print('NEW LINE',mx,pp)

        # POPPING small a
        while not pqa.empty():
            aj,j = pqa.get()
            if aj >= pp:
                pqa.put((aj,j))
                break
            fsa.add(j)
            pca[ii] -= 1    # j is now failed

        # add i to PQA, inc(PCB)
        pqa.put((a[i],i))
        pca[ii] += 1

        # if i was in PQB, dec(PCB)
        if i not in fsb:
            pcb[ii] -= 1

        # POPPING small b
        while not pqb.empty():
            bj,j = pqb.get()
            if bj >= pp:
                pqb.put((bj,j))
                break
            fsb.add(j)

            #if j>=i:
            #print('-- from b',l[j])
            #pcb[ii] -= 1
    # print(pca)
    # print(pcb)
    return max([pca[i]+pcb[i] for i in range(n+1)])

t = int(input())
for i in range(t):
    n,p =  list(map(int,input().split()))
    l   = [list(map(int,input().split())) for _ in range(n)]
    print('Case #%d: %s'%((i+1), f(n,p,l)))

