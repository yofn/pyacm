#!/usr/bin/env python3

#https://codeforces.com/group/H9K9zY8tcT/contest/297258/problem/B
#贪心+拓扑排序

def f(ll):
    n  = len(ll)
    el = [l[0]  for l in ll]
    nl = [l[1]  for l in ll]
    pl = [[i-1 for i in l[2:]] for l in ll]    # parent topics of topic-i
    cl = [[] for i in range(n)]
    for i in range(n):
        for p in pl[i]:
            cl[p].append(i)
    tl = [[el[i],cl[i]] for i in range(n)]
    return tl


t = int(input())
l = [list(map(int,input().split())) for _ in range(t)]
print(f(l))
