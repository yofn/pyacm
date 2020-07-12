#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/1057/A
#给出新路由连接到的旧路由,让寻找从1-n的路径

n  = int(input())   #2e5
pl = list(map(int,input().split())) #p2开始
ll = [n]
while ll[-1]>1:
    ll.append(pl[ll[-1]-2])
ll.reverse()
print(*ll)
