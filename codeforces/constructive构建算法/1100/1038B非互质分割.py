#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/1038/B
# 构建题的例子往往有误导性!!
# 非唯一解时不要尝试重现例子..出题人不是带路党
# n*(n+1)/2 根据n的奇偶性, 将s1设为[1,n-1]或[1,n]

def f(n):
    if n<3:
        return ['No']
    l  = ['Yes']
    l.append('2 1 %d'%(n if n%2==0 else n-1))
    s2 = [n-2] + list(range(2,n-1)) + [n if n%2==1 else n-1]
    l.append(' '.join(map(str,s2)))
    return l

n = int(input())
[print(r) for r in f(n)]
