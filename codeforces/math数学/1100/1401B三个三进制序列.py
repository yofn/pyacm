#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1401/B
# a,b的0,1,2个数给出; 可以任何排次序, 使得c=(aibi,0,-aibi)的总和最小..
# 构建题!
# 2=a2b1>a2b2=a2b0=0    ==> a=2的时候让b=1 (+2);        其他都是0
# 0=a1b1=a1b0>a1b2=-2   ==> a=1的时候尽量不对b2 (-2)!   其他都是0
# 0=a0b2=a0b1=a0b0      ==> a=0都一样!
# b=2的时候尽量不要对上a1 (-2); 其他都是0
# b=1的时候尽量对上a2 (+1);     其他都是0
# b=0的都是0!
# 所以只要注意两个case: a2b1 和 a1b2

def f(l1,l2):
    a0,a1,a2 = l1
    b0,b1,b2 = l2
    a2b1 = min(a2,b1)
    a2  -= a2b1
    b1  -= a2b1
    a1b2 = max(0, b2-a0-a2)
    return (a2b1-a1b2)<<1

q = int(input())
for _ in range(q):
    l1 = list(map(int,input().split()))
    l2 = list(map(int,input().split()))
    print(f(l1,l2))

