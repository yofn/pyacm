#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/596/A
#矩形顶点不全,如果能恢复则打印面积,否则打印-1

def area(ps):
    xl = [p[0] for p in ps]
    yl = [p[1] for p in ps]
    lx = max(xl)-min(xl)
    ly = max(yl)-min(yl)
    return lx*ly if lx*ly>0 else -1

ps  = [list(map(int,input().split())) for _ in range(int(input()))]
print(area(ps))

