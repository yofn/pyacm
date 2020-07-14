#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/501/B

def changes(ul):
    o2n   = {u[0]:u[1] for u in ul}
    n2o   = {u[1]:u[0] for u in ul}
    for n in n2o.keys():
        print("check",n)
        if n in o2n:
            o2n[n2o[n]] = o2n[n]
            print("del",n)
            del o2n[n]
    return [len(o2n)] + ['%s %s'%(k,v) for k,v in o2n.items()]

ul  = [input().split() for _ in range(int(input()))] #1000;20
[print(r) for r in changes(ul)]

