#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/727/A


def trans(a,b):
    l   = [b]
    while True:
        if l[-1]==a:
            l.reverse()
            return l
        if l[-1]<a:
            return []   #means NO
        if l[-1]%10 == 1:
            l.append(l[-1]//10)
            continue
        if l[-1]%2  == 0:
            l.append(l[-1]//2)
            continue
        return []       #means NO

a,b = list(map(int,input().split()))
r   = trans(a,b)
if  len(r)>0:
    print('YES')
    print(len(r))
    print(*r)
else:
    print('NO')

