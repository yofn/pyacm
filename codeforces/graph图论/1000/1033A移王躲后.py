#!/usr/bin/env python3

#https://codeforces.com/problemset/problem/1033/A
#王:3x3-1内移动; 后:对角/行/列
#回到数学解(这是一个很好的例子,数学insights非常非常重要!)

def okay(qr,qc,kr,kc,tr,tc):
    return (qr-kr)*(qr-tr)>0 and (qc-kc)*(qc-tc)>0

n       = int(input())  #1000
qr,qc   = [int(s)-1 for s in input().split()]
kr,kc   = [int(s)-1 for s in input().split()] 
tr,tc   = [int(s)-1 for s in input().split()] 
print('YES' if okay(qr,qc,kr,kc,tr,tc) else 'NO')

