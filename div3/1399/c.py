#!/usr/bin/python3
#https://codeforces.com/contest/1399/problem/C
#w1,w2,..wn.. 100
#n和w的范围非常小!

def f(l):
    n  = len(l)
    bl = [0]* 51
    sl = [0]*101
    for i in l:
        bl[i] += 1
    for i in range(1,51):
        for j in range(i,51):
            sl[i+j] += min(bl[i],bl[j]) if i!=j else bl[i]//2
    return max(sl)

T  = int(input())
for i in range(T):
    _ = input()
    l = list(map(int,input().split()))
    print(f(l))
