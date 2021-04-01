#!/usr/bin/env python3
import cProfile

import io,os
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline

def f(n,a,b):
    a.sort()
    b.sort()
    tianji = -n
    for i in range(n+1):
        if i != 0 and a[n-i] <= b[i-1]:
            break
        cur  = -i
        flag = True
        for j in range(i,n):
            if (a[j-i] > b[j]):
                flag = False
            else:
                cur += a[j-i] < b[j]
        if flag:
            tianji = max(tianji, cur)
    if tianji < 0 :
        return 'win'
    if tianji > 0 : 
        return 'lose'
    return 'draw'

def main():
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    print(f(n,a,b))

cProfile.run("main()")
