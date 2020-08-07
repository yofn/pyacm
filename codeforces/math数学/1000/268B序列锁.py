#!/usr/bin/env python3

# https://codeforces.com/problemset/problem/268/B
# 从1开始向上推,得到 f(n+1)=f(n)+n; f(1)=1
# 得到f(n)=n*(n-1)//2 + 1
# 注意f(n)的含义= 从1向前数第n个需要按的次数!
# g(n)=g(n-1)+n*(n-1)//2+1
# https://wenku.baidu.com/view/fa423a1c31b765ce050814bc.html
# https://zhuanlan.zhihu.com/p/26351880

n = int(input())    #2000
print(n+(n*(n-1)*(n+1))//6)
