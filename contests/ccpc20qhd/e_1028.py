#!/usr/bin/env python3
#ccpc20qhd-e
#每个人有高低两个分; 得分>=最高分*p%的是可以通过的..
#求所有情况下，通过最多的人数!
'''
20A28   现在的解法有点长??没有相透?
分析: 大概率是要用到排序..排a还是排b?
    排序和双指针? + 二分搜索?
    优先队列..
    对a排序..假设选择aj
    所有i<j的都选择b
    所有i>j的都选择a
    然后检查有多少是>=aj*p% .. 根据更新的值来数数??
分析结果:
    方法1:
        维护两个排序的列表, a和b
        + a的好维护, b的较复杂(但其实也就是相当于查询,不过最好用链表来维护b), 
        做两次二分查找，加起来等于过的人数
        以这个为基础，看后面还有没有优化的空间
        复杂度分析平时多练，比赛的时候要快（可以模糊点、有个范围）
    方法2:
        先让及格线尽可能低,后逐步提高及格线; 这样做的好处是
        然后把bl变成一个小根堆..
        用优先队列的话, put和get没问题, 如何一个元素呢? i从b->a, 要从b中取走bi!
        所以需要自己实现一个二叉堆? 或者使用heapq?
        也许不需要? 可以跟踪一下被移除的item也反推Q大小..
        反过来也行，让及格线从高到低变化，然后跟踪及格的人数(大根堆/反向优先队列)？
        优先队列本来就是tuple (priority,value)
        用PriorityQueue实现还是有点尴尬,因为我们不一定取,我们还要检查!
        还是手写一个堆?
        bi->ai时从b堆删除一个item怎么搞呢?
        解决方法:
        + 如果从b堆中删除的节点<i就认为这是一个无效的删除..因为bi已经不存在!!
        + 我们只要记录从b堆中进行了多少次的有效删除，就知道b堆中有有效元素的个数(有效及格)
编码:
    函数1: 二分
    函数2: 维护bl
    函数3: 处理每个case!
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

