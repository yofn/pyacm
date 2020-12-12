#!/usr/bin/env python3
#ccpc20wh
'''
3
2 2 2
3 1 10
11 45 14
n = n ppl
x = x minutes to rest!
t = across bridge

16
120
616

分析:
+ 来回送的时间(0边->1边 x 2n) AB+BA; 需要2nt的时间!
+ 这是老人的时间分别为0边(0-2t-4t-(2n-2)t) (t-3t-..(2n-1)t)
+ 来回送完之后(0边) 是等老人, 然后AB-BA
+ 0边等待时间=t-
n,x,t = 2,2,10 => (8,14),(10,12)  -> 12 + 8 = 20
n,x,t = 2,2,7  => (8,11),(10, 9)  -> 10 + 8 = 18
'''

def f(l):
    n,x,t = l
    return min(max(2*n*t,x+2*t),max(2*n*t+t,x+t))+2*n*t
    
n = int(input())
for i in range(n):
    l = list(map(int,input().split()))
    print(f(l))
