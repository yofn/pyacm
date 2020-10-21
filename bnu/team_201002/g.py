#!/usr/bin/env python3
#https://codeforces.com/group/H9K9zY8tcT/contest/297258/problem/G
#首先如何处理样例3? 不能经过(0,0)两次!  (看最后三个字符<--基于下面构建方法的基础上)
#什么问题?
#看题解: 用构造保证了后加的block不会改变前面的解!
#奇数上行驶,偶数上放块!(横的块x为偶数,竖的块y为偶数)
#   m   = {'L':[-2,0],'R':[2,0],'D':[0,-2],'U':[0,2]}
#       bl.append([b[0],bb[1]+2])

def f(l):
    is90 = lambda c1,c2: c1==None or (c1 in ['L','R'] and c2 in ['U','D']) or (c2 in ['L','R'] and c1 in ['U','D'])
    newb = lambda p,c,bbs: [[p[0],bbs],[p[0],-bbs]] if c in ['U','D'] else [[bbs,p[1]],[-bbs,p[1]]]
    tail = lambda t: t in ['LRL','RLR','UDU','DUD']
    if tail(''.join(l[-3:])):
        return [['impossible']]
    bbs = 0         #bounding box size
    p   = [0,0]     #p for ball, b for block, bb for bounding box
    pl  = [[0,0]]   #pl[0] for ball, others for blocks, AVOID shallow copy of p!
    cc  = None
    for c in l:
        if is90(cc,c):
            bbs += 2
            pl  = pl + newb(p,c,bbs)
        if   c=='U':
            p[1] = bbs-1
        elif c=='D':
            p[1] = 1-bbs
        elif c=='L':
            p[0] = 1-bbs
        else:
            p[0] = bbs-1
        cc = c
    pl  = [[b[0]-p[0],b[1]-p[1]] for b in pl]
    pl  = [pl[0]] + [[len(pl)-1]] + pl[1:]
    return pl

l = list(input())
[print(*r) for r in f(l)]
