#!/usr/bin/env python3
# brute-force or 01 backpack!
 
# from big to small: 1-7

c = [648,328,198,88,28, 6,1]
r = [388,198,128,58,28,18,8]

def f(n):
    if n>=1297: #All
        return (n-1297)*10 + 826
    if n>=969:  #134567
        return  (n-969)*10 + 628
    s = 0
    if n>=648:  #23456 or 1
        n -= 648
        s += 430

n = int(input())
print(f(n))
