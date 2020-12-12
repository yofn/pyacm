#!/usr/bin/env python3
'''
    print('Case #%d: %s'%((i+1), f(a,b)))
分析:
    1
    5
    1 2
    2 3
    1 3
    4 5
    4 5
    dfs找环?
    或者更简单的做法? 如何利用袜子只有两个??
    https://www.jianshu.com/p/561e3550b13d
    //如果访问过，且不是其父节点，那么就构成环????
编码:
    注意: 说明中关于ai和bi的条件!!! 不能用数组!
    如何维护边关系: 双向还是单向?
    如何保证不会走回去?
'''

t = int(input())
for i in range(t):
    n   = int(input())
    el  = {}
    for j in range(n):
        f,t = list(map(int,input().split()))
        n1, n2 = f-1, t-1
        if n1 not in el:
            el[n1] = []
        if n2 not in el:
            el[n2] = []
        el[n1].append(n2)
        el[n2].append(n1)
    st  = [0]*n     #...
    mx  = 0
    uzd = set() #better than list!
    for i in range(n):
        if i in uzd:
            continue
        sp      = 0
        st[sp]  = i
        nn      = 0
        while sp>-1:
            pp  = st[sp]
            sp -= 1
            if pp in uzd:
                continue
            uzd.add(pp)
            nn += 1
            if pp not in el:
                continue
            for ii in el[pp]:
                if ii in uzd:
                    continue
                sp      += 1
                st[sp]   = ii
        if nn>mx:
            mx=nn
    print(mx)

