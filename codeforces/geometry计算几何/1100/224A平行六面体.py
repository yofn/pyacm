#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/224/A
#边为整数; 知道相邻三个面的面积; 求所有12个边的边长
#直角吗? 看用例是!
#相当于代数题:已知ab,bc,ac;求(a+b+c)*4
#注意是整数! 尽量避免浮点数运算?

from math import sqrt
a1,a2,a3 = list(map(int,input().split()))    #1e4
a,b,c    = sqrt((a2*a3)/a1), sqrt((a1*a3)/a2), sqrt((a1*a2)/a3)
print(4*int(a+b+c))
