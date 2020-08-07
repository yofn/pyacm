#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1051/B
# 3e5, 所以不能n**2复杂度!
# 分成两边,两两互质..
# 性质: 两个偶数不能互质!
# 差为1的总是互质
# 被例子误导了,还以为有多难~~
# https://codeforces.com/blog/entry/61969


def f(ll):
    l,r = ll    #3e5
    rl  = ['YES']
    for i in range(l,r+1,2):
        rl.append('%d %d'%(i,i+1))
    return rl

l = list(map(int,input().split()))
[print(r) for r in f(l)]
