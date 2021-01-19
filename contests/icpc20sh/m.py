#!/usr/bin/python3

def f(il,nil):
    fl  = set()
    for p in nil:
        pp = ''
        for dn in p:
            pp += '/' + dn
            fl.add(pp)
    rl  = set()
    for p in il:
        pp = ''
        for dn in p:
            pp += '/' + dn
            if pp not in fl:
                rl.add(pp)
                break
    return len(rl)

T  = int(input())
for i in range(T):
    n,m = list(map(int,input().split())) 
    il  = [input().split('/') for i in range(n)]
    nil = [input().split('/') for i in range(m)]
    print(f(il,nil))
