#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/1030/B
#在区域内用半点集的交! 参考下面的oiwiki链接
#https://oi-wiki.org/geometry/half-plane/#_3

inhalf  = lambda A,B,C,p: (A*p[0]+B*p[1]+C)>=0
inR     = lambda n,d,p: inhalf(1,1,-d,p) and inhalf(-1,-1,(n<<1)-d,p) and inhalf(1,-1,d,p) and inhalf(-1,1,d,p)
n,d     =  list(map(int,input().split())) #100
ps      = [list(map(int,input().split())) for i in range(int(input()))]
[print('YES' if inR(n,d,p) else 'NO') for p in ps]

