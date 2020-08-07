#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1036/A
# 面积固定,求最小高度
# 性质: 每提高1, 面积增加1? 除了边上这两个!
# 题意理解错误: 注意只能移动奇数点~~

def f(ll):
    n,k = ll    #3e5
    return (k+n-1)//n

l = list(map(int,input().split()))
print(f(l))
